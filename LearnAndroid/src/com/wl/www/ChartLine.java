package com.wl.www;

import android.graphics.Canvas;
import android.graphics.Paint;
import com.wl.www.ValueArrayList;
import com.wl.www.ValueTransform;
import com.wl.www.ChartBase;

public class ChartLine extends ChartBase
{
    public ChartLine(ValueArrayList _valist)
    {
	super(_valist);
    }

    public void onDraw(Canvas canvas, Paint[] mPaints,
		       int iStart, int iStop,
		       int xStart, int xEnd,
		       ValueTransform ytrans)
    {
	boolean first = true;
	int x0, x1, y0, y1, w;
	super.onDraw(canvas, mPaints, iStart, iStop, xStart, xEnd, ytrans);
	w = (xEnd - xStart) / (iStop - iStart);
	x0 = 0; y0 = 0;
	for (int i = iStart; i < iStop; ++i) {
	    x1 = x0 + w;
	    if (valist.in(i)) {
		y1 = ytrans.transform(valist.get(i, 0));
		if (!first)
		    canvas.drawLine((x0 + x1) / 2 - w, y0,
				    (x0 + x1) / 2, y1, mPaints[0]);
		y0 = y1;
		first = false;
	    }
	    x0 = x1;
	}
    }
}
