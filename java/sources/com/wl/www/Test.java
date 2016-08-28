package com.wl.www;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Test {
    public static void main(String args[]) throws Exception {
        FileInputStream fis = new FileInputStream(new File("test.json"));
        byte[] fbody = new byte[4096];
        int fbodylen = fis.read(fbody);
        fis.close();

        String docstr = new String(fbody, 0, fbodylen, "UTF-8");
        RapidDocument doc0 = new RapidDocument(docstr);
        FreezeDocument4 doc40 = doc0.Freeze4(doc0.GetRoot());
        FreezeDocument8 doc80 = doc0.Freeze8(doc0.GetRoot());
        ObjectOutputStream oos4 = new ObjectOutputStream
            (new FileOutputStream(new File("test4.bin")));
        oos4.writeObject(doc40);
        oos4.close();
        ObjectOutputStream oos8 = new ObjectOutputStream
            (new FileOutputStream(new File("test8.bin")));
        oos8.writeObject(doc80);
        oos8.close();

        System.out.printf("Root Object Size = %d, %d\n",
                          doc40.GetObjectSize(doc40.GetRoot()),
                          doc80.GetObjectSize(doc80.GetRoot()));

        ObjectInputStream ois4 = new ObjectInputStream
            (new FileInputStream(new File("test4.bin")));
        FreezeDocument4 doc41 = (FreezeDocument4)ois4.readObject();
        ois4.close();
        ObjectInputStream ois8 = new ObjectInputStream
            (new FileInputStream(new File("test8.bin")));
        FreezeDocument8 doc81 = (FreezeDocument8)ois8.readObject();
        ois8.close();

        System.out.printf("BodySize1 = %d, %d, BodySize2 = %d, %d\n",
                          doc40.BodySize(), doc80.BodySize(),
                          doc41.BodySize(), doc81.BodySize());

        System.out.printf("doc40(%s)\n", doc40.Render(doc40.GetRoot()));
        recur_show4("doc40:", doc40, doc40.GetRoot());
        System.out.printf("doc80(%s)\n", doc80.Render(doc80.GetRoot()));
        recur_show8("doc80:", doc80, doc80.GetRoot());
        System.out.printf("doc41(%s)\n", doc41.Render(doc41.GetRoot()));
        recur_show4("doc41:", doc41, doc41.GetRoot());
        System.out.printf("doc81(%s)\n", doc81.Render(doc81.GetRoot()));
        recur_show8("doc81:", doc81, doc81.GetRoot());

        RapidDocument doc42 = doc41.Unfreeze(doc41.GetRoot());
        RapidDocument doc82 = doc81.Unfreeze(doc81.GetRoot());
        System.out.printf("doc42(%s)\n", doc42.Render(doc42.GetRoot()));
        recur_showr("doc42:", doc42, doc42.GetRoot());
        System.out.printf("doc82(%s)\n", doc82.Render(doc82.GetRoot()));
        recur_showr("doc82:", doc82, doc82.GetRoot());
    }
    public static void recur_show4(String indent, FreezeDocument4 doc, long pos)
    {
        if (doc.IsRemoved(pos)) System.out.printf("%sremoved\n", indent);
        if (doc.IsNull(pos)) System.out.printf("%snull\n", indent);
        else if (doc.IsFalse(pos)) System.out.printf("%sfalse\n", indent);
        else if (doc.IsTrue(pos)) System.out.printf("%strue\n", indent);
        else if (doc.IsInt(pos)) System.out.printf("%s%d\n", indent, doc.GetInt(pos));
        else if (doc.IsUint(pos)) System.out.printf("%s%d\n", indent, doc.GetUint(pos));
        else if (doc.IsDouble(pos)) System.out.printf("%s%f\n", indent, doc.GetDouble(pos));
        else if (doc.IsString(pos)) System.out.printf("%s%s\n", indent, doc.GetString(pos));
        else if (doc.IsArray(pos)) {
            System.out.printf("%s[\n", indent);
            for (long idx = 0; idx < doc.GetArraySpace(pos); ++idx)
                recur_show4(indent + "    ", doc, doc.GetArray(pos, idx));
            System.out.printf("%s]\n", indent);
        } else if (doc.IsObject(pos)) {
            System.out.printf("%s{\n", indent);
            for (long idx = 0; idx < doc.GetObjectSpace(pos); ++idx) {
                System.out.printf("%s    \"%s\":\n", indent, doc.GetObjectKey(pos, idx));
                recur_show4(indent + "   ", doc, doc.GetObject(pos, idx));
            }
            System.out.printf("%s}\n", indent);
        }
    }
    public static void recur_show8(String indent, FreezeDocument8 doc, long pos)
    {
        if (doc.IsRemoved(pos)) System.out.printf("%sremoved\n", indent);
        if (doc.IsNull(pos)) System.out.printf("%snull\n", indent);
        else if (doc.IsFalse(pos)) System.out.printf("%sfalse\n", indent);
        else if (doc.IsTrue(pos)) System.out.printf("%strue\n", indent);
        else if (doc.IsInt(pos)) System.out.printf("%s%d\n", indent, doc.GetInt(pos));
        else if (doc.IsUint(pos)) System.out.printf("%s%d\n", indent, doc.GetUint(pos));
        else if (doc.IsDouble(pos)) System.out.printf("%s%f\n", indent, doc.GetDouble(pos));
        else if (doc.IsString(pos)) System.out.printf("%s%s\n", indent, doc.GetString(pos));
        else if (doc.IsArray(pos)) {
            System.out.printf("%s[\n", indent);
            for (long idx = 0; idx < doc.GetArraySpace(pos); ++idx)
                recur_show8(indent + "    ", doc, doc.GetArray(pos, idx));
            System.out.printf("%s]\n", indent);
        } else if (doc.IsObject(pos)) {
            System.out.printf("%s{\n", indent);
            for (long idx = 0; idx < doc.GetObjectSpace(pos); ++idx) {
                System.out.printf("%s    \"%s\":\n", indent, doc.GetObjectKey(pos, idx));
                recur_show8(indent + "   ", doc, doc.GetObject(pos, idx));
            }
            System.out.printf("%s}\n", indent);
        }
    }
    public static void recur_showr(String indent, RapidDocument doc, long pos)
    {
        if (doc.IsRemoved(pos)) System.out.printf("%sremoved\n", indent);
        if (doc.IsNull(pos)) System.out.printf("%snull\n", indent);
        else if (doc.IsFalse(pos)) System.out.printf("%sfalse\n", indent);
        else if (doc.IsTrue(pos)) System.out.printf("%strue\n", indent);
        else if (doc.IsInt(pos)) System.out.printf("%s%d\n", indent, doc.GetInt(pos));
        else if (doc.IsUint(pos)) System.out.printf("%s%d\n", indent, doc.GetUint(pos));
        else if (doc.IsDouble(pos)) System.out.printf("%s%f\n", indent, doc.GetDouble(pos));
        else if (doc.IsString(pos)) System.out.printf("%s%s\n", indent, doc.GetString(pos));
        else if (doc.IsArray(pos)) {
            System.out.printf("%s[\n", indent);
            for (long idx = 0; idx < doc.GetArraySpace(pos); ++idx)
                recur_showr(indent + "    ", doc, doc.GetArray(pos, idx));
            System.out.printf("%s]\n", indent);
        } else if (doc.IsObject(pos)) {
            System.out.printf("%s{\n", indent);
            for (long idx = 0; idx < doc.GetObjectSpace(pos); ++idx) {
                System.out.printf("%s    \"%s\":\n", indent, doc.GetObjectKey(pos, idx));
                recur_showr(indent + "   ", doc, doc.GetObject(pos, idx));
            }
            System.out.printf("%s}\n", indent);
        }
    }
}
