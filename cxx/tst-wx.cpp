#include <wx/wx.h>
#include <wx/dc.h>
#include <wx/dcbuffer.h>
#include <wx/graphics.h>
#include <wx/frame.h>
#include <wx/app.h>

static const size_t cross_size = 8;
static const size_t diamond_size0 = 16;
static const size_t diamond_size1 = 32;
class TstLayer_t {
public:
    TstLayer_t(wxWindow *window, const wxPen *pen);
    ~TstLayer_t();

    void setSize(const wxSize &sz);
    void paint_grid(void);
    void paint_0(void);
    void paint_1(void);
    void paint_left(wxCoord cx, wxCoord cy);
    void paint_right(wxCoord cx, wxCoord cy);
    void paint_cursor(wxCoord cx, wxCoord cy);

    wxBitmap *mSurface;
    wxMemoryDC *mDC;
private:
    wxWindow *_window;
    const wxPen *_pen;
    void _updateDC(void);
    void _drawbegin(void);
    void _drawend(void);
};
TstLayer_t::TstLayer_t(wxWindow *window, const wxPen *pen)
{
    _window = window;
    _pen = pen;
    mSurface = new wxBitmap(window->GetClientSize());
    mDC = NULL;
    _updateDC();
    mDC->Clear();
}
TstLayer_t::~TstLayer_t()
{
    delete mSurface;
}

void
TstLayer_t::setSize(const wxSize &sz)
{
    if (sz == mDC->GetSize()) return;
    mSurface->SetWidth(sz.GetWidth());
    mSurface->SetHeight(sz.GetHeight());
    _updateDC();
}

void
TstLayer_t::paint_grid(void)
{
    wxCoord px, py;
    wxSize sz;

    _drawbegin();
    sz = mDC->GetSize();
    for (px = 32; px < sz.GetWidth(); px += 32)
        mDC->DrawLine(px, 0, px, sz.GetHeight());
    for (py = 32; py < sz.GetHeight(); py += 32)
        mDC->DrawLine(0, py, sz.GetWidth(), py);
    _drawend();
}
void
TstLayer_t::paint_0(void)
{
    wxCoord px, py;
    wxSize sz;

    _drawbegin();
    sz = mDC->GetSize();
    for (px = 64; px < sz.GetWidth(); px += 64)
        for (py = 64; py < sz.GetHeight(); py += 64) {
            mDC->DrawLine(px - cross_size, py - cross_size,
                          px + cross_size, py + cross_size);
            mDC->DrawLine(px - cross_size, py + cross_size,
                          px + cross_size, py - cross_size);
        }
    _drawend();
}
void
TstLayer_t::paint_1(void)
{
    wxCoord px, py;
    wxSize sz;

    _drawbegin();
    sz = mDC->GetSize();
    for (px = 32; px < sz.GetWidth(); px += 64)
        for (py = 32; py < sz.GetHeight(); py += 64) {
            mDC->DrawLine(px - cross_size, py - cross_size,
                          px + cross_size, py + cross_size);
            mDC->DrawLine(px - cross_size, py + cross_size,
                          px + cross_size, py - cross_size);
        }
    _drawend();
}
void
TstLayer_t::paint_left(wxCoord cx, wxCoord cy)
{
    wxPoint points[4];

    _drawbegin();
    points[0] = wxPoint(cx, cy - diamond_size0);
    points[1] = wxPoint(cx + diamond_size1, cy);
    points[2] = wxPoint(cx, cy + diamond_size0);
    points[3] = wxPoint(cx - diamond_size1, cy);
    mDC->DrawPolygon(4, points);
    _drawend();
}
void
TstLayer_t::paint_right(wxCoord cx, wxCoord cy)
{
    wxPoint points[4];

    _drawbegin();
    points[0] = wxPoint(cx, cy - diamond_size1);
    points[1] = wxPoint(cx + diamond_size0, cy);
    points[2] = wxPoint(cx, cy + diamond_size1);
    points[3] = wxPoint(cx - diamond_size0, cy);
    mDC->DrawPolygon(4, points);
    _drawend();
}
void
TstLayer_t::paint_cursor(wxCoord cx, wxCoord cy)
{
    wxSize sz;

    _drawbegin();
    sz = mDC->GetSize();
    mDC->Clear();
    mDC->DrawLine(cx, 0, cx, sz.GetHeight());
    mDC->DrawLine(0, cy, sz.GetWidth(), cy);
    _drawend();
}
void
TstLayer_t::_updateDC(void)
{
    if (mDC) delete mDC;
    mDC = new wxMemoryDC(*mSurface);
    mDC->SetBackground(*wxBLACK_BRUSH);
    mDC->SetPen(*_pen);
}
void
TstLayer_t::_drawbegin(void)
{
}
void
TstLayer_t::_drawend(void)
{
}

class TstCanvas_t: public wxWindow {
    wxDECLARE_EVENT_TABLE();
public:
    TstCanvas_t(wxFrame *parent);
    ~TstCanvas_t();

    void OnSize(wxSizeEvent &event);
    void OnPaint(wxPaintEvent &event);
    void OnMouseMove(wxMouseEvent &event);
    void OnMouseLeftDown(wxMouseEvent &event);
    void OnMouseRightDown(wxMouseEvent &event);
    void OnMouseEnter(wxMouseEvent &event);
    void OnMouseLeave(wxMouseEvent &event);
private:
    TstLayer_t *_layers[6];
};

wxBEGIN_EVENT_TABLE(TstCanvas_t, wxWindow)
EVT_SIZE(TstCanvas_t::OnSize)
EVT_PAINT(TstCanvas_t::OnPaint)
EVT_MOTION(TstCanvas_t::OnMouseMove)
EVT_LEFT_DOWN(TstCanvas_t::OnMouseLeftDown)
EVT_RIGHT_DOWN(TstCanvas_t::OnMouseRightDown)
EVT_ENTER_WINDOW(TstCanvas_t::OnMouseEnter)
EVT_LEAVE_WINDOW(TstCanvas_t::OnMouseLeave)
wxEND_EVENT_TABLE()

TstCanvas_t::TstCanvas_t(wxFrame *parent): wxWindow(parent, wxID_ANY)
{
    fprintf(stderr, "TstCanvas_t()\n");
    SetBackgroundColour(*wxBLACK);
    for (unsigned idx = 0; idx < sizeof(_layers) / sizeof(_layers[0]); ++idx)
        _layers[idx] = NULL;
}
TstCanvas_t::~TstCanvas_t()
{
    fprintf(stderr, "~TstCanvas_t()\n");
    for (unsigned idx = 0; idx < sizeof(_layers) / sizeof(_layers[0]); ++idx)
        if (_layers[idx]) delete _layers[idx];
}

void
TstCanvas_t::OnSize(wxSizeEvent &event)
{
    fprintf(stderr, "OnSize(%u, %u)\n",
            event.GetSize().GetWidth(), event.GetSize().GetHeight());
    for (unsigned idx = 0; idx < sizeof(_layers) / sizeof(_layers[0]); ++idx)
        if (_layers[idx]) _layers[idx]->setSize(event.GetSize());
}

void
TstCanvas_t::OnPaint(wxPaintEvent &event)
{
    wxPaintDC dc(this);
    wxSize sz(GetClientSize());
    //wxGraphicsContext *gc = wxGraphicsContext::Create(dc);

    dc.SetPen(*wxBLUE_PEN);
    dc.DrawLine(0, 0, sz.GetWidth(), sz.GetHeight());
    dc.DrawLine(0, sz.GetHeight(), sz.GetWidth(), 0);

    if (_layers[0] == NULL) {
        _layers[0] = new TstLayer_t(this, wxRED_PEN);
        _layers[0]->paint_grid();
    }
    if (_layers[1] == NULL) {
        _layers[1] = new TstLayer_t(this, wxBLUE_PEN);
        _layers[1]->paint_0();
    }
    if (_layers[2] == NULL) {
        _layers[2] = new TstLayer_t(this, wxGREEN_PEN);
        _layers[2]->paint_1();
    }
    if (_layers[3] == NULL) _layers[3] = new TstLayer_t(this, wxYELLOW_PEN);
    if (_layers[4] == NULL) _layers[4] = new TstLayer_t(this, wxCYAN_PEN);
    if (_layers[5] == NULL) _layers[5] = new TstLayer_t(this, wxWHITE_PEN);
    for (unsigned idx = 0; idx < sizeof(_layers) / sizeof(_layers[0]); ++idx)
        dc.Blit(0, 0, sz.GetWidth(), sz.GetHeight(),
                _layers[idx]->mDC, 0, 0, wxOR);
}
void
TstCanvas_t::OnMouseMove(wxMouseEvent &event)
{
    //fprintf(stderr, "OnMouseMove(%u, %u)\n",
    //(unsigned)event.GetX(), (unsigned)event.GetY());
    if (_layers[5]) {
        _layers[5]->paint_cursor(event.GetX(), event.GetY());
        Refresh();
        Update();
    }
}
void
TstCanvas_t::OnMouseLeftDown(wxMouseEvent &event)
{
    fprintf(stderr, "OnMouseLeftDown(%u, %u)\n",
            (unsigned)event.GetX(), (unsigned)event.GetY());
    if (_layers[3]) {
        _layers[3]->paint_left(event.GetX(), event.GetY());
        Refresh();
        Update();
    }
}
void
TstCanvas_t::OnMouseRightDown(wxMouseEvent &event)
{
    fprintf(stderr, "OnMouseRightDown(%u, %u)\n",
            (unsigned)event.GetX(), (unsigned)event.GetY());
    if (_layers[4]) {
        _layers[4]->paint_right(event.GetX(), event.GetY());
        Refresh();
        Update();
    }
}
void
TstCanvas_t::OnMouseEnter(wxMouseEvent &event)
{
    fprintf(stderr, "OnMouseEnter(%u, %u)\n",
            (unsigned)event.GetX(), (unsigned)event.GetY());
    if (_layers[5]) {
        _layers[5]->paint_cursor(event.GetX(), event.GetY());
        Refresh();
        Update();
    }
}
void
TstCanvas_t::OnMouseLeave(wxMouseEvent &event)
{
    fprintf(stderr, "OnMouseLeave(%u, %u)\n",
            (unsigned)event.GetX(), (unsigned)event.GetY());
    if (_layers[5]) {
        _layers[5]->mDC->Clear();
        Refresh();
        Update();
    }
}

class TstFrame_t: public wxFrame {
public:
    TstFrame_t(wxWindow *window = NULL):
        wxFrame(window, wxID_ANY, "TstFrame_t")
    { _canvas = new TstCanvas_t(this); }
private:
    TstCanvas_t *_canvas;
};

class TstApp_t: public wxApp {
public:
    TstApp_t(void);
    virtual ~TstApp_t();
    virtual bool OnInit(void);
    virtual int OnExit(void);
};

IMPLEMENT_APP(TstApp_t);

TstApp_t::TstApp_t(void)
{
    fprintf(stderr, "TstApp_t()\n");
}

bool
TstApp_t::OnInit(void)
{
    TstFrame_t *_frame;
    if (!wxApp::OnInit()) return false;
    wxInitAllImageHandlers();
    _frame = new TstFrame_t();
    SetTopWindow(_frame);
    _frame->Show(true);
    fprintf(stderr, "OnInit()\n");
    return true;
}

int
TstApp_t::OnExit(void)
{
    fprintf(stderr, "OnExit()\n");
    return wxApp::OnExit();
}

TstApp_t::~TstApp_t()
{
    fprintf(stderr, "~TstApp_t()\n");
}
