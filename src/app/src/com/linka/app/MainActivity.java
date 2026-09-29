package com.linkaProject.LinkaAi;
import android.widget.TextView;
import android.app.Activity;
import android.os.Bundle;
import android.widget.Button;
import android.view.animation.AnimationUtils;
public class MainActivity extends Activity {
    private TextView txtHome;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        txtHome = findViewById(R.id.txtHome);
        txtHome.startAnimation(AnimationUtils.loadAnimation(this, R.anim.slide_bounce));
    }
}
