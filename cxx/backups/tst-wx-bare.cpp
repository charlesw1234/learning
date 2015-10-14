#include <wx/wx.h>
#include <wx/app.h>

class TstFrame_t: public wxFrame {
public:
    TstFrame_t(wxWindow *window = NULL):
        wxFrame(window, wxID_ANY, "TstFrame_t")
    {}
};
class TstApp_t: public wxApp {
    virtual bool OnInit(void);
    virtual int OnExit(void);
private:
    TstFrame_t *_frame;
};
IMPLEMENT_APP(TstApp_t);

bool
TstApp_t::OnInit(void)
{
    if (!wxApp::OnInit()) return false;
    wxInitAllImageHandlers();
    _frame = new TstFrame_t();
    SetTopWindow(_frame);
    _frame->Show(true);
    return true;
}
int
TstApp_t::OnExit(void)
{
    //delete _frame;
    return wxApp::OnExit();
}
