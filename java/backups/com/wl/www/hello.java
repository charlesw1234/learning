package com.wl.www;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;
import com.wl.www.ValueArrayList;

public class hello
{
    public static void main(String args[])
    {
	ValueArrayList valist = new ValueArrayList();
	valist.append(JSONArray.fromObject("[[ 1.0, 1.3 ], [ 0.92, 0.99, 0.98 ]]"));
	System.out.printf("Hello Java %d: %4.2f, %4.2f\n", valist.size(), valist.getMax(), valist.getMin());
    }
}
