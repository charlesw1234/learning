#include <QDir>

int
main(void)
{
    QDir dobj(".");
    foreach (QString entry,
             dobj.entryList(QStringList("*.cpp"), QDir::Files, QDir::Name))
        printf("%s\n", entry.toUtf8().constData());
    return 0;
}
