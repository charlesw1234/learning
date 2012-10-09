package com.wl.www;

import com.wl.www.ValueArrayList;

public class hello
{
    public static void main(String args[])
    {
	ValueArrayList valist = new ValueArrayList();
	Double[] varr;
	varr = new Double[2];
	varr[0] = 1.0;
	varr[1] = 1.3;
	valist.append(varr);
	varr = new Double[3];
	varr[0] = 0.92;
	varr[1] = 0.99;
	varr[2] = 0.98;
	valist.append(varr);
	System.out.printf("Hello Java %d: %4.2f, %4.2f\n", valist.size(), valist.getMax(), valist.getMin());
    }
}
