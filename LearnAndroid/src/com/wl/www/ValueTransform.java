package com.wl.www;

import com.wl.www.ValueList;

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

    public void update(double _vMax, double _vMin)
    {
	if (trans == 0) {
	    vMax = _vMax;
	    vMin = _vMin;
	} else {
	    if (vMax < _vMax) vMax = _vMax;
	    if (vMin > _vMin) vMin = _vMin;
	}
	trans = (iMax - iMin) / (vMax - vMin);
    }

    public void update(ValueList vlist)
    {
	update(vlist.getMax(), vlist.getMin());
    }

    public int transform(double value)
    {
	return (int)((value - vMin) * trans) + iMin;
    }
}
