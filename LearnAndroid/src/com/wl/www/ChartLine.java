package com.wl.www;

import android.graphics.Canvas;
import android.graphics.Paint;
import com.wl.www.ValueArrayList;
import com.wl.www.ValueTransform;
import com.wl.www.ChartBase;

public class ChartLine extends ChartBase
{
    private int vcol, pcol;

    public ChartLine(ValueArrayList _valist, int _vcol, int _pcol)
    {
	super(_valist);
	vcol = _vcol;
	pcol = _pcol;
    }

    public void onDraw(Canvas canvas, Paint[] mPaints,
		       int iStart, int iStop, int xStart, int xEnd,
		       ValueTransform ytrans)
    {
	boolean first = true;
	int x0, x1, y0, y1, w;

	w = (xEnd - xStart) / (iStop - iStart);
	x0 = 0; y0 = 0;
	for (int i = iStart; i < iStop; ++i) {
	    x1 = x0 + w;
	    if (valist.in(i)) {
		y1 = ytrans.transform(valist.get(i, vcol));
		if (!first)
		    canvas.drawLine((x0 + x1) / 2 - w, y0,
				    (x0 + x1) / 2, y1, mPaints[pcol]);
		y0 = y1;
		first = false;
	    }
	    x0 = x1;
	}
    }
}
