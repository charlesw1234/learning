package com.wl.www;

import java.util.ArrayList;
import org.json.JSONArray;
import org.json.JSONException;

public class ValueArrayList
{
    private int offset;
    private ArrayList<Double> vmax;
    private ArrayList<Double> vmin;
    private ArrayList<double[]> valist;

    public ValueArrayList()
    {
	super();
	offset = 0;
	vmax = new ArrayList<Double>();
	vmin = new ArrayList<Double>();
	valist = new ArrayList<double[]>();
    }

    public void setOffset(int _offset)
    {
	offset = _offset;
    }

    public void append(double[] varray)
    {
	valist.add(varray);
	for (int col = 0; col < varray.length; ++col) {
	    if (vmax.size() == col) vmax.add(varray[col]);
	    else if (vmax.get(col) < varray[col]) vmax.set(col, varray[col]);
	    if (vmin.size() == col) vmin.add(varray[col]);
	    else if (vmin.get(col) > varray[col]) vmin.set(col, varray[col]);
	}
    }

    public void append(JSONArray jarray)
    {
	try {
	    for (int i = 0; i < jarray.length(); ++i) {
		JSONArray jarray0 = jarray.getJSONArray(i);
		double[] varray = new double[jarray0.length()];
		for (int j = 0; j < jarray0.length(); ++j)
		    //varray[j] = jarray0.getDouble(j);
		    varray[j] = jarray0.getInt(j);
		append(varray);
	    }
	} catch (JSONException ex) {
	}
    }

    public boolean in(int index)
    {
	return index >= offset && index < offset + valist.size();
    }
    public double get(int index, int col) { return valist.get(index - offset)[col]; }
    public int size() { return valist.size(); }
    public double max(int... cols)
    {
	double value = vmax.get(cols[0]);
	for (int i = 1; i < cols.length; ++i)
	    if (value < vmax.get(cols[i])) value = vmax.get(cols[i]);
	return value;
    }
    public double min(int... cols)
    {
	double value = vmin.get(cols[0]);
	for (int i = 1; i < cols.length; ++i)
	    if (value > vmin.get(cols[i])) value = vmin.get(cols[i]);
	return value;
    }
}
