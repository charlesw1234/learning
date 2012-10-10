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
import com.wl.www.ChartKLine;

public class Chart extends View
{
    private Paint[] mPaintsLine;
    private Paint[] mPaintsKLine;
    private ValueArrayList valist;
    private ChartLine cline;
    private ChartKLine ckline;

    public Chart(Context context, AttributeSet attrs)
    {
	super(context, attrs);
	mPaintsLine = new Paint[]{ new Paint() };
	mPaintsLine[0].setColor(Color.WHITE);
	mPaintsKLine = new Paint[]{ new Paint(), new Paint() };
	mPaintsKLine[0].setColor(Color.RED);
	mPaintsKLine[0].setStyle(Paint.Style.STROKE);
	mPaintsKLine[1].setColor(Color.GREEN);
	mPaintsKLine[1].setStyle(Paint.Style.FILL);

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
		valist = new ValueArrayList();
		valist.append(new JSONArray(text));
		cline = new ChartLine(valist, 4, 0);
		ckline = new ChartKLine(valist, 1, 2, 3, 4);
	    } catch (JSONException ex) {
	    }
	} catch (IOException ex) {
	}

    }

    @Override public void onDraw(Canvas canvas)
    {
	super.onDraw(canvas);
	ValueTransform vtrans = new ValueTransform(0, this.getHeight());
	vtrans.update(valist, 1, 2,3, 4);
	canvas.drawText(String.format("%d, %f, %f", valist.size(), valist.min(1, 2, 3, 4), valist.max(1, 2, 3, 4)),
			0, 50, mPaintsLine[0]);
	ckline.onDraw(canvas, mPaintsKLine,
		      0, valist.size(),
		      0, this.getWidth(),
		      vtrans);
	cline.onDraw(canvas, mPaintsLine,
		     0, valist.size(),
		     0, this.getWidth(),
		     vtrans);
    }
}
