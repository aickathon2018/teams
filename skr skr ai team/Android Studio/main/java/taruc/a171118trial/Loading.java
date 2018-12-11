package taruc.a171118trial;

import android.animation.ObjectAnimator;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.os.Handler;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

public class Loading extends AppCompatActivity {

    private ImageView imageView1;
    private static int SPLASH_TIME_OUT=2000;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        imageView1 = (ImageView) findViewById(R.id.imageView1);
        MediaPlayer skrr = MediaPlayer.create(Loading.this,R.raw.skrr);
        skrr.start();
        ObjectAnimator rotate = ObjectAnimator.ofFloat(imageView1, "rotation", 0f, 20f, 0f, -20f, 0f); // rotate o degree then 20 degree and so on for one loop of rotation.
// animateView (View object)
        rotate.setRepeatCount(5); // repeat the loop 20 times
        rotate.setDuration(300); // animation play time 100 ms
        rotate.start();
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                Intent homeIntent = new Intent (Loading.this,ParkingMark.class);
                startActivity(homeIntent);
                finish();
            }
        },SPLASH_TIME_OUT);

    }

}





