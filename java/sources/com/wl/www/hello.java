package com.wl.www;

import com.wl.www.ValueArrayList;

public class hello
{
    public static void main(String args[])
    {
	ValueArrayList valist = new ValueArrayList();
	valist.append(new double[]{ 1.0, 1.3 });
	valist.append(new double[]{ 0.92, 0.99, 0.98 });
	System.out.printf("Hello Java %d: %4.2f, %4.2f\n", valist.size(), valist.getMax(), valist.getMin());
    }
}
