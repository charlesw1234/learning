package com.wl.www;

import java.io.IOException;
import java.io.InputStream;

import org.json.JSONObject;
import org.json.JSONArray;
import org.json.JSONException;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.StatusLine;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;

import android.app.Activity;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.widget.TextView;

public class LearnAndroidActivity extends Activity
{
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
	TextView tv1, tv2;
	DisplayMetrics dm;
	String jweather;
	JSONObject jobj;

        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

	dm = new DisplayMetrics();
	getWindowManager().getDefaultDisplay().getMetrics(dm);
	tv1 = (TextView)findViewById(R.id.tv1);
	tv1.setText("Hello Screen(" + dm.widthPixels + " * " +
		    dm.heightPixels + ")");

	tv2 = (TextView)findViewById(R.id.tv2);
	HttpClient client = new DefaultHttpClient();
	HttpGet request = new HttpGet("http://www.weather.com.cn/data/sk/101110101.html");
	jweather = "{ 'ok': false }";
	try {
	    HttpResponse response = client.execute(request);
	    HttpEntity entity = response.getEntity();
	    InputStream istream = entity.getContent();
	    byte[] sbuf = new byte[512];
	    istream.read(sbuf);
	    jweather = new String(sbuf);
	    try {
		jobj = new JSONObject(jweather);
		tv2.setText(String.format("Hello Json(%s)", jobj.toString()));
	    } catch (JSONException ex) {
		tv2.setText("JSONObject failed");
	    }
	} catch (IOException ex) {
	    tv2.setText(String.format("client.execute(%s), %s",
				      jweather, ex.toString()));
	}
    }
}
