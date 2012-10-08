package com.wl.www;

import com.wl.www.ValueList;

public class hello
{
    public static void main(String args[])
    {
	ValueList vlist = new ValueList();
	vlist.append(1.0);
	vlist.append(1.02);
	vlist.append(0.92);
	System.out.printf("Hello Java: %4.2f, %4.2f\n", vlist.getMax(), vlist.getMin());
    }
}
