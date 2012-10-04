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
	int x0, x1, y0, y1;
	super.onDraw(canvas);
	ValueTransform vtrans = new ValueTransform(0, this.getHeight());
	vtrans.update(vlist);
	int barw = this.getWidth() / vlist.size();
	mPaint.setColor(Color.RED);
	x0 = barw / 2; y0 = vtrans.transform(vlist.get(0));
	for (int i = 1; i < vlist.size(); ++i) {
	    x1 = x0 + barw;
	    y1 = vtrans.transform(vlist.get(i));
	    canvas.drawLine(x0, y0, x1, y1, mPaint);
	    x0 = x1; y0 = y1;
	}
    }
}
