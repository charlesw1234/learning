package com.wl.www;

import android.graphics.Canvas;
import android.graphics.Paint;
import com.wl.www.ValueArrayList;
import com.wl.www.ValueTransform;

public abstract class ChartBase
{
    protected ValueArrayList valist;

    protected ChartBase(ValueArrayList _valist)
    {
	super();
	valist = _valist;
    }

    public abstract void onDraw(Canvas canvas, Paint[] mPaints,
				int iStart, int iStop, int xStart, int xEnd,
				ValueTransform ytrans);
}
