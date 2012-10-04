package com.wl.www;

import android.graphics.Canvas;
import android.graphics.Paint;
import com.wl.www.ValueList;
import com.wl.www.ValueTransform;

public class ChartBase
{
    protected ValueList vlist;

    public ChartBase(ValueList _vlist)
    {
	super();
	vlist = _vlist;
    }

    public void onDraw(Canvas canvas, Paint mPaint,
		       int iStart, int iStop,
		       int xStart, int xEnd,
		       ValueTransform ytrans)
    {
    }
}
