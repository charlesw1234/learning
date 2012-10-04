package com.wl.www;

import java.util.ArrayList;

public class ValueList
{
    private int offset;
    private double vMax;
    private double vMin;
    private ArrayList<Double> values;

    public ValueList()
    {
	super();
	offset = 0;
	values = new ArrayList<Double>();
    }

    public void setOffset(int _offset)
    {
	offset = _offset;
    }

    public void append(double value)
    {
	if (values.size() == 0) {
	    vMax = vMin = value;
	} else {
	    if (vMax < value) vMax = value;
	    if (vMin > value) vMin = value;
	}
	values.add(value);
    }

    public boolean in(int index)
    {
	return index >= offset && index < offset + values.size();
    }
    public double get(int index) { return values.get(index - offset); }
    public int size() { return values.size(); }
    public double getMax() { return vMax; }
    public double getMin() { return vMin; }
}
