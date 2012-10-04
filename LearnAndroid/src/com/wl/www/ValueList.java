package com.wl.www;

import java.util.ArrayList;

public class ValueList
{
    private double vMax;
    private double vMin;
    private ArrayList<Double> values;

    public ValueList()
    {
	super();
	values = new ArrayList<Double>();
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

    public double get(int index) { return values.get(index); }
    public int size() { return values.size(); }
    public double getVMax() { return vMax; }
    public double getVMin() { return vMin; }
}
