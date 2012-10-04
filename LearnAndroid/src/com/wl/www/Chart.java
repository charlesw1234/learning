package com.wl.www;

import java.io.IOException;
import java.io.InputStream;
import java.io.ByteArrayOutputStream;

import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONException;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.View;

import com.wl.www.ValueList;
import com.wl.www.ValueTransform;
import com.wl.www.ChartLine;

public class Chart extends View
{
    private Paint mPaint;
    private ValueList vlist;

    public Chart(Context context, AttributeSet attrs)
    {
	super(context, attrs);
	mPaint = new Paint();
	vlist = new ValueList();

	try {
	    InputStream is = context.getAssets().open("data.json");
	    byte[] buf = new byte[1024];
	    ByteArrayOutputStream arrOS = new ByteArrayOutputStream();
	    while (is.read(buf) != -1) arrOS.write(buf, 0, buf.length);
	    is.close();
	    arrOS.close();
	    String text = new String(arrOS.toByteArray());
	    text.trim();
	    try {
		JSONArray jarr = new JSONArray(text);
		for (int i = 0; i < jarr.length(); ++i)
		    vlist.append(jarr.getDouble(i));
	    } catch (JSONException ex) {
	    }
	} catch (IOException ex) {
	}

    }

    @Override public void onDraw(Canvas canvas)
    {
	super.onDraw(canvas);
	ValueTransform vtrans = new ValueTransform(0, this.getHeight());
	vtrans.update(vlist);
	ChartLine cline = new ChartLine(vlist);
	mPaint.setColor(Color.RED);
	cline.onDraw(canvas, mPaint,
		     0, vlist.size(),
		     0, this.getWidth(),
		     vtrans);
    }
}
