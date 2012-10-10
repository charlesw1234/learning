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

import com.wl.www.ValueArrayList;
import com.wl.www.ValueTransform;
import com.wl.www.ChartLine;

public class Chart extends View
{
    private Paint[] mPaints;
    private ValueArrayList valist;

    public Chart(Context context, AttributeSet attrs)
    {
	super(context, attrs);
	mPaints = new Paint[]{ new Paint(), new Paint() };
	mPaints[0].setColor(Color.RED);
	mPaints[1].setColor(Color.GREEN);
	valist = new ValueArrayList();

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
		    valist.append(new double[]{jarr.getDouble(i)});
	    } catch (JSONException ex) {
	    }
	} catch (IOException ex) {
	}

    }

    @Override public void onDraw(Canvas canvas)
    {
	super.onDraw(canvas);
	ValueTransform vtrans = new ValueTransform(0, this.getHeight());
	vtrans.update(valist);
	ChartLine cline = new ChartLine(valist);
	cline.onDraw(canvas, mPaints,
		     0, valist.size(),
		     0, this.getWidth(),
		     vtrans);
    }
}
