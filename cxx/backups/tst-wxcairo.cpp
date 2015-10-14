#include <cairo.h>
#include <wx/wx.h>
#include <wx/graphics.h>
#include <wx/frame.h>
#include <wx/app.h>

#define NLAYERS 6
static const size_t cross_size = 8;
static const size_t diamond_size0 = 16;
static const size_t diamond_size1 = 32;

class TstLayer_t {
public:
    TstLayer_t(void) { sr = NULL; }
    ~TstLayer_t() { if (sr) cairo_surface_destroy(sr); }

    void make_surface(cairo_t *cr, const wxSize &sz);
    void set_size(const wxSize &sz);
    void clear(void);
    void paint_grid(void);
    void paint_cross0(void);
    void paint_cross1(void);
    void paint_left(wxCoord cx, wxCoord cy);
    void paint_right(wxCoord cx, wxCoord cy);
    void paint_cursor(wxCoord cx, wxCoord cy);
    cairo_surface_t *sr;
    wxCoord width, height;
};

void
TstLayer_t::make_surface(cairo_t *cr, const wxSize &sz)
{
    cairo_surface_t *crsr = cairo_get_target(cr);
    width = sz.GetWidth();
    height = sz.GetHeight();
    sr = cairo_surface_create_similar(crsr, CAIRO_CONTENT_COLOR_ALPHA,
                                      width, height);
    clear();
}
void
TstLayer_t::set_size(const wxSize &sz)
{
    cairo_surface_t *nsr;
    if (sr == NULL) return;
    if (width == sz.GetWidth() && height == sz.GetHeight()) return;
    width = sz.GetWidth(); height = sz.GetHeight();
    nsr = cairo_surface_create_similar(sr, CAIRO_CONTENT_COLOR_ALPHA,
                                       width, height);
    cairo_surface_destroy(sr);
    sr = nsr;
    clear();
}
void
TstLayer_t::clear(void)
{
    cairo_t *cr = cairo_create(sr);

    cairo_set_operator(cr, CAIRO_OPERATOR_CLEAR);
    cairo_rectangle(cr, 0, 0, width, height);
    cairo_fill(cr);
    cairo_destroy(cr);
}
void
TstLayer_t::paint_grid(void)
{
    wxCoord cur;
    cairo_t *cr = cairo_create(sr);

    cairo_set_antialias(cr, CAIRO_ANTIALIAS_NONE);
    cairo_set_source_rgb(cr, 0.5, 0, 0);
    cairo_set_line_width(cr, 1);
    for (cur = 32; cur < width; cur += 32) {
        cairo_move_to(cr, cur, 0);
        cairo_line_to(cr, cur, height);
    }
    for (cur = 32; cur < height; cur += 32) {
        cairo_move_to(cr, 0, cur);
        cairo_line_to(cr, width, cur);
    }
    cairo_stroke(cr);
    cairo_destroy(cr);
}
void
TstLayer_t::paint_cross0(void)
{
    wxCoord px, py;
    cairo_t *cr = cairo_create(sr);

    cairo_set_antialias(cr, CAIRO_ANTIALIAS_NONE);
    cairo_set_source_rgb(cr, 0, 0.5, 0);
    cairo_set_line_width(cr, 1);
    for (px = 64; px < width; px += 64)
        for (py = 64; py < height; py += 64) {
            cairo_move_to(cr, px - cross_size, py - cross_size);
            cairo_line_to(cr, px + cross_size, py + cross_size);
            cairo_move_to(cr, px - cross_size, py + cross_size);
            cairo_line_to(cr, px + cross_size, py - cross_size);
        }
    cairo_stroke(cr);
    cairo_destroy(cr);
}
void
TstLayer_t::paint_cross1(void)
{
    wxCoord px, py;
    cairo_t *cr = cairo_create(sr);

    cairo_set_antialias(cr, CAIRO_ANTIALIAS_NONE);
    cairo_set_source_rgb(cr, 0, 0, 0.5);
    cairo_set_line_width(cr, 1);
    for (px = 32; px < width; px += 64)
        for (py = 32; py < height; py += 64) {
            cairo_move_to(cr, px - cross_size, py - cross_size);
            cairo_line_to(cr, px + cross_size, py + cross_size);
            cairo_move_to(cr, px - cross_size, py + cross_size);
            cairo_line_to(cr, px + cross_size, py - cross_size);
        }
    cairo_stroke(cr);
    cairo_destroy(cr);
}
void
TstLayer_t::paint_left(wxCoord cx, wxCoord cy)
{
    cairo_t *cr = cairo_create(sr);

    cairo_set_antialias(cr, CAIRO_ANTIALIAS_NONE);
    cairo_set_source_rgb(cr, 0, 1, 0);
    cairo_set_line_width(cr, 1);
    cairo_move_to(cr, cx, cy - diamond_size0);
    cairo_line_to(cr, cx + diamond_size1, cy);
    cairo_line_to(cr, cx, cy + diamond_size0);
    cairo_line_to(cr, cx - diamond_size1, cy);
    cairo_line_to(cr, cx, cy - diamond_size0);
    cairo_stroke(cr);
    cairo_destroy(cr);
}
void
TstLayer_t::paint_right(wxCoord cx, wxCoord cy)
{
    cairo_t *cr = cairo_create(sr);

    cairo_set_antialias(cr, CAIRO_ANTIALIAS_NONE);
    cairo_set_source_rgb(cr, 0, 0, 1);
    cairo_set_line_width(cr, 1);
    cairo_move_to(cr, cx, cy - diamond_size1);
    cairo_line_to(cr, cx + diamond_size0, cy);
    cairo_line_to(cr, cx, cy + diamond_size1);
    cairo_line_to(cr, cx - diamond_size0, cy);
    cairo_line_to(cr, cx, cy - diamond_size1);
    cairo_stroke(cr);
    cairo_destroy(cr);
}
void
TstLayer_t::paint_cursor(wxCoord cx, wxCoord cy)
{
    cairo_t *cr = cairo_create(sr);

    cairo_set_antialias(cr, CAIRO_ANTIALIAS_NONE);
    cairo_set_source_rgb(cr, 0, 1, 1);
    cairo_set_line_width(cr, 1);
    cairo_move_to(cr, cx, 0);
    cairo_line_to(cr, cx, height);
    cairo_move_to(cr, 0, cy);
    cairo_line_to(cr, width, cy);
    cairo_stroke(cr);
    cairo_destroy(cr);
}

class TstCanvas_t: public wxWindow {
    wxDECLARE_EVENT_TABLE();
public:
    TstCanvas_t(wxFrame *parent);
    ~TstCanvas_t();

    void OnSize(wxSizeEvent &ev);
    void OnPaint(wxPaintEvent &ev);
    void OnMouseMove(wxMouseEvent &ev);
    void OnMouseLeftDown(wxMouseEvent &ev);
    void OnMouseRightDown(wxMouseEvent &ev);
    void OnMouseEnter(wxMouseEvent &ev);
    void OnMouseLeave(wxMouseEvent &ev);
private:
    TstLayer_t *_layers[NLAYERS];
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
    for (unsigned idx = 0; idx < NLAYERS; ++idx)
        _layers[idx] = new TstLayer_t();
}
TstCanvas_t::~TstCanvas_t()
{
    fprintf(stderr, "~TstCanvas_t()\n");
    for (unsigned idx = 0; idx < NLAYERS; ++idx) delete _layers[idx];
}
void
TstCanvas_t::OnSize(wxSizeEvent &ev)
{
    fprintf(stderr, "OnSize(%u, %u)\n",
            ev.GetSize().GetWidth(), ev.GetSize().GetHeight());
    for (unsigned idx = 0; idx < NLAYERS; ++idx)
        _layers[idx]->set_size(ev.GetSize());
}
void
TstCanvas_t::OnPaint(wxPaintEvent &ev)
{
    wxSize sz(GetClientSize());
    wxPaintDC dc(this);
    wxGraphicsContext *gc = wxGraphicsContext::Create(dc);
    cairo_t *cr = (cairo_t *)gc->GetNativeContext();

    if (!_layers[0]->sr) {
        _layers[0]->make_surface(cr, sz);
        _layers[0]->paint_grid();
    }
    if (!_layers[1]->sr) {
        _layers[1]->make_surface(cr, sz);
        _layers[1]->paint_cross0();
    }
    if (!_layers[2]->sr) {
        _layers[2]->make_surface(cr, sz);
        _layers[2]->paint_cross1();
    }
    if (!_layers[3]->sr) _layers[3]->make_surface(cr, sz);
    if (!_layers[4]->sr) _layers[4]->make_surface(cr, sz);
    if (!_layers[5]->sr) _layers[5]->make_surface(cr, sz);
    for (unsigned idx = 0; idx < 6; ++idx) {
        cairo_set_source_surface(cr, _layers[idx]->sr, 0, 0);
        cairo_paint(cr);
    }
    delete gc;
}
void
TstCanvas_t::OnMouseMove(wxMouseEvent &ev)
{
    //fprintf(stderr, "OnMouseMove(%u, %u)\n",
    //(unsigned)ev.GetX(), (unsigned)ev.GetY());
    if (_layers[5]) {
        _layers[5]->clear();
        _layers[5]->paint_cursor(ev.GetX(), ev.GetY());
        Refresh();
        Update();
    }
}
void
TstCanvas_t::OnMouseLeftDown(wxMouseEvent &ev)
{
    fprintf(stderr, "OnMouseLeftDown(%u, %u)\n",
            (unsigned)ev.GetX(), (unsigned)ev.GetY());
    if (_layers[3]) {
        _layers[3]->paint_left(ev.GetX(), ev.GetY());
        Refresh();
        Update();
    }
}
void
TstCanvas_t::OnMouseRightDown(wxMouseEvent &ev)
{
    fprintf(stderr, "OnMouseRightDown(%u, %u)\n",
            (unsigned)ev.GetX(), (unsigned)ev.GetY());
    if (_layers[4]) {
        _layers[4]->paint_right(ev.GetX(), ev.GetY());
        Refresh();
        Update();
    }
}
void
TstCanvas_t::OnMouseEnter(wxMouseEvent &ev)
{
    fprintf(stderr, "OnMouseEnter(%u, %u)\n",
            (unsigned)ev.GetX(), (unsigned)ev.GetY());
    if (_layers[5]) {
        _layers[5]->paint_cursor(ev.GetX(), ev.GetY());
        Refresh();
        Update();
    }
}
void
TstCanvas_t::OnMouseLeave(wxMouseEvent &ev)
{
    fprintf(stderr, "OnMouseLeave(%u, %u)\n",
            (unsigned)ev.GetX(), (unsigned)ev.GetY());
    if (_layers[5]) {
        _layers[5]->clear();
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
