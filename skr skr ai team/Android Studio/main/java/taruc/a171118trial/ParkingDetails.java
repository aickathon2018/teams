package taruc.a171118trial;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;


import com.bumptech.glide.load.engine.DiskCacheStrategy;
import com.bumptech.glide.request.RequestOptions;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;


public class ParkingDetails extends AppCompatActivity {
    FirebaseDatabase database = FirebaseDatabase.getInstance();
    DatabaseReference myRef = database.getReference("aeon");

    private static int SPLASH_TIME_OUT=2000;
    public final static String MESSAGE_KEY ="ganeshannt.senddata.message_key";
    public final static String MESSAGE_KEY_2 ="ganeshannt.senddata.message_key_2";
    private ImageView imageView2;
    private static final String TAG = "MainActivity";
    private TextView textView;
    private TextView textView2;
    private Button button1;
    private Button button2;
    private Button button3;
    private Button button4;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_parking_details);

        Intent intent = getIntent();
        String message = intent.getStringExtra(MESSAGE_KEY);
        textView = (TextView) findViewById(R.id.textView);
        textView.setText("  :  " + message);
        String message2 = intent.getStringExtra(MESSAGE_KEY_2);
        textView2 = (TextView) findViewById(R.id.textView2);
        textView2.setText("  :  " + message2);

        init();

        button1 = (Button) findViewById(R.id.button);
        button1.setEnabled(false);

        button2 = (Button) findViewById(R.id.button2);
        button2.setEnabled(false);


        button3 = (Button) findViewById(R.id.button3);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                HOME();
            }
        });

        button4 = (Button) findViewById(R.id.button4);
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Refresh();
            }
        });

    }

    private void init(){

        imageView2=(ImageView)findViewById(R.id.imageView2);
        String url = "https://firebasestorage.googleapis.com/v0/b/rpiappcontrol-1f76e.appspot.com/o/carpark%2Fcarpark?alt=media&token=";
        // Glide.get(getApplicationContext()).clearDiskCache();
        GlideApp.with(this).load(url).apply(RequestOptions.skipMemoryCacheOf(true)).diskCacheStrategy(DiskCacheStrategy.NONE).into(imageView2);
        //Glide.get(getApplicationContext()).clearMemory();
        myRef.child("free").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                String value = dataSnapshot.getValue(String.class);
                //Log.d(TAG, "Value is: " + value);
                textView = (TextView) findViewById(R.id.textView);
                textView.setText("  :  " + value);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
        myRef.child("occupied").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                String value2 = dataSnapshot.getValue(String.class);
                //Log.d(TAG, "Value is: " + value);
                textView2 = (TextView) findViewById(R.id.textView2);
                textView2.setText("  :  " + value2);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });


    }

    private void HOME(){
        Intent intent= new Intent(this ,ParkingMark.class);
        startActivity(intent);
    }

    private void Refresh(){
        imageView2=(ImageView)findViewById(R.id.imageView2);
        String url = "https://firebasestorage.googleapis.com/v0/b/rpiappcontrol-1f76e.appspot.com/o/carpark%2Fcarpark?alt=media&token=";
        // Glide.get(getApplicationContext()).clearDiskCache();
        GlideApp.with(this).load(url).apply(RequestOptions.skipMemoryCacheOf(true)).diskCacheStrategy(DiskCacheStrategy.NONE).into(imageView2);
        //Glide.get(getApplicationContext()).clearMemory();
        myRef.child("free").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                String value = dataSnapshot.getValue(String.class);
                //Log.d(TAG, "Value is: " + value);
                textView = (TextView) findViewById(R.id.textView);
                textView.setText("  :  " + value);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
        myRef.child("occupied").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                String value2 = dataSnapshot.getValue(String.class);
                //Log.d(TAG, "Value is: " + value);
                textView2 = (TextView) findViewById(R.id.textView2);
                textView2.setText("  :  " + value2);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {

            }
        });
    }
}