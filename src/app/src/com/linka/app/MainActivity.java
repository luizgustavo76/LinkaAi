package com.linkaProject.LinkaAi;
import android.widget.TextView;
import android.app.Activity;
import android.os.Bundle;
import android.view.animation.AnimationUtils;
public class MainActivity extends Activity {
    private TextView txtHome;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login);
        txtHome = findViewById(R.id.txtHome);
        txtHome.startAnimation(AnimationUtils.loadAnimation(this, R.anim.slide_bounce));
    }
}
