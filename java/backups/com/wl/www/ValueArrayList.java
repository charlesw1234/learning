package com.wl.www;

import java.util.ArrayList;
import net.sf.json.JSONArray;

public class ValueArrayList
{
    private int offset;
    private double vMax;
    private double vMin;
    private ArrayList<double[]> valist;

    public ValueArrayList()
    {
	super();
	offset = 0;
	valist = new ArrayList<double[]>();
    }

    public void setOffset(int _offset)
    {
	offset = _offset;
    }

    public void append(double[] varray)
    {
	int idx;
	if (valist.size() > 0) {
	    idx = 0;
	} else {
	    vMax = vMin = varray[0];
	    idx = 1;
	}
	while (idx < varray.length) {
	    if (vMax < varray[idx]) vMax = varray[idx];
	    if (vMin > varray[idx]) vMin = varray[idx];
	    ++idx;
	}
	valist.add(varray);
    }

    public void append(JSONArray jarray)
    {
	for (int i = 0; i < jarray.size(); ++i) {
	    JSONArray jarray0 = jarray.getJSONArray(i);
	    double[] varray = new double[jarray0.size()];
	    for (int j = 0; j < jarray0.size(); ++j)
		varray[j] = jarray0.getDouble(j);
	    append(varray);
	}
    }

    public boolean in(int index)
    {
	return index >= offset && index < offset + valist.size();
    }
    public double get(int index, int col) { return valist.get(index - offset)[col]; }
    public int size() { return valist.size(); }
    public double getMax() { return vMax; }
    public double getMin() { return vMin; }
}
