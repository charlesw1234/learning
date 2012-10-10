package com.wl.www;

import com.wl.www.ValueArrayList;

public class ValueTransform
{
    private double vMax, vMin;
    private int iMax, iMin;
    private double trans;

    public ValueTransform(int _iMax, int _iMin)
    {
	trans = 0;
	iMax = _iMax;
	iMin = _iMin;
    }

    public void update(double value)
    {
	if (trans == 0) {
	    vMax = vMin = value;
	} else {
	    if (vMax < value) vMax = value;
	    if (vMin > value) vMin = value;
	}
	trans = (iMax - iMin) / (vMax - vMin);
    }

    public void update(ValueArrayList valist, int... cols)
    {
	update(valist.max(cols));
	update(valist.min(cols));
    }

    public int transform(double value)
    {
	return (int)((value - vMin) * trans) + iMin;
    }
}
