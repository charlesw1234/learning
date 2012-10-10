package com.wl.www;

import android.graphics.Canvas;
import android.graphics.Paint;
import com.wl.www.ValueArrayList;
import com.wl.www.ValueTransform;
import com.wl.www.ChartBase;

public class ChartKLine extends ChartBase
{
    private int copen, cmax, cmin, cclose;
    public ChartKLine(ValueArrayList _valist, int _copen, int _cmax, int _cmin, int _cclose)
    {
	super(_valist);
	copen = _copen;
	cmax = _cmax;
	cmin = _cmin;
	cclose = _cclose;
    }

    public void onDraw(Canvas canvas, Paint[] mPaints,
		       int iStart, int iStop,
		       int xStart, int xEnd,
		       ValueTransform ytrans)
    {
	boolean first = true;
	int x0, x1, w;
	double vopen, vclose;
	int yopen, ymax, ymin, yclose;

	super.onDraw(canvas, mPaints, iStart, iStop, xStart, xEnd, ytrans);
	w = (xEnd - xStart) / (iStop - iStart);
	x0 = 0;
	for (int i = iStart; i < iStop; ++i) {
	    x1 = x0 + w;
	    if (valist.in(i)) {
		yopen = ytrans.transform(vopen = valist.get(i, copen));
		ymax = ytrans.transform(valist.get(i, cmax));
		ymin = ytrans.transform(valist.get(i, cmin));
		yclose = ytrans.transform(vclose = valist.get(i, cclose));
		if (vopen <= vclose) {
		    canvas.drawLine((x0 + x1) / 2, ymax,
				    (x0 + x1) / 2, yclose, mPaints[0]);
		    canvas.drawLine((x0 + x1) / 2, yopen,
				    (x0 + x1) / 2, ymin, mPaints[0]);
		    canvas.drawRect(x0 + 3, yopen, x1 - 3, yclose, mPaints[0]);
		} else {
		    canvas.drawLine((x0 + x1) / 2, ymax,
				    (x0 + x1) / 2, yopen, mPaints[1]);
		    canvas.drawLine((x0 + x1) / 2, yclose,
				    (x0 + x1) / 2, ymin, mPaints[1]);
		    canvas.drawRect(x0 + 3, yclose, x1 - 3, yopen, mPaints[1]);
		}
		first = false;
	    }
	    x0 = x1;
	}
    }
}
