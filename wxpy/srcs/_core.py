# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.

import __core
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


#//----------------------------------------------------------------------------
#// These will be reset when the _wxPySetDictionary is called.  Dummy
#// values are set here for tools that do static source analysis.
Platform = ""
PlatformInfo = ()

#// Give a reference to the dictionary of this module to the C++ extension
#// code.
_core_._wxPySetDictionary(vars())

#// A little trick to make 'wx' be a reference to this module so wx.Names can
#// be used here.
import sys as _sys
wx = _sys.modules[__name__]


#----------------------------------------------------------------------------
            
import warnings
class wxPyDeprecationWarning(DeprecationWarning):
    pass
warnings.simplefilter('default', wxPyDeprecationWarning)
del warnings

def deprecated(item, msg=''):
    """
    Create a delegating wrapper that raises a deprecation warning.  Can be
    used with callable objects (functions, methods, classes) or with
    properties.
    """
    import warnings
    if isinstance(item, type):
        # It is a class.  Make a subclass that raises a warning.
        class DeprecatedClassProxy(item):
            def __init__(*args, **kw):
                warnings.warn("Using deprecated class %s. %s" % (item.__name__, msg),
                          wxPyDeprecationWarning, stacklevel=2)
                item.__init__(*args, **kw)
        DeprecatedClassProxy.__name__ = item.__name__
        return DeprecatedClassProxy
    
    elif callable(item):
        # wrap a new function around the callable
        def deprecated_func(*args, **kw):
            warnings.warn("Call to deprecated item. %s" %  msg,
                          wxPyDeprecationWarning, stacklevel=2)
            return item(*args, **kw)
        deprecated_func.__name__ = item.__name__
        deprecated_func.__doc__ = item.__doc__
        if hasattr(item, '__dict__'):
            deprecated_func.__dict__.update(item.__dict__)
        return deprecated_func
        
    elif hasattr(item, '__get__'):
        # it should be a property if there is a getter
        class DepGetProp(object):
            def __init__(self,item, msg):
                self.item = item
                self.msg = msg
            def __get__(self, inst, klass):
                warnings.warn("Accessing deprecated property. %s" % msg,
                              wxPyDeprecationWarning, stacklevel=2)
                return self.item.__get__(inst, klass)
        class DepGetSetProp(DepGetProp):
            def __set__(self, inst, val):
                warnings.warn("Accessing deprecated property. %s" % msg,
                              wxPyDeprecationWarning, stacklevel=2)
                return self.item.__set__(inst, val)
        class DepGetSetDelProp(DepGetSetProp):
            def __delete__(self, inst):
                warnings.warn("Accessing deprecated property. %s" % msg,
                              wxPyDeprecationWarning, stacklevel=2)
                return self.item.__delete__(inst)
        
        if hasattr(item, '__set__') and hasattr(item, '__delete__'):
            return DepGetSetDelProp(item, msg)
        elif hasattr(item, '__set__'):
            return DepGetSetProp(item, msg)
        else:
            return DepGetProp(item, msg)
    else:
        raise TypeError, "unsupported type %s" % type(item)
                   
         
                   
#----------------------------------------------------------------------------

DefaultCoord = __core.DefaultCoord
NOT_FOUND = __core.NOT_FOUND
NO_LEN = __core.NO_LEN
VSCROLL = __core.VSCROLL
HSCROLL = __core.HSCROLL
CAPTION = __core.CAPTION
DOUBLE_BORDER = __core.DOUBLE_BORDER
SUNKEN_BORDER = __core.SUNKEN_BORDER
RAISED_BORDER = __core.RAISED_BORDER
BORDER = __core.BORDER
SIMPLE_BORDER = __core.SIMPLE_BORDER
STATIC_BORDER = __core.STATIC_BORDER
TRANSPARENT_WINDOW = __core.TRANSPARENT_WINDOW
NO_BORDER = __core.NO_BORDER
DEFAULT_CONTROL_BORDER = __core.DEFAULT_CONTROL_BORDER
DEFAULT_STATUSBAR_STYLE = __core.DEFAULT_STATUSBAR_STYLE
TAB_TRAVERSAL = __core.TAB_TRAVERSAL
WANTS_CHARS = __core.WANTS_CHARS
POPUP_WINDOW = __core.POPUP_WINDOW
CENTER_FRAME = __core.CENTER_FRAME
CENTRE_ON_SCREEN = __core.CENTRE_ON_SCREEN
CENTER_ON_SCREEN = __core.CENTER_ON_SCREEN
CLIP_CHILDREN = __core.CLIP_CHILDREN
CLIP_SIBLINGS = __core.CLIP_SIBLINGS
WINDOW_STYLE_MASK = __core.WINDOW_STYLE_MASK
ALWAYS_SHOW_SB = __core.ALWAYS_SHOW_SB
RETAINED = __core.RETAINED
BACKINGSTORE = __core.BACKINGSTORE
COLOURED = __core.COLOURED
FIXED_LENGTH = __core.FIXED_LENGTH
LB_NEEDED_SB = __core.LB_NEEDED_SB
LB_ALWAYS_SB = __core.LB_ALWAYS_SB
LB_SORT = __core.LB_SORT
LB_SINGLE = __core.LB_SINGLE
LB_MULTIPLE = __core.LB_MULTIPLE
LB_EXTENDED = __core.LB_EXTENDED
LB_OWNERDRAW = __core.LB_OWNERDRAW
LB_HSCROLL = __core.LB_HSCROLL
CB_SIMPLE = __core.CB_SIMPLE
CB_DROPDOWN = __core.CB_DROPDOWN
CB_SORT = __core.CB_SORT
CB_READONLY = __core.CB_READONLY
RA_HORIZONTAL = __core.RA_HORIZONTAL
RA_VERTICAL = __core.RA_VERTICAL
RA_SPECIFY_ROWS = __core.RA_SPECIFY_ROWS
RA_SPECIFY_COLS = __core.RA_SPECIFY_COLS
RB_GROUP = __core.RB_GROUP
RB_SINGLE = __core.RB_SINGLE
SB_HORIZONTAL = __core.SB_HORIZONTAL
SB_VERTICAL = __core.SB_VERTICAL
TOOL_TOP = __core.TOOL_TOP
TOOL_BOTTOM = __core.TOOL_BOTTOM
TOOL_LEFT = __core.TOOL_LEFT
TOOL_RIGHT = __core.TOOL_RIGHT
OK = __core.OK
YES_NO = __core.YES_NO
CANCEL = __core.CANCEL
YES = __core.YES
NO = __core.NO
NO_DEFAULT = __core.NO_DEFAULT
YES_DEFAULT = __core.YES_DEFAULT
OK_DEFAULT = __core.OK_DEFAULT
CANCEL_DEFAULT = __core.CANCEL_DEFAULT
APPLY = __core.APPLY
CLOSE = __core.CLOSE
ICON_EXCLAMATION = __core.ICON_EXCLAMATION
ICON_HAND = __core.ICON_HAND
ICON_QUESTION = __core.ICON_QUESTION
ICON_INFORMATION = __core.ICON_INFORMATION
ICON_STOP = __core.ICON_STOP
ICON_ASTERISK = __core.ICON_ASTERISK
ICON_MASK = __core.ICON_MASK
ICON_WARNING = __core.ICON_WARNING
ICON_ERROR = __core.ICON_ERROR
ICON_NONE = __core.ICON_NONE
FORWARD = __core.FORWARD
BACKWARD = __core.BACKWARD
RESET = __core.RESET
HELP = __core.HELP
MORE = __core.MORE
SETUP = __core.SETUP
SIZE_AUTO_WIDTH = __core.SIZE_AUTO_WIDTH
SIZE_AUTO_HEIGHT = __core.SIZE_AUTO_HEIGHT
SIZE_AUTO = __core.SIZE_AUTO
SIZE_USE_EXISTING = __core.SIZE_USE_EXISTING
SIZE_ALLOW_MINUS_ONE = __core.SIZE_ALLOW_MINUS_ONE
SIZE_FORCE = __core.SIZE_FORCE
SIZE_FORCE_EVENT = __core.SIZE_FORCE_EVENT
PRINT_QUALITY_HIGH = __core.PRINT_QUALITY_HIGH
PRINT_QUALITY_MEDIUM = __core.PRINT_QUALITY_MEDIUM
PRINT_QUALITY_LOW = __core.PRINT_QUALITY_LOW
PRINT_QUALITY_DRAFT = __core.PRINT_QUALITY_DRAFT
ID_AUTO_LOWEST = __core.ID_AUTO_LOWEST
ID_AUTO_HIGHEST = __core.ID_AUTO_HIGHEST
ID_ANY = __core.ID_ANY
ID_SEPARATOR = __core.ID_SEPARATOR
ID_NONE = __core.ID_NONE
ID_LOWEST = __core.ID_LOWEST
ID_OPEN = __core.ID_OPEN
ID_CLOSE = __core.ID_CLOSE
ID_NEW = __core.ID_NEW
ID_SAVE = __core.ID_SAVE
ID_SAVEAS = __core.ID_SAVEAS
ID_REVERT = __core.ID_REVERT
ID_EXIT = __core.ID_EXIT
ID_UNDO = __core.ID_UNDO
ID_REDO = __core.ID_REDO
ID_HELP = __core.ID_HELP
ID_PRINT = __core.ID_PRINT
ID_PRINT_SETUP = __core.ID_PRINT_SETUP
ID_PAGE_SETUP = __core.ID_PAGE_SETUP
ID_PREVIEW = __core.ID_PREVIEW
ID_ABOUT = __core.ID_ABOUT
ID_HELP_CONTENTS = __core.ID_HELP_CONTENTS
ID_HELP_COMMANDS = __core.ID_HELP_COMMANDS
ID_HELP_PROCEDURES = __core.ID_HELP_PROCEDURES
ID_HELP_CONTEXT = __core.ID_HELP_CONTEXT
ID_HELP_INDEX = __core.ID_HELP_INDEX
ID_HELP_SEARCH = __core.ID_HELP_SEARCH
ID_CLOSE_ALL = __core.ID_CLOSE_ALL
ID_PREFERENCES = __core.ID_PREFERENCES
ID_EDIT = __core.ID_EDIT
ID_CUT = __core.ID_CUT
ID_COPY = __core.ID_COPY
ID_PASTE = __core.ID_PASTE
ID_CLEAR = __core.ID_CLEAR
ID_FIND = __core.ID_FIND
ID_DUPLICATE = __core.ID_DUPLICATE
ID_SELECTALL = __core.ID_SELECTALL
ID_DELETE = __core.ID_DELETE
ID_REPLACE = __core.ID_REPLACE
ID_REPLACE_ALL = __core.ID_REPLACE_ALL
ID_PROPERTIES = __core.ID_PROPERTIES
ID_VIEW_DETAILS = __core.ID_VIEW_DETAILS
ID_VIEW_LARGEICONS = __core.ID_VIEW_LARGEICONS
ID_VIEW_SMALLICONS = __core.ID_VIEW_SMALLICONS
ID_VIEW_LIST = __core.ID_VIEW_LIST
ID_VIEW_SORTDATE = __core.ID_VIEW_SORTDATE
ID_VIEW_SORTNAME = __core.ID_VIEW_SORTNAME
ID_VIEW_SORTSIZE = __core.ID_VIEW_SORTSIZE
ID_VIEW_SORTTYPE = __core.ID_VIEW_SORTTYPE
ID_FILE = __core.ID_FILE
ID_FILE1 = __core.ID_FILE1
ID_FILE2 = __core.ID_FILE2
ID_FILE3 = __core.ID_FILE3
ID_FILE4 = __core.ID_FILE4
ID_FILE5 = __core.ID_FILE5
ID_FILE6 = __core.ID_FILE6
ID_FILE7 = __core.ID_FILE7
ID_FILE8 = __core.ID_FILE8
ID_FILE9 = __core.ID_FILE9
ID_OK = __core.ID_OK
ID_CANCEL = __core.ID_CANCEL
ID_APPLY = __core.ID_APPLY
ID_YES = __core.ID_YES
ID_NO = __core.ID_NO
ID_STATIC = __core.ID_STATIC
ID_FORWARD = __core.ID_FORWARD
ID_BACKWARD = __core.ID_BACKWARD
ID_DEFAULT = __core.ID_DEFAULT
ID_MORE = __core.ID_MORE
ID_SETUP = __core.ID_SETUP
ID_RESET = __core.ID_RESET
ID_CONTEXT_HELP = __core.ID_CONTEXT_HELP
ID_YESTOALL = __core.ID_YESTOALL
ID_NOTOALL = __core.ID_NOTOALL
ID_ABORT = __core.ID_ABORT
ID_RETRY = __core.ID_RETRY
ID_IGNORE = __core.ID_IGNORE
ID_ADD = __core.ID_ADD
ID_REMOVE = __core.ID_REMOVE
ID_UP = __core.ID_UP
ID_DOWN = __core.ID_DOWN
ID_HOME = __core.ID_HOME
ID_REFRESH = __core.ID_REFRESH
ID_STOP = __core.ID_STOP
ID_INDEX = __core.ID_INDEX
ID_BOLD = __core.ID_BOLD
ID_ITALIC = __core.ID_ITALIC
ID_JUSTIFY_CENTER = __core.ID_JUSTIFY_CENTER
ID_JUSTIFY_FILL = __core.ID_JUSTIFY_FILL
ID_JUSTIFY_RIGHT = __core.ID_JUSTIFY_RIGHT
ID_JUSTIFY_LEFT = __core.ID_JUSTIFY_LEFT
ID_UNDERLINE = __core.ID_UNDERLINE
ID_INDENT = __core.ID_INDENT
ID_UNINDENT = __core.ID_UNINDENT
ID_ZOOM_100 = __core.ID_ZOOM_100
ID_ZOOM_FIT = __core.ID_ZOOM_FIT
ID_ZOOM_IN = __core.ID_ZOOM_IN
ID_ZOOM_OUT = __core.ID_ZOOM_OUT
ID_UNDELETE = __core.ID_UNDELETE
ID_REVERT_TO_SAVED = __core.ID_REVERT_TO_SAVED
ID_CDROM = __core.ID_CDROM
ID_CONVERT = __core.ID_CONVERT
ID_EXECUTE = __core.ID_EXECUTE
ID_FLOPPY = __core.ID_FLOPPY
ID_HARDDISK = __core.ID_HARDDISK
ID_BOTTOM = __core.ID_BOTTOM
ID_FIRST = __core.ID_FIRST
ID_LAST = __core.ID_LAST
ID_TOP = __core.ID_TOP
ID_INFO = __core.ID_INFO
ID_JUMP_TO = __core.ID_JUMP_TO
ID_NETWORK = __core.ID_NETWORK
ID_SELECT_COLOR = __core.ID_SELECT_COLOR
ID_SELECT_FONT = __core.ID_SELECT_FONT
ID_SORT_ASCENDING = __core.ID_SORT_ASCENDING
ID_SORT_DESCENDING = __core.ID_SORT_DESCENDING
ID_SPELL_CHECK = __core.ID_SPELL_CHECK
ID_STRIKETHROUGH = __core.ID_STRIKETHROUGH
ID_SYSTEM_MENU = __core.ID_SYSTEM_MENU
ID_CLOSE_FRAME = __core.ID_CLOSE_FRAME
ID_MOVE_FRAME = __core.ID_MOVE_FRAME
ID_RESIZE_FRAME = __core.ID_RESIZE_FRAME
ID_MAXIMIZE_FRAME = __core.ID_MAXIMIZE_FRAME
ID_ICONIZE_FRAME = __core.ID_ICONIZE_FRAME
ID_RESTORE_FRAME = __core.ID_RESTORE_FRAME
ID_MDI_WINDOW_FIRST = __core.ID_MDI_WINDOW_FIRST
ID_MDI_WINDOW_CASCADE = __core.ID_MDI_WINDOW_CASCADE
ID_MDI_WINDOW_TILE_HORZ = __core.ID_MDI_WINDOW_TILE_HORZ
ID_MDI_WINDOW_TILE_VERT = __core.ID_MDI_WINDOW_TILE_VERT
ID_MDI_WINDOW_ARRANGE_ICONS = __core.ID_MDI_WINDOW_ARRANGE_ICONS
ID_MDI_WINDOW_PREV = __core.ID_MDI_WINDOW_PREV
ID_MDI_WINDOW_NEXT = __core.ID_MDI_WINDOW_NEXT
ID_MDI_WINDOW_LAST = __core.ID_MDI_WINDOW_LAST
ID_OSX_MENU_FIRST = __core.ID_OSX_MENU_FIRST
ID_OSX_HIDE = __core.ID_OSX_HIDE
ID_OSX_HIDEOTHERS = __core.ID_OSX_HIDEOTHERS
ID_OSX_SHOWALL = __core.ID_OSX_SHOWALL
ID_OSX_MENU_LAST = __core.ID_OSX_MENU_LAST
ID_FILEDLGG = __core.ID_FILEDLGG
ID_FILECTRL = __core.ID_FILECTRL
ID_HIGHEST = __core.ID_HIGHEST
MENU_TEAROFF = __core.MENU_TEAROFF
MB_DOCKABLE = __core.MB_DOCKABLE
NO_FULL_REPAINT_ON_RESIZE = __core.NO_FULL_REPAINT_ON_RESIZE
FULL_REPAINT_ON_RESIZE = __core.FULL_REPAINT_ON_RESIZE
LI_HORIZONTAL = __core.LI_HORIZONTAL
LI_VERTICAL = __core.LI_VERTICAL
WS_EX_VALIDATE_RECURSIVELY = __core.WS_EX_VALIDATE_RECURSIVELY
WS_EX_BLOCK_EVENTS = __core.WS_EX_BLOCK_EVENTS
WS_EX_TRANSIENT = __core.WS_EX_TRANSIENT
WS_EX_THEMED_BACKGROUND = __core.WS_EX_THEMED_BACKGROUND
WS_EX_PROCESS_IDLE = __core.WS_EX_PROCESS_IDLE
WS_EX_PROCESS_UI_UPDATES = __core.WS_EX_PROCESS_UI_UPDATES
CENTRE = __core.CENTRE
CENTER = __core.CENTER
HORIZONTAL = __core.HORIZONTAL
VERTICAL = __core.VERTICAL
BOTH = __core.BOTH
ORIENTATION_MASK = __core.ORIENTATION_MASK
LEFT = __core.LEFT
RIGHT = __core.RIGHT
UP = __core.UP
DOWN = __core.DOWN
TOP = __core.TOP
BOTTOM = __core.BOTTOM
NORTH = __core.NORTH
SOUTH = __core.SOUTH
WEST = __core.WEST
EAST = __core.EAST
ALL = __core.ALL
DIRECTION_MASK = __core.DIRECTION_MASK
ALIGN_INVALID = __core.ALIGN_INVALID
ALIGN_NOT = __core.ALIGN_NOT
ALIGN_CENTER_HORIZONTAL = __core.ALIGN_CENTER_HORIZONTAL
ALIGN_CENTRE_HORIZONTAL = __core.ALIGN_CENTRE_HORIZONTAL
ALIGN_LEFT = __core.ALIGN_LEFT
ALIGN_TOP = __core.ALIGN_TOP
ALIGN_RIGHT = __core.ALIGN_RIGHT
ALIGN_BOTTOM = __core.ALIGN_BOTTOM
ALIGN_CENTER_VERTICAL = __core.ALIGN_CENTER_VERTICAL
ALIGN_CENTRE_VERTICAL = __core.ALIGN_CENTRE_VERTICAL
ALIGN_CENTER = __core.ALIGN_CENTER
ALIGN_CENTRE = __core.ALIGN_CENTRE
ALIGN_MASK = __core.ALIGN_MASK
FIXED_MINSIZE = __core.FIXED_MINSIZE
RESERVE_SPACE_EVEN_IF_HIDDEN = __core.RESERVE_SPACE_EVEN_IF_HIDDEN
SIZER_FLAG_BITS_MASK = __core.SIZER_FLAG_BITS_MASK
ADJUST_MINSIZE = 0 
STRETCH_NOT = __core.STRETCH_NOT
SHRINK = __core.SHRINK
GROW = __core.GROW
EXPAND = __core.EXPAND
SHAPED = __core.SHAPED
TILE = __core.TILE
STRETCH_MASK = __core.STRETCH_MASK
BORDER_DEFAULT = __core.BORDER_DEFAULT
BORDER_NONE = __core.BORDER_NONE
BORDER_STATIC = __core.BORDER_STATIC
BORDER_SIMPLE = __core.BORDER_SIMPLE
BORDER_RAISED = __core.BORDER_RAISED
BORDER_SUNKEN = __core.BORDER_SUNKEN
BORDER_DOUBLE = __core.BORDER_DOUBLE
BORDER_THEME = __core.BORDER_THEME
BORDER_MASK = __core.BORDER_MASK
BG_STYLE_ERASE = __core.BG_STYLE_ERASE
BG_STYLE_SYSTEM = __core.BG_STYLE_SYSTEM
BG_STYLE_PAINT = __core.BG_STYLE_PAINT
BG_STYLE_TRANSPARENT = __core.BG_STYLE_TRANSPARENT
BG_STYLE_COLOUR = __core.BG_STYLE_COLOUR
BG_STYLE_CUSTOM = __core.BG_STYLE_CUSTOM
DEFAULT = __core.DEFAULT
DECORATIVE = __core.DECORATIVE
ROMAN = __core.ROMAN
SCRIPT = __core.SCRIPT
SWISS = __core.SWISS
MODERN = __core.MODERN
TELETYPE = __core.TELETYPE
VARIABLE = __core.VARIABLE
FIXED = __core.FIXED
NORMAL = __core.NORMAL
LIGHT = __core.LIGHT
BOLD = __core.BOLD
ITALIC = __core.ITALIC
SLANT = __core.SLANT
SOLID = __core.SOLID
DOT = __core.DOT
LONG_DASH = __core.LONG_DASH
SHORT_DASH = __core.SHORT_DASH
DOT_DASH = __core.DOT_DASH
USER_DASH = __core.USER_DASH
TRANSPARENT = __core.TRANSPARENT
STIPPLE = __core.STIPPLE
STIPPLE_MASK = __core.STIPPLE_MASK
STIPPLE_MASK_OPAQUE = __core.STIPPLE_MASK_OPAQUE
BDIAGONAL_HATCH = __core.BDIAGONAL_HATCH
CROSSDIAG_HATCH = __core.CROSSDIAG_HATCH
FDIAGONAL_HATCH = __core.FDIAGONAL_HATCH
CROSS_HATCH = __core.CROSS_HATCH
HORIZONTAL_HATCH = __core.HORIZONTAL_HATCH
VERTICAL_HATCH = __core.VERTICAL_HATCH
WXK_NONE = __core.WXK_NONE
WXK_CONTROL_A = __core.WXK_CONTROL_A
WXK_CONTROL_B = __core.WXK_CONTROL_B
WXK_CONTROL_C = __core.WXK_CONTROL_C
WXK_CONTROL_D = __core.WXK_CONTROL_D
WXK_CONTROL_E = __core.WXK_CONTROL_E
WXK_CONTROL_F = __core.WXK_CONTROL_F
WXK_CONTROL_G = __core.WXK_CONTROL_G
WXK_CONTROL_H = __core.WXK_CONTROL_H
WXK_CONTROL_I = __core.WXK_CONTROL_I
WXK_CONTROL_J = __core.WXK_CONTROL_J
WXK_CONTROL_K = __core.WXK_CONTROL_K
WXK_CONTROL_L = __core.WXK_CONTROL_L
WXK_CONTROL_M = __core.WXK_CONTROL_M
WXK_CONTROL_N = __core.WXK_CONTROL_N
WXK_CONTROL_O = __core.WXK_CONTROL_O
WXK_CONTROL_P = __core.WXK_CONTROL_P
WXK_CONTROL_Q = __core.WXK_CONTROL_Q
WXK_CONTROL_R = __core.WXK_CONTROL_R
WXK_CONTROL_S = __core.WXK_CONTROL_S
WXK_CONTROL_T = __core.WXK_CONTROL_T
WXK_CONTROL_U = __core.WXK_CONTROL_U
WXK_CONTROL_V = __core.WXK_CONTROL_V
WXK_CONTROL_W = __core.WXK_CONTROL_W
WXK_CONTROL_X = __core.WXK_CONTROL_X
WXK_CONTROL_Y = __core.WXK_CONTROL_Y
WXK_CONTROL_Z = __core.WXK_CONTROL_Z
WXK_BACK = __core.WXK_BACK
WXK_TAB = __core.WXK_TAB
WXK_RETURN = __core.WXK_RETURN
WXK_ESCAPE = __core.WXK_ESCAPE
WXK_SPACE = __core.WXK_SPACE
WXK_DELETE = __core.WXK_DELETE
WXK_START = __core.WXK_START
WXK_LBUTTON = __core.WXK_LBUTTON
WXK_RBUTTON = __core.WXK_RBUTTON
WXK_CANCEL = __core.WXK_CANCEL
WXK_MBUTTON = __core.WXK_MBUTTON
WXK_CLEAR = __core.WXK_CLEAR
WXK_SHIFT = __core.WXK_SHIFT
WXK_ALT = __core.WXK_ALT
WXK_CONTROL = __core.WXK_CONTROL
WXK_MENU = __core.WXK_MENU
WXK_PAUSE = __core.WXK_PAUSE
WXK_CAPITAL = __core.WXK_CAPITAL
WXK_END = __core.WXK_END
WXK_HOME = __core.WXK_HOME
WXK_LEFT = __core.WXK_LEFT
WXK_UP = __core.WXK_UP
WXK_RIGHT = __core.WXK_RIGHT
WXK_DOWN = __core.WXK_DOWN
WXK_SELECT = __core.WXK_SELECT
WXK_PRINT = __core.WXK_PRINT
WXK_EXECUTE = __core.WXK_EXECUTE
WXK_SNAPSHOT = __core.WXK_SNAPSHOT
WXK_INSERT = __core.WXK_INSERT
WXK_HELP = __core.WXK_HELP
WXK_NUMPAD0 = __core.WXK_NUMPAD0
WXK_NUMPAD1 = __core.WXK_NUMPAD1
WXK_NUMPAD2 = __core.WXK_NUMPAD2
WXK_NUMPAD3 = __core.WXK_NUMPAD3
WXK_NUMPAD4 = __core.WXK_NUMPAD4
WXK_NUMPAD5 = __core.WXK_NUMPAD5
WXK_NUMPAD6 = __core.WXK_NUMPAD6
WXK_NUMPAD7 = __core.WXK_NUMPAD7
WXK_NUMPAD8 = __core.WXK_NUMPAD8
WXK_NUMPAD9 = __core.WXK_NUMPAD9
WXK_MULTIPLY = __core.WXK_MULTIPLY
WXK_ADD = __core.WXK_ADD
WXK_SEPARATOR = __core.WXK_SEPARATOR
WXK_SUBTRACT = __core.WXK_SUBTRACT
WXK_DECIMAL = __core.WXK_DECIMAL
WXK_DIVIDE = __core.WXK_DIVIDE
WXK_F1 = __core.WXK_F1
WXK_F2 = __core.WXK_F2
WXK_F3 = __core.WXK_F3
WXK_F4 = __core.WXK_F4
WXK_F5 = __core.WXK_F5
WXK_F6 = __core.WXK_F6
WXK_F7 = __core.WXK_F7
WXK_F8 = __core.WXK_F8
WXK_F9 = __core.WXK_F9
WXK_F10 = __core.WXK_F10
WXK_F11 = __core.WXK_F11
WXK_F12 = __core.WXK_F12
WXK_F13 = __core.WXK_F13
WXK_F14 = __core.WXK_F14
WXK_F15 = __core.WXK_F15
WXK_F16 = __core.WXK_F16
WXK_F17 = __core.WXK_F17
WXK_F18 = __core.WXK_F18
WXK_F19 = __core.WXK_F19
WXK_F20 = __core.WXK_F20
WXK_F21 = __core.WXK_F21
WXK_F22 = __core.WXK_F22
WXK_F23 = __core.WXK_F23
WXK_F24 = __core.WXK_F24
WXK_NUMLOCK = __core.WXK_NUMLOCK
WXK_SCROLL = __core.WXK_SCROLL
WXK_PAGEUP = __core.WXK_PAGEUP
WXK_PAGEDOWN = __core.WXK_PAGEDOWN
WXK_NUMPAD_SPACE = __core.WXK_NUMPAD_SPACE
WXK_NUMPAD_TAB = __core.WXK_NUMPAD_TAB
WXK_NUMPAD_ENTER = __core.WXK_NUMPAD_ENTER
WXK_NUMPAD_F1 = __core.WXK_NUMPAD_F1
WXK_NUMPAD_F2 = __core.WXK_NUMPAD_F2
WXK_NUMPAD_F3 = __core.WXK_NUMPAD_F3
WXK_NUMPAD_F4 = __core.WXK_NUMPAD_F4
WXK_NUMPAD_HOME = __core.WXK_NUMPAD_HOME
WXK_NUMPAD_LEFT = __core.WXK_NUMPAD_LEFT
WXK_NUMPAD_UP = __core.WXK_NUMPAD_UP
WXK_NUMPAD_RIGHT = __core.WXK_NUMPAD_RIGHT
WXK_NUMPAD_DOWN = __core.WXK_NUMPAD_DOWN
WXK_NUMPAD_PAGEUP = __core.WXK_NUMPAD_PAGEUP
WXK_NUMPAD_PAGEDOWN = __core.WXK_NUMPAD_PAGEDOWN
WXK_NUMPAD_END = __core.WXK_NUMPAD_END
WXK_NUMPAD_BEGIN = __core.WXK_NUMPAD_BEGIN
WXK_NUMPAD_INSERT = __core.WXK_NUMPAD_INSERT
WXK_NUMPAD_DELETE = __core.WXK_NUMPAD_DELETE
WXK_NUMPAD_EQUAL = __core.WXK_NUMPAD_EQUAL
WXK_NUMPAD_MULTIPLY = __core.WXK_NUMPAD_MULTIPLY
WXK_NUMPAD_ADD = __core.WXK_NUMPAD_ADD
WXK_NUMPAD_SEPARATOR = __core.WXK_NUMPAD_SEPARATOR
WXK_NUMPAD_SUBTRACT = __core.WXK_NUMPAD_SUBTRACT
WXK_NUMPAD_DECIMAL = __core.WXK_NUMPAD_DECIMAL
WXK_NUMPAD_DIVIDE = __core.WXK_NUMPAD_DIVIDE
WXK_WINDOWS_LEFT = __core.WXK_WINDOWS_LEFT
WXK_WINDOWS_RIGHT = __core.WXK_WINDOWS_RIGHT
WXK_WINDOWS_MENU = __core.WXK_WINDOWS_MENU
WXK_RAW_CONTROL = __core.WXK_RAW_CONTROL
WXK_COMMAND = __core.WXK_COMMAND
WXK_SPECIAL1 = __core.WXK_SPECIAL1
WXK_SPECIAL2 = __core.WXK_SPECIAL2
WXK_SPECIAL3 = __core.WXK_SPECIAL3
WXK_SPECIAL4 = __core.WXK_SPECIAL4
WXK_SPECIAL5 = __core.WXK_SPECIAL5
WXK_SPECIAL6 = __core.WXK_SPECIAL6
WXK_SPECIAL7 = __core.WXK_SPECIAL7
WXK_SPECIAL8 = __core.WXK_SPECIAL8
WXK_SPECIAL9 = __core.WXK_SPECIAL9
WXK_SPECIAL10 = __core.WXK_SPECIAL10
WXK_SPECIAL11 = __core.WXK_SPECIAL11
WXK_SPECIAL12 = __core.WXK_SPECIAL12
WXK_SPECIAL13 = __core.WXK_SPECIAL13
WXK_SPECIAL14 = __core.WXK_SPECIAL14
WXK_SPECIAL15 = __core.WXK_SPECIAL15
WXK_SPECIAL16 = __core.WXK_SPECIAL16
WXK_SPECIAL17 = __core.WXK_SPECIAL17
WXK_SPECIAL18 = __core.WXK_SPECIAL18
WXK_SPECIAL19 = __core.WXK_SPECIAL19
WXK_SPECIAL20 = __core.WXK_SPECIAL20
WXK_PRIOR = WXK_PAGEUP
WXK_NEXT  = WXK_PAGEDOWN
WXK_NUMPAD_PRIOR = WXK_NUMPAD_PAGEUP
WXK_NUMPAD_NEXT  = WXK_NUMPAD_PAGEDOWN    

PAPER_NONE = __core.PAPER_NONE
PAPER_LETTER = __core.PAPER_LETTER
PAPER_LEGAL = __core.PAPER_LEGAL
PAPER_A4 = __core.PAPER_A4
PAPER_CSHEET = __core.PAPER_CSHEET
PAPER_DSHEET = __core.PAPER_DSHEET
PAPER_ESHEET = __core.PAPER_ESHEET
PAPER_LETTERSMALL = __core.PAPER_LETTERSMALL
PAPER_TABLOID = __core.PAPER_TABLOID
PAPER_LEDGER = __core.PAPER_LEDGER
PAPER_STATEMENT = __core.PAPER_STATEMENT
PAPER_EXECUTIVE = __core.PAPER_EXECUTIVE
PAPER_A3 = __core.PAPER_A3
PAPER_A4SMALL = __core.PAPER_A4SMALL
PAPER_A5 = __core.PAPER_A5
PAPER_B4 = __core.PAPER_B4
PAPER_B5 = __core.PAPER_B5
PAPER_FOLIO = __core.PAPER_FOLIO
PAPER_QUARTO = __core.PAPER_QUARTO
PAPER_10X14 = __core.PAPER_10X14
PAPER_11X17 = __core.PAPER_11X17
PAPER_NOTE = __core.PAPER_NOTE
PAPER_ENV_9 = __core.PAPER_ENV_9
PAPER_ENV_10 = __core.PAPER_ENV_10
PAPER_ENV_11 = __core.PAPER_ENV_11
PAPER_ENV_12 = __core.PAPER_ENV_12
PAPER_ENV_14 = __core.PAPER_ENV_14
PAPER_ENV_DL = __core.PAPER_ENV_DL
PAPER_ENV_C5 = __core.PAPER_ENV_C5
PAPER_ENV_C3 = __core.PAPER_ENV_C3
PAPER_ENV_C4 = __core.PAPER_ENV_C4
PAPER_ENV_C6 = __core.PAPER_ENV_C6
PAPER_ENV_C65 = __core.PAPER_ENV_C65
PAPER_ENV_B4 = __core.PAPER_ENV_B4
PAPER_ENV_B5 = __core.PAPER_ENV_B5
PAPER_ENV_B6 = __core.PAPER_ENV_B6
PAPER_ENV_ITALY = __core.PAPER_ENV_ITALY
PAPER_ENV_MONARCH = __core.PAPER_ENV_MONARCH
PAPER_ENV_PERSONAL = __core.PAPER_ENV_PERSONAL
PAPER_FANFOLD_US = __core.PAPER_FANFOLD_US
PAPER_FANFOLD_STD_GERMAN = __core.PAPER_FANFOLD_STD_GERMAN
PAPER_FANFOLD_LGL_GERMAN = __core.PAPER_FANFOLD_LGL_GERMAN
PAPER_ISO_B4 = __core.PAPER_ISO_B4
PAPER_JAPANESE_POSTCARD = __core.PAPER_JAPANESE_POSTCARD
PAPER_9X11 = __core.PAPER_9X11
PAPER_10X11 = __core.PAPER_10X11
PAPER_15X11 = __core.PAPER_15X11
PAPER_ENV_INVITE = __core.PAPER_ENV_INVITE
PAPER_LETTER_EXTRA = __core.PAPER_LETTER_EXTRA
PAPER_LEGAL_EXTRA = __core.PAPER_LEGAL_EXTRA
PAPER_TABLOID_EXTRA = __core.PAPER_TABLOID_EXTRA
PAPER_A4_EXTRA = __core.PAPER_A4_EXTRA
PAPER_LETTER_TRANSVERSE = __core.PAPER_LETTER_TRANSVERSE
PAPER_A4_TRANSVERSE = __core.PAPER_A4_TRANSVERSE
PAPER_LETTER_EXTRA_TRANSVERSE = __core.PAPER_LETTER_EXTRA_TRANSVERSE
PAPER_A_PLUS = __core.PAPER_A_PLUS
PAPER_B_PLUS = __core.PAPER_B_PLUS
PAPER_LETTER_PLUS = __core.PAPER_LETTER_PLUS
PAPER_A4_PLUS = __core.PAPER_A4_PLUS
PAPER_A5_TRANSVERSE = __core.PAPER_A5_TRANSVERSE
PAPER_B5_TRANSVERSE = __core.PAPER_B5_TRANSVERSE
PAPER_A3_EXTRA = __core.PAPER_A3_EXTRA
PAPER_A5_EXTRA = __core.PAPER_A5_EXTRA
PAPER_B5_EXTRA = __core.PAPER_B5_EXTRA
PAPER_A2 = __core.PAPER_A2
PAPER_A3_TRANSVERSE = __core.PAPER_A3_TRANSVERSE
PAPER_A3_EXTRA_TRANSVERSE = __core.PAPER_A3_EXTRA_TRANSVERSE
PAPER_DBL_JAPANESE_POSTCARD = __core.PAPER_DBL_JAPANESE_POSTCARD
PAPER_A6 = __core.PAPER_A6
PAPER_JENV_KAKU2 = __core.PAPER_JENV_KAKU2
PAPER_JENV_KAKU3 = __core.PAPER_JENV_KAKU3
PAPER_JENV_CHOU3 = __core.PAPER_JENV_CHOU3
PAPER_JENV_CHOU4 = __core.PAPER_JENV_CHOU4
PAPER_LETTER_ROTATED = __core.PAPER_LETTER_ROTATED
PAPER_A3_ROTATED = __core.PAPER_A3_ROTATED
PAPER_A4_ROTATED = __core.PAPER_A4_ROTATED
PAPER_A5_ROTATED = __core.PAPER_A5_ROTATED
PAPER_B4_JIS_ROTATED = __core.PAPER_B4_JIS_ROTATED
PAPER_B5_JIS_ROTATED = __core.PAPER_B5_JIS_ROTATED
PAPER_JAPANESE_POSTCARD_ROTATED = __core.PAPER_JAPANESE_POSTCARD_ROTATED
PAPER_DBL_JAPANESE_POSTCARD_ROTATED = __core.PAPER_DBL_JAPANESE_POSTCARD_ROTATED
PAPER_A6_ROTATED = __core.PAPER_A6_ROTATED
PAPER_JENV_KAKU2_ROTATED = __core.PAPER_JENV_KAKU2_ROTATED
PAPER_JENV_KAKU3_ROTATED = __core.PAPER_JENV_KAKU3_ROTATED
PAPER_JENV_CHOU3_ROTATED = __core.PAPER_JENV_CHOU3_ROTATED
PAPER_JENV_CHOU4_ROTATED = __core.PAPER_JENV_CHOU4_ROTATED
PAPER_B6_JIS = __core.PAPER_B6_JIS
PAPER_B6_JIS_ROTATED = __core.PAPER_B6_JIS_ROTATED
PAPER_12X11 = __core.PAPER_12X11
PAPER_JENV_YOU4 = __core.PAPER_JENV_YOU4
PAPER_JENV_YOU4_ROTATED = __core.PAPER_JENV_YOU4_ROTATED
PAPER_P16K = __core.PAPER_P16K
PAPER_P32K = __core.PAPER_P32K
PAPER_P32KBIG = __core.PAPER_P32KBIG
PAPER_PENV_1 = __core.PAPER_PENV_1
PAPER_PENV_2 = __core.PAPER_PENV_2
PAPER_PENV_3 = __core.PAPER_PENV_3
PAPER_PENV_4 = __core.PAPER_PENV_4
PAPER_PENV_5 = __core.PAPER_PENV_5
PAPER_PENV_6 = __core.PAPER_PENV_6
PAPER_PENV_7 = __core.PAPER_PENV_7
PAPER_PENV_8 = __core.PAPER_PENV_8
PAPER_PENV_9 = __core.PAPER_PENV_9
PAPER_PENV_10 = __core.PAPER_PENV_10
PAPER_P16K_ROTATED = __core.PAPER_P16K_ROTATED
PAPER_P32K_ROTATED = __core.PAPER_P32K_ROTATED
PAPER_P32KBIG_ROTATED = __core.PAPER_P32KBIG_ROTATED
PAPER_PENV_1_ROTATED = __core.PAPER_PENV_1_ROTATED
PAPER_PENV_2_ROTATED = __core.PAPER_PENV_2_ROTATED
PAPER_PENV_3_ROTATED = __core.PAPER_PENV_3_ROTATED
PAPER_PENV_4_ROTATED = __core.PAPER_PENV_4_ROTATED
PAPER_PENV_5_ROTATED = __core.PAPER_PENV_5_ROTATED
PAPER_PENV_6_ROTATED = __core.PAPER_PENV_6_ROTATED
PAPER_PENV_7_ROTATED = __core.PAPER_PENV_7_ROTATED
PAPER_PENV_8_ROTATED = __core.PAPER_PENV_8_ROTATED
PAPER_PENV_9_ROTATED = __core.PAPER_PENV_9_ROTATED
PAPER_PENV_10_ROTATED = __core.PAPER_PENV_10_ROTATED
PAPER_A0 = __core.PAPER_A0
PAPER_A1 = __core.PAPER_A1
PORTRAIT = __core.PORTRAIT
LANDSCAPE = __core.LANDSCAPE
DUPLEX_SIMPLEX = __core.DUPLEX_SIMPLEX
DUPLEX_HORIZONTAL = __core.DUPLEX_HORIZONTAL
DUPLEX_VERTICAL = __core.DUPLEX_VERTICAL
ITEM_SEPARATOR = __core.ITEM_SEPARATOR
ITEM_NORMAL = __core.ITEM_NORMAL
ITEM_CHECK = __core.ITEM_CHECK
ITEM_RADIO = __core.ITEM_RADIO
ITEM_DROPDOWN = __core.ITEM_DROPDOWN
ITEM_MAX = __core.ITEM_MAX
CHK_UNCHECKED = __core.CHK_UNCHECKED
CHK_CHECKED = __core.CHK_CHECKED
CHK_UNDETERMINED = __core.CHK_UNDETERMINED
HT_NOWHERE = __core.HT_NOWHERE
HT_SCROLLBAR_FIRST = __core.HT_SCROLLBAR_FIRST
HT_SCROLLBAR_ARROW_LINE_1 = __core.HT_SCROLLBAR_ARROW_LINE_1
HT_SCROLLBAR_ARROW_LINE_2 = __core.HT_SCROLLBAR_ARROW_LINE_2
HT_SCROLLBAR_ARROW_PAGE_1 = __core.HT_SCROLLBAR_ARROW_PAGE_1
HT_SCROLLBAR_ARROW_PAGE_2 = __core.HT_SCROLLBAR_ARROW_PAGE_2
HT_SCROLLBAR_THUMB = __core.HT_SCROLLBAR_THUMB
HT_SCROLLBAR_BAR_1 = __core.HT_SCROLLBAR_BAR_1
HT_SCROLLBAR_BAR_2 = __core.HT_SCROLLBAR_BAR_2
HT_SCROLLBAR_LAST = __core.HT_SCROLLBAR_LAST
HT_WINDOW_OUTSIDE = __core.HT_WINDOW_OUTSIDE
HT_WINDOW_INSIDE = __core.HT_WINDOW_INSIDE
HT_WINDOW_VERT_SCROLLBAR = __core.HT_WINDOW_VERT_SCROLLBAR
HT_WINDOW_HORZ_SCROLLBAR = __core.HT_WINDOW_HORZ_SCROLLBAR
HT_WINDOW_CORNER = __core.HT_WINDOW_CORNER
HT_MAX = __core.HT_MAX
MOD_NONE = __core.MOD_NONE
MOD_ALT = __core.MOD_ALT
MOD_CONTROL = __core.MOD_CONTROL
MOD_ALTGR = __core.MOD_ALTGR
MOD_SHIFT = __core.MOD_SHIFT
MOD_META = __core.MOD_META
MOD_WIN = __core.MOD_WIN
MOD_RAW_CONTROL = __core.MOD_RAW_CONTROL
MOD_CMD = __core.MOD_CMD
MOD_ALL = __core.MOD_ALL
UPDATE_UI_NONE = __core.UPDATE_UI_NONE
UPDATE_UI_RECURSE = __core.UPDATE_UI_RECURSE
UPDATE_UI_FROMIDLE = __core.UPDATE_UI_FROMIDLE
Layout_Default = __core.Layout_Default
Layout_LeftToRight = __core.Layout_LeftToRight
Layout_RightToLeft = __core.Layout_RightToLeft
#---------------------------------------------------------------------------

class Object(object):
    """
    The base class for most wx objects, although in wxPython not
    much functionality is needed nor exposed.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def GetClassName(*args, **kwargs):
        """
        GetClassName(self) -> String

        Returns the class name of the C++ class using wxRTTI.
        """
        return __core.Object_GetClassName(*args, **kwargs)

    def Destroy(*args, **kwargs):
        """
        Destroy(self)

        Deletes the C++ object this Python object is a proxy for.
        """
        args[0].this.own(False)
        return __core.Object_Destroy(*args, **kwargs)

    def IsSameAs(*args, **kwargs):
        """
        IsSameAs(self, Object p) -> bool

        For wx.Objects that use C++ reference counting internally, this method
        can be used to determine if two objects are referencing the same data
        object.
        """
        return __core.Object_IsSameAs(*args, **kwargs)

    ClassName = property(GetClassName,doc="See `GetClassName`") 
__core.Object_swigregister(Object)
_wxPySetDictionary = __core._wxPySetDictionary
cvar = __core.cvar
EmptyString = cvar.EmptyString

class RefCounter(object):
    """Proxy of C++ RefCounter class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> RefCounter"""
        this = __core.new_RefCounter(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_RefCounter
    __del__ = lambda self : None;
    def GetRefCount(*args, **kwargs):
        """GetRefCount(self) -> int"""
        return __core.RefCounter_GetRefCount(*args, **kwargs)

    def IncRef(*args, **kwargs):
        """IncRef(self)"""
        return __core.RefCounter_IncRef(*args, **kwargs)

    def DecRef(*args, **kwargs):
        """DecRef(self)"""
        return __core.RefCounter_DecRef(*args, **kwargs)

__core.RefCounter_swigregister(RefCounter)

#---------------------------------------------------------------------------

BITMAP_TYPE_INVALID = __core.BITMAP_TYPE_INVALID
BITMAP_TYPE_BMP = __core.BITMAP_TYPE_BMP
BITMAP_TYPE_ICO = __core.BITMAP_TYPE_ICO
BITMAP_TYPE_CUR = __core.BITMAP_TYPE_CUR
BITMAP_TYPE_XBM = __core.BITMAP_TYPE_XBM
BITMAP_TYPE_XBM_DATA = __core.BITMAP_TYPE_XBM_DATA
BITMAP_TYPE_XPM = __core.BITMAP_TYPE_XPM
BITMAP_TYPE_XPM_DATA = __core.BITMAP_TYPE_XPM_DATA
BITMAP_TYPE_TIF = __core.BITMAP_TYPE_TIF
BITMAP_TYPE_TIFF = __core.BITMAP_TYPE_TIFF
BITMAP_TYPE_GIF = __core.BITMAP_TYPE_GIF
BITMAP_TYPE_PNG = __core.BITMAP_TYPE_PNG
BITMAP_TYPE_JPEG = __core.BITMAP_TYPE_JPEG
BITMAP_TYPE_PNM = __core.BITMAP_TYPE_PNM
BITMAP_TYPE_PCX = __core.BITMAP_TYPE_PCX
BITMAP_TYPE_PICT = __core.BITMAP_TYPE_PICT
BITMAP_TYPE_ICON = __core.BITMAP_TYPE_ICON
BITMAP_TYPE_ANI = __core.BITMAP_TYPE_ANI
BITMAP_TYPE_IFF = __core.BITMAP_TYPE_IFF
BITMAP_TYPE_TGA = __core.BITMAP_TYPE_TGA
BITMAP_TYPE_MACCURSOR = __core.BITMAP_TYPE_MACCURSOR
BITMAP_TYPE_MAX = __core.BITMAP_TYPE_MAX
BITMAP_TYPE_ANY = __core.BITMAP_TYPE_ANY
BITMAP_DEFAULT_TYPE = __core.BITMAP_DEFAULT_TYPE
ODDEVEN_RULE = __core.ODDEVEN_RULE
WINDING_RULE = __core.WINDING_RULE
CURSOR_NONE = __core.CURSOR_NONE
CURSOR_ARROW = __core.CURSOR_ARROW
CURSOR_RIGHT_ARROW = __core.CURSOR_RIGHT_ARROW
CURSOR_BULLSEYE = __core.CURSOR_BULLSEYE
CURSOR_CHAR = __core.CURSOR_CHAR
CURSOR_CROSS = __core.CURSOR_CROSS
CURSOR_HAND = __core.CURSOR_HAND
CURSOR_IBEAM = __core.CURSOR_IBEAM
CURSOR_LEFT_BUTTON = __core.CURSOR_LEFT_BUTTON
CURSOR_MAGNIFIER = __core.CURSOR_MAGNIFIER
CURSOR_MIDDLE_BUTTON = __core.CURSOR_MIDDLE_BUTTON
CURSOR_NO_ENTRY = __core.CURSOR_NO_ENTRY
CURSOR_PAINT_BRUSH = __core.CURSOR_PAINT_BRUSH
CURSOR_PENCIL = __core.CURSOR_PENCIL
CURSOR_POINT_LEFT = __core.CURSOR_POINT_LEFT
CURSOR_POINT_RIGHT = __core.CURSOR_POINT_RIGHT
CURSOR_QUESTION_ARROW = __core.CURSOR_QUESTION_ARROW
CURSOR_RIGHT_BUTTON = __core.CURSOR_RIGHT_BUTTON
CURSOR_SIZENESW = __core.CURSOR_SIZENESW
CURSOR_SIZENS = __core.CURSOR_SIZENS
CURSOR_SIZENWSE = __core.CURSOR_SIZENWSE
CURSOR_SIZEWE = __core.CURSOR_SIZEWE
CURSOR_SIZING = __core.CURSOR_SIZING
CURSOR_SPRAYCAN = __core.CURSOR_SPRAYCAN
CURSOR_WAIT = __core.CURSOR_WAIT
CURSOR_WATCH = __core.CURSOR_WATCH
CURSOR_BLANK = __core.CURSOR_BLANK
CURSOR_DEFAULT = __core.CURSOR_DEFAULT
CURSOR_COPY_ARROW = __core.CURSOR_COPY_ARROW
CURSOR_ARROWWAIT = __core.CURSOR_ARROWWAIT
CURSOR_OPEN_HAND = __core.CURSOR_OPEN_HAND
CURSOR_CLOSED_HAND = __core.CURSOR_CLOSED_HAND
CURSOR_MAX = __core.CURSOR_MAX
#---------------------------------------------------------------------------

class Size(object):
    """
    wx.Size is a useful data structure used to represent the size of
    something.  It simply contains integer width and height
    properties.  In most places in wxPython where a wx.Size is
    expected a (width, height) tuple can be used instead.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    width = property(__core.Size_width_get, __core.Size_width_set)
    height = property(__core.Size_height_get, __core.Size_height_set)
    x = width; y = height 
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int w=0, int h=0) -> Size

        Creates a size object.
        """
        this = __core.new_Size(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Size
    __del__ = lambda self : None;
    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Test for equality of wx.Size objects.
        """
        return __core.Size___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Test for inequality of wx.Size objects.
        """
        return __core.Size___ne__(*args, **kwargs)

    def __add__(*args, **kwargs):
        """
        __add__(self, Size sz) -> Size

        Add sz's proprties to this and return the result.
        """
        return __core.Size___add__(*args, **kwargs)

    def __sub__(*args, **kwargs):
        """
        __sub__(self, Size sz) -> Size

        Subtract sz's properties from this and return the result.
        """
        return __core.Size___sub__(*args, **kwargs)

    def IncTo(*args, **kwargs):
        """
        IncTo(self, Size sz)

        Increments this object so that both of its dimensions are not less
        than the corresponding dimensions of the size.
        """
        return __core.Size_IncTo(*args, **kwargs)

    def DecTo(*args, **kwargs):
        """
        DecTo(self, Size sz)

        Decrements this object so that both of its dimensions are not greater
        than the corresponding dimensions of the size.
        """
        return __core.Size_DecTo(*args, **kwargs)

    def IncBy(*args, **kwargs):
        """IncBy(self, int dx, int dy)"""
        return __core.Size_IncBy(*args, **kwargs)

    def DecBy(*args, **kwargs):
        """DecBy(self, int dx, int dy)"""
        return __core.Size_DecBy(*args, **kwargs)

    def Scale(*args, **kwargs):
        """
        Scale(self, float xscale, float yscale)

        Scales the dimensions of this object by the given factors.
        """
        return __core.Size_Scale(*args, **kwargs)

    def Set(*args, **kwargs):
        """
        Set(self, int w, int h)

        Set both width and height.
        """
        return __core.Size_Set(*args, **kwargs)

    def SetWidth(*args, **kwargs):
        """SetWidth(self, int w)"""
        return __core.Size_SetWidth(*args, **kwargs)

    def SetHeight(*args, **kwargs):
        """SetHeight(self, int h)"""
        return __core.Size_SetHeight(*args, **kwargs)

    def GetWidth(*args, **kwargs):
        """GetWidth(self) -> int"""
        return __core.Size_GetWidth(*args, **kwargs)

    def GetHeight(*args, **kwargs):
        """GetHeight(self) -> int"""
        return __core.Size_GetHeight(*args, **kwargs)

    def IsFullySpecified(*args, **kwargs):
        """
        IsFullySpecified(self) -> bool

        Returns True if both components of the size are non-default values.
        """
        return __core.Size_IsFullySpecified(*args, **kwargs)

    def SetDefaults(*args, **kwargs):
        """
        SetDefaults(self, Size size)

        Combine this size with the other one replacing the default components
        of this object (i.e. equal to -1) with those of the other.
        """
        return __core.Size_SetDefaults(*args, **kwargs)

    def Get(*args, **kwargs):
        """
        Get() -> (width,height)

        Returns the width and height properties as a tuple.
        """
        return __core.Size_Get(*args, **kwargs)

    asTuple = wx.deprecated(Get, "asTuple is deprecated, use `Get` instead")
    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'wx.Size'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.width = val
        elif index == 1: self.height = val
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0,0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (wx.Size, self.Get())

__core.Size_swigregister(Size)

#---------------------------------------------------------------------------

class RealPoint(object):
    """
    A data structure for representing a point or position with floating
    point x and y properties.  In wxPython most places that expect a
    wx.RealPoint can also accept a (x,y) tuple.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    x = property(__core.RealPoint_x_get, __core.RealPoint_x_set)
    y = property(__core.RealPoint_y_get, __core.RealPoint_y_set)
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, double x=0.0, double y=0.0) -> RealPoint

        Create a wx.RealPoint object
        """
        this = __core.new_RealPoint(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_RealPoint
    __del__ = lambda self : None;
    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Test for equality of wx.RealPoint objects.
        """
        return __core.RealPoint___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Test for inequality of wx.RealPoint objects.
        """
        return __core.RealPoint___ne__(*args, **kwargs)

    def __add__(*args, **kwargs):
        """
        __add__(self, RealPoint pt) -> RealPoint

        Add pt's proprties to this and return the result.
        """
        return __core.RealPoint___add__(*args, **kwargs)

    def __sub__(*args, **kwargs):
        """
        __sub__(self, RealPoint pt) -> RealPoint

        Subtract pt's properties from this and return the result.
        """
        return __core.RealPoint___sub__(*args, **kwargs)

    def Set(*args, **kwargs):
        """
        Set(self, double x, double y)

        Set both the x and y properties
        """
        return __core.RealPoint_Set(*args, **kwargs)

    def Get(*args, **kwargs):
        """
        Get() -> (x,y)

        Return the x and y properties as a tuple. 
        """
        return __core.RealPoint_Get(*args, **kwargs)

    asTuple = wx.deprecated(Get, "asTuple is deprecated, use `Get` instead")
    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'wx.RealPoint'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.x = val
        elif index == 1: self.y = val
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0.0, 0.0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (wx.RealPoint, self.Get())

__core.RealPoint_swigregister(RealPoint)

#---------------------------------------------------------------------------

class Point(object):
    """
    A data structure for representing a point or position with integer x
    and y properties.  Most places in wxPython that expect a wx.Point can
    also accept a (x,y) tuple.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    x = property(__core.Point_x_get, __core.Point_x_set)
    y = property(__core.Point_y_get, __core.Point_y_set)
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int x=0, int y=0) -> Point

        Create a wx.Point object
        """
        this = __core.new_Point(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Point
    __del__ = lambda self : None;
    def IsFullySpecified(*args, **kwargs):
        """IsFullySpecified(self) -> bool"""
        return __core.Point_IsFullySpecified(*args, **kwargs)

    def SetDefaults(*args, **kwargs):
        """SetDefaults(self, Point pt)"""
        return __core.Point_SetDefaults(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Test for equality of wx.Point objects.
        """
        return __core.Point___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Test for inequality of wx.Point objects.
        """
        return __core.Point___ne__(*args, **kwargs)

    def __add__(*args, **kwargs):
        """
        __add__(self, Point pt) -> Point

        Add pt's proprties to this and return the result.
        """
        return __core.Point___add__(*args, **kwargs)

    def __sub__(*args, **kwargs):
        """
        __sub__(self, Point pt) -> Point

        Subtract pt's properties from this and return the result.
        """
        return __core.Point___sub__(*args, **kwargs)

    def Set(*args, **kwargs):
        """
        Set(self, long x, long y)

        Set both the x and y properties
        """
        return __core.Point_Set(*args, **kwargs)

    def Get(*args, **kwargs):
        """
        Get() -> (x,y)

        Return the x and y properties as a tuple. 
        """
        return __core.Point_Get(*args, **kwargs)

    asTuple = wx.deprecated(Get, "asTuple is deprecated, use `Get` instead")
    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'wx.Point'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.x = val
        elif index == 1: self.y = val
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0,0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (wx.Point, self.Get())

__core.Point_swigregister(Point)

#---------------------------------------------------------------------------

class Rect(object):
    """
    A class for representing and manipulating rectangles.  It has x, y,
    width and height properties.  In wxPython most palces that expect a
    wx.Rect can also accept a (x,y,width,height) tuple.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int x=0, int y=0, int width=0, int height=0) -> Rect

        Create a new Rect object.
        """
        this = __core.new_Rect(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Rect
    __del__ = lambda self : None;
    def GetX(*args, **kwargs):
        """GetX(self) -> int"""
        return __core.Rect_GetX(*args, **kwargs)

    def SetX(*args, **kwargs):
        """SetX(self, int x)"""
        return __core.Rect_SetX(*args, **kwargs)

    def GetY(*args, **kwargs):
        """GetY(self) -> int"""
        return __core.Rect_GetY(*args, **kwargs)

    def SetY(*args, **kwargs):
        """SetY(self, int y)"""
        return __core.Rect_SetY(*args, **kwargs)

    def GetWidth(*args, **kwargs):
        """GetWidth(self) -> int"""
        return __core.Rect_GetWidth(*args, **kwargs)

    def SetWidth(*args, **kwargs):
        """SetWidth(self, int w)"""
        return __core.Rect_SetWidth(*args, **kwargs)

    def GetHeight(*args, **kwargs):
        """GetHeight(self) -> int"""
        return __core.Rect_GetHeight(*args, **kwargs)

    def SetHeight(*args, **kwargs):
        """SetHeight(self, int h)"""
        return __core.Rect_SetHeight(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """GetPosition(self) -> Point"""
        return __core.Rect_GetPosition(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, Point p)"""
        return __core.Rect_SetPosition(*args, **kwargs)

    def GetSize(*args, **kwargs):
        """GetSize(self) -> Size"""
        return __core.Rect_GetSize(*args, **kwargs)

    def SetSize(*args, **kwargs):
        """SetSize(self, Size s)"""
        return __core.Rect_SetSize(*args, **kwargs)

    def IsEmpty(*args, **kwargs):
        """IsEmpty(self) -> bool"""
        return __core.Rect_IsEmpty(*args, **kwargs)

    def GetTopLeft(*args, **kwargs):
        """GetTopLeft(self) -> Point"""
        return __core.Rect_GetTopLeft(*args, **kwargs)

    def SetTopLeft(*args, **kwargs):
        """SetTopLeft(self, Point p)"""
        return __core.Rect_SetTopLeft(*args, **kwargs)

    def GetBottomRight(*args, **kwargs):
        """GetBottomRight(self) -> Point"""
        return __core.Rect_GetBottomRight(*args, **kwargs)

    def SetBottomRight(*args, **kwargs):
        """SetBottomRight(self, Point p)"""
        return __core.Rect_SetBottomRight(*args, **kwargs)

    def GetTopRight(*args, **kwargs):
        """GetTopRight(self) -> Point"""
        return __core.Rect_GetTopRight(*args, **kwargs)

    def SetTopRight(*args, **kwargs):
        """SetTopRight(self, Point p)"""
        return __core.Rect_SetTopRight(*args, **kwargs)

    def GetBottomLeft(*args, **kwargs):
        """GetBottomLeft(self) -> Point"""
        return __core.Rect_GetBottomLeft(*args, **kwargs)

    def SetBottomLeft(*args, **kwargs):
        """SetBottomLeft(self, Point p)"""
        return __core.Rect_SetBottomLeft(*args, **kwargs)

    def GetLeft(*args, **kwargs):
        """GetLeft(self) -> int"""
        return __core.Rect_GetLeft(*args, **kwargs)

    def GetTop(*args, **kwargs):
        """GetTop(self) -> int"""
        return __core.Rect_GetTop(*args, **kwargs)

    def GetBottom(*args, **kwargs):
        """GetBottom(self) -> int"""
        return __core.Rect_GetBottom(*args, **kwargs)

    def GetRight(*args, **kwargs):
        """GetRight(self) -> int"""
        return __core.Rect_GetRight(*args, **kwargs)

    def SetLeft(*args, **kwargs):
        """SetLeft(self, int left)"""
        return __core.Rect_SetLeft(*args, **kwargs)

    def SetRight(*args, **kwargs):
        """SetRight(self, int right)"""
        return __core.Rect_SetRight(*args, **kwargs)

    def SetTop(*args, **kwargs):
        """SetTop(self, int top)"""
        return __core.Rect_SetTop(*args, **kwargs)

    def SetBottom(*args, **kwargs):
        """SetBottom(self, int bottom)"""
        return __core.Rect_SetBottom(*args, **kwargs)

    position = property(GetPosition, SetPosition)
    size = property(GetSize, SetSize)
    left = property(GetLeft, SetLeft)
    right = property(GetRight, SetRight)
    top = property(GetTop, SetTop)
    bottom = property(GetBottom, SetBottom)

    def Inflate(*args, **kwargs):
        """
        Inflate(self, int dx, int dy) -> Rect

        Increases the size of the rectangle.

        The left border is moved farther left and the right border is moved
        farther right by ``dx``. The upper border is moved farther up and the
        bottom border is moved farther down by ``dy``. (Note the the width and
        height of the rectangle thus change by ``2*dx`` and ``2*dy``,
        respectively.) If one or both of ``dx`` and ``dy`` are negative, the
        opposite happens: the rectangle size decreases in the respective
        direction.

        The change is made to the rectangle inplace, if instead you need a
        copy that is inflated, preserving the original then make the copy
        first::

            copy = wx.Rect(*original)
            copy.Inflate(10,15)


        """
        return __core.Rect_Inflate(*args, **kwargs)

    def Deflate(*args, **kwargs):
        """
        Deflate(self, int dx, int dy) -> Rect

        Decrease the rectangle size. This method is the opposite of `Inflate`
        in that Deflate(a,b) is equivalent to Inflate(-a,-b).  Please refer to
        `Inflate` for a full description.
        """
        return __core.Rect_Deflate(*args, **kwargs)

    def OffsetXY(*args, **kwargs):
        """
        OffsetXY(self, int dx, int dy)

        Moves the rectangle by the specified offset. If dx is positive, the
        rectangle is moved to the right, if dy is positive, it is moved to the
        bottom, otherwise it is moved to the left or top respectively.
        """
        return __core.Rect_OffsetXY(*args, **kwargs)

    def Offset(*args, **kwargs):
        """
        Offset(self, Point pt)

        Same as `OffsetXY` but uses dx,dy from Point
        """
        return __core.Rect_Offset(*args, **kwargs)

    def Intersect(*args, **kwargs):
        """
        Intersect(self, Rect rect) -> Rect

        Returns the intersectsion of this rectangle and rect.
        """
        return __core.Rect_Intersect(*args, **kwargs)

    def Union(*args, **kwargs):
        """
        Union(self, Rect rect) -> Rect

        Returns the union of this rectangle and rect.
        """
        return __core.Rect_Union(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Test for equality of wx.Rect objects.
        """
        return __core.Rect___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Test for inequality of wx.Rect objects.
        """
        return __core.Rect___ne__(*args, **kwargs)

    def __add__(*args, **kwargs):
        """
        __add__(self, Rect rect) -> Rect

        Add rect's proprties to this and return the result.
        """
        return __core.Rect___add__(*args, **kwargs)

    def __mul__(*args, **kwargs):
        """
        __mul__(self, Rect rect) -> Rect

        Calculate the intersection of the rectangles and return the result.
        """
        return __core.Rect___mul__(*args, **kwargs)

    def __iadd__(*args, **kwargs):
        """
        __iadd__(self, Rect rect) -> Rect

        Add the properties of rect to this rectangle, updating this rectangle.
        """
        return __core.Rect___iadd__(*args, **kwargs)

    def ContainsXY(*args, **kwargs):
        """
        ContainsXY(self, int x, int y) -> bool

        Return True if the point is inside the rect.
        """
        return __core.Rect_ContainsXY(*args, **kwargs)

    def Contains(*args, **kwargs):
        """
        Contains(self, Point pt) -> bool

        Return True if the point is inside the rect.
        """
        return __core.Rect_Contains(*args, **kwargs)

    def ContainsRect(*args, **kwargs):
        """
        ContainsRect(self, Rect rect) -> bool

        Returns ``True`` if the given rectangle is completely inside this
        rectangle or touches its boundary.
        """
        return __core.Rect_ContainsRect(*args, **kwargs)

    #Inside = wx.deprecated(Contains, "Use `Contains` instead.")
    #InsideXY = wx.deprecated(ContainsXY, "Use `ContainsXY` instead.")
    #InsideRect = wx.deprecated(ContainsRect, "Use `ContainsRect` instead.")
    Inside = Contains
    InsideXY = ContainsXY
    InsideRect = ContainsRect

    def Intersects(*args, **kwargs):
        """
        Intersects(self, Rect rect) -> bool

        Returns True if the rectangles have a non empty intersection.
        """
        return __core.Rect_Intersects(*args, **kwargs)

    def CenterIn(*args, **kwargs):
        """
        CenterIn(self, Rect r, int dir=BOTH) -> Rect

        Center this rectangle within the one passed to the method, which is
        usually, but not necessarily, the larger one.
        """
        return __core.Rect_CenterIn(*args, **kwargs)

    CentreIn = CenterIn 
    x = property(__core.Rect_x_get, __core.Rect_x_set)
    y = property(__core.Rect_y_get, __core.Rect_y_set)
    width = property(__core.Rect_width_get, __core.Rect_width_set)
    height = property(__core.Rect_height_get, __core.Rect_height_set)
    def Set(*args, **kwargs):
        """
        Set(self, int x=0, int y=0, int width=0, int height=0)

        Set all rectangle properties.
        """
        return __core.Rect_Set(*args, **kwargs)

    def Get(*args, **kwargs):
        """
        Get() -> (x,y,width,height)

        Return the rectangle properties as a tuple.
        """
        return __core.Rect_Get(*args, **kwargs)

    asTuple = wx.deprecated(Get, "asTuple is deprecated, use `Get` instead")
    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'wx.Rect'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.x = val
        elif index == 1: self.y = val
        elif index == 2: self.width = val
        elif index == 3: self.height = val
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0,0,0,0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (wx.Rect, self.Get())

    Bottom = property(GetBottom,SetBottom,doc="See `GetBottom` and `SetBottom`") 
    BottomRight = property(GetBottomRight,SetBottomRight,doc="See `GetBottomRight` and `SetBottomRight`") 
    BottomLeft = property(GetBottomLeft,SetBottomLeft,doc="See `GetBottomLeft` and `SetBottomLeft`") 
    Height = property(GetHeight,SetHeight,doc="See `GetHeight` and `SetHeight`") 
    Left = property(GetLeft,SetLeft,doc="See `GetLeft` and `SetLeft`") 
    Position = property(GetPosition,SetPosition,doc="See `GetPosition` and `SetPosition`") 
    Right = property(GetRight,SetRight,doc="See `GetRight` and `SetRight`") 
    Size = property(GetSize,SetSize,doc="See `GetSize` and `SetSize`") 
    Top = property(GetTop,SetTop,doc="See `GetTop` and `SetTop`") 
    TopLeft = property(GetTopLeft,SetTopLeft,doc="See `GetTopLeft` and `SetTopLeft`") 
    TopRight = property(GetTopRight,SetTopRight,doc="See `GetTopRight` and `SetTopRight`") 
    Width = property(GetWidth,SetWidth,doc="See `GetWidth` and `SetWidth`") 
    X = property(GetX,SetX,doc="See `GetX` and `SetX`") 
    Y = property(GetY,SetY,doc="See `GetY` and `SetY`") 
    Empty = property(IsEmpty,doc="See `IsEmpty`") 
__core.Rect_swigregister(Rect)

def RectPP(*args, **kwargs):
    """
    RectPP(Point topLeft, Point bottomRight) -> Rect

    Create a new Rect object from Points representing two corners.
    """
    val = __core.new_RectPP(*args, **kwargs)
    return val

def RectPS(*args, **kwargs):
    """
    RectPS(Point pos, Size size) -> Rect

    Create a new Rect from a position and size.
    """
    val = __core.new_RectPS(*args, **kwargs)
    return val

def RectS(*args, **kwargs):
    """
    RectS(Size size) -> Rect

    Create a new Rect from a size only.
    """
    val = __core.new_RectS(*args, **kwargs)
    return val


def IntersectRect(*args, **kwargs):
  """
    IntersectRect(Rect r1, Rect r2) -> Rect

    Calculate and return the intersection of r1 and r2.
    """
  return __core.IntersectRect(*args, **kwargs)
#---------------------------------------------------------------------------

class Point2D(object):
    """
    wx.Point2Ds represent a point or a vector in a 2d coordinate system
    with floating point values.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, double x=0.0, double y=0.0) -> Point2D

        Create a w.Point2D object.
        """
        this = __core.new_Point2D(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Point2D
    __del__ = lambda self : None;
    def GetFloor(*args, **kwargs):
        """
        GetFloor() -> (x,y)

        Convert to integer
        """
        return __core.Point2D_GetFloor(*args, **kwargs)

    def GetRounded(*args, **kwargs):
        """
        GetRounded() -> (x,y)

        Convert to integer
        """
        return __core.Point2D_GetRounded(*args, **kwargs)

    def GetVectorLength(*args, **kwargs):
        """GetVectorLength(self) -> double"""
        return __core.Point2D_GetVectorLength(*args, **kwargs)

    def GetVectorAngle(*args, **kwargs):
        """GetVectorAngle(self) -> double"""
        return __core.Point2D_GetVectorAngle(*args, **kwargs)

    def SetVectorLength(*args, **kwargs):
        """SetVectorLength(self, double length)"""
        return __core.Point2D_SetVectorLength(*args, **kwargs)

    def SetVectorAngle(*args, **kwargs):
        """SetVectorAngle(self, double degrees)"""
        return __core.Point2D_SetVectorAngle(*args, **kwargs)

    def SetPolarCoordinates(self, angle, length):
        self.SetVectorLength(length)
        self.SetVectorAngle(angle)
    def Normalize(self):
        self.SetVectorLength(1.0)

    def GetDistance(*args, **kwargs):
        """GetDistance(self, Point2D pt) -> double"""
        return __core.Point2D_GetDistance(*args, **kwargs)

    def GetDistanceSquare(*args, **kwargs):
        """GetDistanceSquare(self, Point2D pt) -> double"""
        return __core.Point2D_GetDistanceSquare(*args, **kwargs)

    def GetDotProduct(*args, **kwargs):
        """GetDotProduct(self, Point2D vec) -> double"""
        return __core.Point2D_GetDotProduct(*args, **kwargs)

    def GetCrossProduct(*args, **kwargs):
        """GetCrossProduct(self, Point2D vec) -> double"""
        return __core.Point2D_GetCrossProduct(*args, **kwargs)

    def __neg__(*args, **kwargs):
        """
        __neg__(self) -> Point2D

        the reflection of this point
        """
        return __core.Point2D___neg__(*args, **kwargs)

    def __iadd__(*args, **kwargs):
        """__iadd__(self, Point2D pt) -> Point2D"""
        return __core.Point2D___iadd__(*args, **kwargs)

    def __isub__(*args, **kwargs):
        """__isub__(self, Point2D pt) -> Point2D"""
        return __core.Point2D___isub__(*args, **kwargs)

    def __imul__(*args):
        """__imul__(self, Point2D pt) -> Point2D"""
        return __core.Point2D___imul__(*args)

    def __idiv__(*args):
        """__idiv__(self, wxPoint2DDouble pt) -> Point2D"""
        return __core.Point2D___idiv__(*args)

    def __add__(*args):
        """__add__(self, Point2D pt) -> Point2D"""
        return __core.Point2D___add__(*args)

    def __sub__(*args):
        """__sub__(self, Point2D pt) -> Point2D"""
        return __core.Point2D___sub__(*args)

    def __mul__(*args):
        """
        __mul__(self, Point2D pt) -> Point2D
        __mul__(self, double n) -> Point2D
        """
        return __core.Point2D___mul__(*args)

    def __div__(*args):
        """
        __div__(self, Point2D pt) -> Point2D
        __div__(self, double n) -> Point2D
        """
        return __core.Point2D___div__(*args)

    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Test for equality of wx.Point2D objects.
        """
        return __core.Point2D___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Test for inequality of wx.Point2D objects.
        """
        return __core.Point2D___ne__(*args, **kwargs)

    x = property(__core.Point2D_x_get, __core.Point2D_x_set)
    y = property(__core.Point2D_y_get, __core.Point2D_y_set)
    def Set(*args, **kwargs):
        """Set(self, double x=0, double y=0)"""
        return __core.Point2D_Set(*args, **kwargs)

    def Get(*args, **kwargs):
        """
        Get() -> (x,y)

        Return x and y properties as a tuple.
        """
        return __core.Point2D_Get(*args, **kwargs)

    asTuple = wx.deprecated(Get, "asTuple is deprecated, use `Get` instead")
    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'wx.Point2D'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.x = val
        elif index == 1: self.y = val
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0.0, 0.0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (wx.Point2D, self.Get())

    Floor = property(GetFloor,doc="See `GetFloor`") 
    Rounded = property(GetRounded,doc="See `GetRounded`") 
    VectorAngle = property(GetVectorAngle,SetVectorAngle,doc="See `GetVectorAngle` and `SetVectorAngle`") 
    VectorLength = property(GetVectorLength,SetVectorLength,doc="See `GetVectorLength` and `SetVectorLength`") 
__core.Point2D_swigregister(Point2D)

def Point2DCopy(*args, **kwargs):
    """
    Point2DCopy(Point2D pt) -> Point2D

    Create a w.Point2D object.
    """
    val = __core.new_Point2DCopy(*args, **kwargs)
    return val

def Point2DFromPoint(*args, **kwargs):
    """
    Point2DFromPoint(Point pt) -> Point2D

    Create a w.Point2D object.
    """
    val = __core.new_Point2DFromPoint(*args, **kwargs)
    return val

#---------------------------------------------------------------------------

Inside = __core.Inside
OutLeft = __core.OutLeft
OutRight = __core.OutRight
OutTop = __core.OutTop
OutBottom = __core.OutBottom
class Rect2D(object):
    """
    wx.Rect2D is a rectangle, with position and size, in a 2D coordinate system
    with floating point component values.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Double x=0.0, Double y=0.0, Double w=0.0, Double h=0.0) -> Rect2D

        wx.Rect2D is a rectangle, with position and size, in a 2D coordinate system
        with floating point component values.
        """
        this = __core.new_Rect2D(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Rect2D
    __del__ = lambda self : None;
    def GetPosition(*args, **kwargs):
        """GetPosition(self) -> Point2D"""
        return __core.Rect2D_GetPosition(*args, **kwargs)

    def GetSize(*args, **kwargs):
        """GetSize(self) -> Size"""
        return __core.Rect2D_GetSize(*args, **kwargs)

    def GetLeft(*args, **kwargs):
        """GetLeft(self) -> Double"""
        return __core.Rect2D_GetLeft(*args, **kwargs)

    def SetLeft(*args, **kwargs):
        """SetLeft(self, Double n)"""
        return __core.Rect2D_SetLeft(*args, **kwargs)

    def MoveLeftTo(*args, **kwargs):
        """MoveLeftTo(self, Double n)"""
        return __core.Rect2D_MoveLeftTo(*args, **kwargs)

    def GetTop(*args, **kwargs):
        """GetTop(self) -> Double"""
        return __core.Rect2D_GetTop(*args, **kwargs)

    def SetTop(*args, **kwargs):
        """SetTop(self, Double n)"""
        return __core.Rect2D_SetTop(*args, **kwargs)

    def MoveTopTo(*args, **kwargs):
        """MoveTopTo(self, Double n)"""
        return __core.Rect2D_MoveTopTo(*args, **kwargs)

    def GetBottom(*args, **kwargs):
        """GetBottom(self) -> Double"""
        return __core.Rect2D_GetBottom(*args, **kwargs)

    def SetBottom(*args, **kwargs):
        """SetBottom(self, Double n)"""
        return __core.Rect2D_SetBottom(*args, **kwargs)

    def MoveBottomTo(*args, **kwargs):
        """MoveBottomTo(self, Double n)"""
        return __core.Rect2D_MoveBottomTo(*args, **kwargs)

    def GetRight(*args, **kwargs):
        """GetRight(self) -> Double"""
        return __core.Rect2D_GetRight(*args, **kwargs)

    def SetRight(*args, **kwargs):
        """SetRight(self, Double n)"""
        return __core.Rect2D_SetRight(*args, **kwargs)

    def MoveRightTo(*args, **kwargs):
        """MoveRightTo(self, Double n)"""
        return __core.Rect2D_MoveRightTo(*args, **kwargs)

    def GetLeftTop(*args, **kwargs):
        """GetLeftTop(self) -> Point2D"""
        return __core.Rect2D_GetLeftTop(*args, **kwargs)

    def SetLeftTop(*args, **kwargs):
        """SetLeftTop(self, Point2D pt)"""
        return __core.Rect2D_SetLeftTop(*args, **kwargs)

    def MoveLeftTopTo(*args, **kwargs):
        """MoveLeftTopTo(self, Point2D pt)"""
        return __core.Rect2D_MoveLeftTopTo(*args, **kwargs)

    def GetLeftBottom(*args, **kwargs):
        """GetLeftBottom(self) -> Point2D"""
        return __core.Rect2D_GetLeftBottom(*args, **kwargs)

    def SetLeftBottom(*args, **kwargs):
        """SetLeftBottom(self, Point2D pt)"""
        return __core.Rect2D_SetLeftBottom(*args, **kwargs)

    def MoveLeftBottomTo(*args, **kwargs):
        """MoveLeftBottomTo(self, Point2D pt)"""
        return __core.Rect2D_MoveLeftBottomTo(*args, **kwargs)

    def GetRightTop(*args, **kwargs):
        """GetRightTop(self) -> Point2D"""
        return __core.Rect2D_GetRightTop(*args, **kwargs)

    def SetRightTop(*args, **kwargs):
        """SetRightTop(self, Point2D pt)"""
        return __core.Rect2D_SetRightTop(*args, **kwargs)

    def MoveRightTopTo(*args, **kwargs):
        """MoveRightTopTo(self, Point2D pt)"""
        return __core.Rect2D_MoveRightTopTo(*args, **kwargs)

    def GetRightBottom(*args, **kwargs):
        """GetRightBottom(self) -> Point2D"""
        return __core.Rect2D_GetRightBottom(*args, **kwargs)

    def SetRightBottom(*args, **kwargs):
        """SetRightBottom(self, Point2D pt)"""
        return __core.Rect2D_SetRightBottom(*args, **kwargs)

    def MoveRightBottomTo(*args, **kwargs):
        """MoveRightBottomTo(self, Point2D pt)"""
        return __core.Rect2D_MoveRightBottomTo(*args, **kwargs)

    def GetCentre(*args, **kwargs):
        """GetCentre(self) -> Point2D"""
        return __core.Rect2D_GetCentre(*args, **kwargs)

    def SetCentre(*args, **kwargs):
        """SetCentre(self, Point2D pt)"""
        return __core.Rect2D_SetCentre(*args, **kwargs)

    def MoveCentreTo(*args, **kwargs):
        """MoveCentreTo(self, Point2D pt)"""
        return __core.Rect2D_MoveCentreTo(*args, **kwargs)

    def GetOutcode(*args, **kwargs):
        """GetOutcode(self, Point2D pt) -> int"""
        return __core.Rect2D_GetOutcode(*args, **kwargs)

    def Contains(*args, **kwargs):
        """Contains(self, Point2D pt) -> bool"""
        return __core.Rect2D_Contains(*args, **kwargs)

    def ContainsRect(*args, **kwargs):
        """ContainsRect(self, Rect2D rect) -> bool"""
        return __core.Rect2D_ContainsRect(*args, **kwargs)

    def IsEmpty(*args, **kwargs):
        """IsEmpty(self) -> bool"""
        return __core.Rect2D_IsEmpty(*args, **kwargs)

    def HaveEqualSize(*args, **kwargs):
        """HaveEqualSize(self, Rect2D rect) -> bool"""
        return __core.Rect2D_HaveEqualSize(*args, **kwargs)

    def Inset(*args):
        """
        Inset(self, Double x, Double y)
        Inset(self, Double left, Double top, Double right, Double bottom)
        """
        return __core.Rect2D_Inset(*args)

    def Offset(*args, **kwargs):
        """Offset(self, Point2D pt)"""
        return __core.Rect2D_Offset(*args, **kwargs)

    def ConstrainTo(*args, **kwargs):
        """ConstrainTo(self, Rect2D rect)"""
        return __core.Rect2D_ConstrainTo(*args, **kwargs)

    def Interpolate(*args, **kwargs):
        """Interpolate(self, int widthfactor, int heightfactor) -> Point2D"""
        return __core.Rect2D_Interpolate(*args, **kwargs)

    def Intersect(*args, **kwargs):
        """Intersect(self, Rect2D otherRect)"""
        return __core.Rect2D_Intersect(*args, **kwargs)

    def CreateIntersection(*args, **kwargs):
        """CreateIntersection(self, Rect2D otherRect) -> Rect2D"""
        return __core.Rect2D_CreateIntersection(*args, **kwargs)

    def Intersects(*args, **kwargs):
        """Intersects(self, Rect2D rect) -> bool"""
        return __core.Rect2D_Intersects(*args, **kwargs)

    def Union(*args, **kwargs):
        """Union(self, Rect2D otherRect)"""
        return __core.Rect2D_Union(*args, **kwargs)

    def CreateUnion(*args, **kwargs):
        """CreateUnion(self, Rect2D otherRect) -> Rect2D"""
        return __core.Rect2D_CreateUnion(*args, **kwargs)

    def Scale(*args):
        """
        Scale(self, Double f)
        Scale(self, int num, int denum)
        """
        return __core.Rect2D_Scale(*args)

    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Test for equality of wx.Rect2D objects.
        """
        return __core.Rect2D___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Test for inequality of wx.Rect2D objects.
        """
        return __core.Rect2D___ne__(*args, **kwargs)

    x = property(__core.Rect2D_x_get, __core.Rect2D_x_set)
    y = property(__core.Rect2D_y_get, __core.Rect2D_y_set)
    width = property(__core.Rect2D_width_get, __core.Rect2D_width_set)
    height = property(__core.Rect2D_height_get, __core.Rect2D_height_set)
    def Set(*args, **kwargs):
        """Set(self, Double x=0, Double y=0, Double width=0, Double height=0)"""
        return __core.Rect2D_Set(*args, **kwargs)

    def Get(*args, **kwargs):
        """
        Get() -> (x,y, width, height)

        Return x, y, width and height y properties as a tuple.
        """
        return __core.Rect2D_Get(*args, **kwargs)

    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'wx.Rect2D'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.x = val
        elif index == 1: self.y = val
        elif index == 2: self.width = val
        elif index == 3: self.height = val                        
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0.0, 0.0, 0.0, 0.0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (wx.Rect2D, self.Get())

__core.Rect2D_swigregister(Rect2D)

class Position(object):
    """Proxy of C++ Position class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, int row=0, int col=0) -> Position"""
        this = __core.new_Position(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Position
    __del__ = lambda self : None;
    def GetRow(*args, **kwargs):
        """GetRow(self) -> int"""
        return __core.Position_GetRow(*args, **kwargs)

    def GetColumn(*args, **kwargs):
        """GetColumn(self) -> int"""
        return __core.Position_GetColumn(*args, **kwargs)

    def GetCol(*args, **kwargs):
        """GetCol(self) -> int"""
        return __core.Position_GetCol(*args, **kwargs)

    def SetRow(*args, **kwargs):
        """SetRow(self, int row)"""
        return __core.Position_SetRow(*args, **kwargs)

    def SetColumn(*args, **kwargs):
        """SetColumn(self, int column)"""
        return __core.Position_SetColumn(*args, **kwargs)

    def SetCol(*args, **kwargs):
        """SetCol(self, int column)"""
        return __core.Position_SetCol(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Test for equality of wx.Position objects.
        """
        return __core.Position___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Test for inequality of wx.Position objects.
        """
        return __core.Position___ne__(*args, **kwargs)

    def __add__(*args):
        """
        __add__(self, Position p) -> Position
        __add__(self, Size s) -> Position
        """
        return __core.Position___add__(*args)

    def __sub__(*args):
        """
        __sub__(self, Position p) -> Position
        __sub__(self, Size s) -> Position
        """
        return __core.Position___sub__(*args)

    row = property(GetRow,SetRow) 
    col = property(GetCol,SetCol) 
__core.Position_swigregister(Position)

#---------------------------------------------------------------------------

FromStart = __core.FromStart
FromCurrent = __core.FromCurrent
FromEnd = __core.FromEnd
class InputStream(object):
    """Proxy of C++ InputStream class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, PyObject p) -> InputStream"""
        this = __core.new_InputStream(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_InputStream
    __del__ = lambda self : None;
    def close(*args, **kwargs):
        """close(self)"""
        return __core.InputStream_close(*args, **kwargs)

    def flush(*args, **kwargs):
        """flush(self)"""
        return __core.InputStream_flush(*args, **kwargs)

    def eof(*args, **kwargs):
        """eof(self) -> bool"""
        return __core.InputStream_eof(*args, **kwargs)

    def read(*args, **kwargs):
        """read(self, int size=-1) -> PyObject"""
        return __core.InputStream_read(*args, **kwargs)

    def readline(*args, **kwargs):
        """readline(self, int size=-1) -> PyObject"""
        return __core.InputStream_readline(*args, **kwargs)

    def readlines(*args, **kwargs):
        """readlines(self, int sizehint=-1) -> PyObject"""
        return __core.InputStream_readlines(*args, **kwargs)

    def seek(*args, **kwargs):
        """seek(self, int offset, int whence=0)"""
        return __core.InputStream_seek(*args, **kwargs)

    def tell(*args, **kwargs):
        """tell(self) -> int"""
        return __core.InputStream_tell(*args, **kwargs)

    def Peek(*args, **kwargs):
        """Peek(self) -> char"""
        return __core.InputStream_Peek(*args, **kwargs)

    def GetC(*args, **kwargs):
        """GetC(self) -> char"""
        return __core.InputStream_GetC(*args, **kwargs)

    def LastRead(*args, **kwargs):
        """LastRead(self) -> size_t"""
        return __core.InputStream_LastRead(*args, **kwargs)

    def CanRead(*args, **kwargs):
        """CanRead(self) -> bool"""
        return __core.InputStream_CanRead(*args, **kwargs)

    def Eof(*args, **kwargs):
        """Eof(self) -> bool"""
        return __core.InputStream_Eof(*args, **kwargs)

    def Ungetch(*args, **kwargs):
        """Ungetch(self, char c) -> bool"""
        return __core.InputStream_Ungetch(*args, **kwargs)

    def SeekI(*args, **kwargs):
        """SeekI(self, long pos, int mode=FromStart) -> long"""
        return __core.InputStream_SeekI(*args, **kwargs)

    def TellI(*args, **kwargs):
        """TellI(self) -> long"""
        return __core.InputStream_TellI(*args, **kwargs)

__core.InputStream_swigregister(InputStream)
DefaultPosition = cvar.DefaultPosition
DefaultSize = cvar.DefaultSize

class OutputStream(object):
    """Proxy of C++ OutputStream class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, PyObject p) -> OutputStream"""
        this = __core.new_OutputStream(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_OutputStream
    __del__ = lambda self : None;
    def close(*args, **kwargs):
        """close(self)"""
        return __core.OutputStream_close(*args, **kwargs)

    def flush(*args, **kwargs):
        """flush(self)"""
        return __core.OutputStream_flush(*args, **kwargs)

    def eof(*args, **kwargs):
        """eof(self) -> bool"""
        return __core.OutputStream_eof(*args, **kwargs)

    def seek(*args, **kwargs):
        """seek(self, int offset, int whence=0)"""
        return __core.OutputStream_seek(*args, **kwargs)

    def tell(*args, **kwargs):
        """tell(self) -> int"""
        return __core.OutputStream_tell(*args, **kwargs)

    def write(*args, **kwargs):
        """write(self, PyObject data)"""
        return __core.OutputStream_write(*args, **kwargs)

    def PutC(*args, **kwargs):
        """PutC(self, char c)"""
        return __core.OutputStream_PutC(*args, **kwargs)

    def LastWrite(*args, **kwargs):
        """LastWrite(self) -> size_t"""
        return __core.OutputStream_LastWrite(*args, **kwargs)

    def SeekO(*args, **kwargs):
        """SeekO(self, unsigned long pos, int mode=FromStart) -> unsigned long"""
        return __core.OutputStream_SeekO(*args, **kwargs)

    def TellO(*args, **kwargs):
        """TellO(self) -> unsigned long"""
        return __core.OutputStream_TellO(*args, **kwargs)

__core.OutputStream_swigregister(OutputStream)

#---------------------------------------------------------------------------

class FSFile(Object):
    """Proxy of C++ FSFile class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, InputStream stream, String loc, String mimetype, String anchor, 
            DateTime modif) -> FSFile
        """
        this = __core.new_FSFile(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_FSFile
    __del__ = lambda self : None;
    def GetStream(*args, **kwargs):
        """GetStream(self) -> InputStream"""
        return __core.FSFile_GetStream(*args, **kwargs)

    def DetachStream(*args, **kwargs):
        """DetachStream(self)"""
        return __core.FSFile_DetachStream(*args, **kwargs)

    def GetMimeType(*args, **kwargs):
        """GetMimeType(self) -> String"""
        return __core.FSFile_GetMimeType(*args, **kwargs)

    def GetLocation(*args, **kwargs):
        """GetLocation(self) -> String"""
        return __core.FSFile_GetLocation(*args, **kwargs)

    def GetAnchor(*args, **kwargs):
        """GetAnchor(self) -> String"""
        return __core.FSFile_GetAnchor(*args, **kwargs)

    def GetModificationTime(*args, **kwargs):
        """GetModificationTime(self) -> DateTime"""
        return __core.FSFile_GetModificationTime(*args, **kwargs)

    Anchor = property(GetAnchor,doc="See `GetAnchor`") 
    Location = property(GetLocation,doc="See `GetLocation`") 
    MimeType = property(GetMimeType,doc="See `GetMimeType`") 
    ModificationTime = property(GetModificationTime,doc="See `GetModificationTime`") 
    Stream = property(GetStream,doc="See `GetStream`") 
__core.FSFile_swigregister(FSFile)

class CPPFileSystemHandler(object):
    """Proxy of C++ CPPFileSystemHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_CPPFileSystemHandler
    __del__ = lambda self : None;
__core.CPPFileSystemHandler_swigregister(CPPFileSystemHandler)

class FileSystemHandler(CPPFileSystemHandler):
    """Proxy of C++ FileSystemHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> FileSystemHandler"""
        this = __core.new_FileSystemHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        FileSystemHandler._setCallbackInfo(self, self, FileSystemHandler)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return __core.FileSystemHandler__setCallbackInfo(*args, **kwargs)

    def CanOpen(*args, **kwargs):
        """CanOpen(self, String location) -> bool"""
        return __core.FileSystemHandler_CanOpen(*args, **kwargs)

    def OpenFile(*args, **kwargs):
        """OpenFile(self, FileSystem fs, String location) -> FSFile"""
        return __core.FileSystemHandler_OpenFile(*args, **kwargs)

    def FindFirst(*args, **kwargs):
        """FindFirst(self, String spec, int flags=0) -> String"""
        return __core.FileSystemHandler_FindFirst(*args, **kwargs)

    def FindNext(*args, **kwargs):
        """FindNext(self) -> String"""
        return __core.FileSystemHandler_FindNext(*args, **kwargs)

    def GetProtocol(*args, **kwargs):
        """GetProtocol(String location) -> String"""
        return __core.FileSystemHandler_GetProtocol(*args, **kwargs)

    GetProtocol = staticmethod(GetProtocol)
    def GetLeftLocation(*args, **kwargs):
        """GetLeftLocation(String location) -> String"""
        return __core.FileSystemHandler_GetLeftLocation(*args, **kwargs)

    GetLeftLocation = staticmethod(GetLeftLocation)
    def GetAnchor(*args, **kwargs):
        """GetAnchor(String location) -> String"""
        return __core.FileSystemHandler_GetAnchor(*args, **kwargs)

    GetAnchor = staticmethod(GetAnchor)
    def GetRightLocation(*args, **kwargs):
        """GetRightLocation(String location) -> String"""
        return __core.FileSystemHandler_GetRightLocation(*args, **kwargs)

    GetRightLocation = staticmethod(GetRightLocation)
    def GetMimeTypeFromExt(*args, **kwargs):
        """GetMimeTypeFromExt(String location) -> String"""
        return __core.FileSystemHandler_GetMimeTypeFromExt(*args, **kwargs)

    GetMimeTypeFromExt = staticmethod(GetMimeTypeFromExt)
__core.FileSystemHandler_swigregister(FileSystemHandler)

def FileSystemHandler_GetProtocol(*args, **kwargs):
  """FileSystemHandler_GetProtocol(String location) -> String"""
  return __core.FileSystemHandler_GetProtocol(*args, **kwargs)

def FileSystemHandler_GetLeftLocation(*args, **kwargs):
  """FileSystemHandler_GetLeftLocation(String location) -> String"""
  return __core.FileSystemHandler_GetLeftLocation(*args, **kwargs)

def FileSystemHandler_GetAnchor(*args, **kwargs):
  """FileSystemHandler_GetAnchor(String location) -> String"""
  return __core.FileSystemHandler_GetAnchor(*args, **kwargs)

def FileSystemHandler_GetRightLocation(*args, **kwargs):
  """FileSystemHandler_GetRightLocation(String location) -> String"""
  return __core.FileSystemHandler_GetRightLocation(*args, **kwargs)

def FileSystemHandler_GetMimeTypeFromExt(*args, **kwargs):
  """FileSystemHandler_GetMimeTypeFromExt(String location) -> String"""
  return __core.FileSystemHandler_GetMimeTypeFromExt(*args, **kwargs)

class FileSystem(Object):
    """Proxy of C++ FileSystem class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> FileSystem"""
        this = __core.new_FileSystem(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_FileSystem
    __del__ = lambda self : None;
    def ChangePathTo(*args, **kwargs):
        """ChangePathTo(self, String location, bool is_dir=False)"""
        return __core.FileSystem_ChangePathTo(*args, **kwargs)

    def GetPath(*args, **kwargs):
        """GetPath(self) -> String"""
        return __core.FileSystem_GetPath(*args, **kwargs)

    def OpenFile(*args, **kwargs):
        """OpenFile(self, String location) -> FSFile"""
        return __core.FileSystem_OpenFile(*args, **kwargs)

    def FindFirst(*args, **kwargs):
        """FindFirst(self, String spec, int flags=0) -> String"""
        return __core.FileSystem_FindFirst(*args, **kwargs)

    def FindNext(*args, **kwargs):
        """FindNext(self) -> String"""
        return __core.FileSystem_FindNext(*args, **kwargs)

    def AddHandler(*args, **kwargs):
        """AddHandler(CPPFileSystemHandler handler)"""
        return __core.FileSystem_AddHandler(*args, **kwargs)

    AddHandler = staticmethod(AddHandler)
    def RemoveHandler(*args, **kwargs):
        """RemoveHandler(CPPFileSystemHandler handler) -> CPPFileSystemHandler"""
        return __core.FileSystem_RemoveHandler(*args, **kwargs)

    RemoveHandler = staticmethod(RemoveHandler)
    def CleanUpHandlers(*args, **kwargs):
        """CleanUpHandlers()"""
        return __core.FileSystem_CleanUpHandlers(*args, **kwargs)

    CleanUpHandlers = staticmethod(CleanUpHandlers)
    def FileNameToURL(*args, **kwargs):
        """FileNameToURL(String filename) -> String"""
        return __core.FileSystem_FileNameToURL(*args, **kwargs)

    FileNameToURL = staticmethod(FileNameToURL)
    def URLToFileName(*args, **kwargs):
        """URLToFileName(String url) -> String"""
        return __core.FileSystem_URLToFileName(*args, **kwargs)

    URLToFileName = staticmethod(URLToFileName)
    Path = property(GetPath,doc="See `GetPath`") 
__core.FileSystem_swigregister(FileSystem)

def FileSystem_AddHandler(*args, **kwargs):
  """FileSystem_AddHandler(CPPFileSystemHandler handler)"""
  return __core.FileSystem_AddHandler(*args, **kwargs)

def FileSystem_RemoveHandler(*args, **kwargs):
  """FileSystem_RemoveHandler(CPPFileSystemHandler handler) -> CPPFileSystemHandler"""
  return __core.FileSystem_RemoveHandler(*args, **kwargs)

def FileSystem_CleanUpHandlers(*args):
  """FileSystem_CleanUpHandlers()"""
  return __core.FileSystem_CleanUpHandlers(*args)

def FileSystem_FileNameToURL(*args, **kwargs):
  """FileSystem_FileNameToURL(String filename) -> String"""
  return __core.FileSystem_FileNameToURL(*args, **kwargs)

def FileSystem_URLToFileName(*args, **kwargs):
  """FileSystem_URLToFileName(String url) -> String"""
  return __core.FileSystem_URLToFileName(*args, **kwargs)

class InternetFSHandler(CPPFileSystemHandler):
    """Proxy of C++ InternetFSHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> InternetFSHandler"""
        this = __core.new_InternetFSHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def CanOpen(*args, **kwargs):
        """CanOpen(self, String location) -> bool"""
        return __core.InternetFSHandler_CanOpen(*args, **kwargs)

    def OpenFile(*args, **kwargs):
        """OpenFile(self, FileSystem fs, String location) -> FSFile"""
        return __core.InternetFSHandler_OpenFile(*args, **kwargs)

__core.InternetFSHandler_swigregister(InternetFSHandler)

class ZipFSHandler(CPPFileSystemHandler):
    """Proxy of C++ ZipFSHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> ZipFSHandler"""
        this = __core.new_ZipFSHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def CanOpen(*args, **kwargs):
        """CanOpen(self, String location) -> bool"""
        return __core.ZipFSHandler_CanOpen(*args, **kwargs)

    def OpenFile(*args, **kwargs):
        """OpenFile(self, FileSystem fs, String location) -> FSFile"""
        return __core.ZipFSHandler_OpenFile(*args, **kwargs)

    def FindFirst(*args, **kwargs):
        """FindFirst(self, String spec, int flags=0) -> String"""
        return __core.ZipFSHandler_FindFirst(*args, **kwargs)

    def FindNext(*args, **kwargs):
        """FindNext(self) -> String"""
        return __core.ZipFSHandler_FindNext(*args, **kwargs)

__core.ZipFSHandler_swigregister(ZipFSHandler)


def __wxMemoryFSHandler_AddFile_wxImage(*args, **kwargs):
  """__wxMemoryFSHandler_AddFile_wxImage(String filename, Image image, int type)"""
  return __core.__wxMemoryFSHandler_AddFile_wxImage(*args, **kwargs)

def __wxMemoryFSHandler_AddFile_wxBitmap(*args, **kwargs):
  """__wxMemoryFSHandler_AddFile_wxBitmap(String filename, Bitmap bitmap, int type)"""
  return __core.__wxMemoryFSHandler_AddFile_wxBitmap(*args, **kwargs)

def __wxMemoryFSHandler_AddFile_Data(*args, **kwargs):
  """__wxMemoryFSHandler_AddFile_Data(String filename, buffer data)"""
  return __core.__wxMemoryFSHandler_AddFile_Data(*args, **kwargs)
def MemoryFSHandler_AddFile(filename, dataItem, imgType=-1):
    """
    Add 'file' to the memory filesystem.  The dataItem parameter can
    either be a `wx.Bitmap`, `wx.Image` or a string that can contain
    arbitrary data.  If a bitmap or image is used then the imgType
    parameter should specify what kind of image file it should be
    written as, wx.BITMAP_TYPE_PNG, etc.
    """
    if isinstance(dataItem, wx.Image):
        __wxMemoryFSHandler_AddFile_wxImage(filename, dataItem, imgType)
    elif isinstance(dataItem, wx.Bitmap):
        __wxMemoryFSHandler_AddFile_wxBitmap(filename, dataItem, imgType)
    else:
        try:
            __wxMemoryFSHandler_AddFile_Data(filename, dataItem)
        except TypeError:
            raise TypeError, 'wx.Image, wx.Bitmap or buffer object expected'

class MemoryFSHandler(CPPFileSystemHandler):
    """Proxy of C++ MemoryFSHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> MemoryFSHandler"""
        this = __core.new_MemoryFSHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def RemoveFile(*args, **kwargs):
        """RemoveFile(String filename)"""
        return __core.MemoryFSHandler_RemoveFile(*args, **kwargs)

    RemoveFile = staticmethod(RemoveFile)
    AddFile = staticmethod(MemoryFSHandler_AddFile) 
    def AddFileWithMimeType(*args, **kwargs):
        """AddFileWithMimeType(String filename, buffer data, String mimetype)"""
        return __core.MemoryFSHandler_AddFileWithMimeType(*args, **kwargs)

    AddFileWithMimeType = staticmethod(AddFileWithMimeType)
    def CanOpen(*args, **kwargs):
        """CanOpen(self, String location) -> bool"""
        return __core.MemoryFSHandler_CanOpen(*args, **kwargs)

    def OpenFile(*args, **kwargs):
        """OpenFile(self, FileSystem fs, String location) -> FSFile"""
        return __core.MemoryFSHandler_OpenFile(*args, **kwargs)

    def FindFirst(*args, **kwargs):
        """FindFirst(self, String spec, int flags=0) -> String"""
        return __core.MemoryFSHandler_FindFirst(*args, **kwargs)

    def FindNext(*args, **kwargs):
        """FindNext(self) -> String"""
        return __core.MemoryFSHandler_FindNext(*args, **kwargs)

__core.MemoryFSHandler_swigregister(MemoryFSHandler)

def MemoryFSHandler_RemoveFile(*args, **kwargs):
  """MemoryFSHandler_RemoveFile(String filename)"""
  return __core.MemoryFSHandler_RemoveFile(*args, **kwargs)

def MemoryFSHandler_AddFileWithMimeType(*args, **kwargs):
  """MemoryFSHandler_AddFileWithMimeType(String filename, buffer data, String mimetype)"""
  return __core.MemoryFSHandler_AddFileWithMimeType(*args, **kwargs)

IMAGE_ALPHA_TRANSPARENT = __core.IMAGE_ALPHA_TRANSPARENT
IMAGE_ALPHA_THRESHOLD = __core.IMAGE_ALPHA_THRESHOLD
IMAGE_ALPHA_OPAQUE = __core.IMAGE_ALPHA_OPAQUE
IMAGE_QUALITY_NEAREST = __core.IMAGE_QUALITY_NEAREST
IMAGE_QUALITY_BILINEAR = __core.IMAGE_QUALITY_BILINEAR
IMAGE_QUALITY_BICUBIC = __core.IMAGE_QUALITY_BICUBIC
IMAGE_QUALITY_BOX_AVERAGE = __core.IMAGE_QUALITY_BOX_AVERAGE
IMAGE_QUALITY_NORMAL = __core.IMAGE_QUALITY_NORMAL
IMAGE_QUALITY_HIGH = __core.IMAGE_QUALITY_HIGH
#---------------------------------------------------------------------------

class ImageHandler(Object):
    """
    This is the base class for implementing image file loading/saving, and
    image creation from data. It is used within `wx.Image` and is not
    normally seen by the application.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def GetName(*args, **kwargs):
        """GetName(self) -> String"""
        return __core.ImageHandler_GetName(*args, **kwargs)

    def GetExtension(*args, **kwargs):
        """GetExtension(self) -> String"""
        return __core.ImageHandler_GetExtension(*args, **kwargs)

    def GetAltExtensions(*args, **kwargs):
        """GetAltExtensions(self) -> wxArrayString"""
        return __core.ImageHandler_GetAltExtensions(*args, **kwargs)

    def GetType(*args, **kwargs):
        """GetType(self) -> int"""
        return __core.ImageHandler_GetType(*args, **kwargs)

    def GetMimeType(*args, **kwargs):
        """GetMimeType(self) -> String"""
        return __core.ImageHandler_GetMimeType(*args, **kwargs)

    def CanRead(*args, **kwargs):
        """CanRead(self, String name) -> bool"""
        return __core.ImageHandler_CanRead(*args, **kwargs)

    def CanReadStream(*args, **kwargs):
        """CanReadStream(self, InputStream stream) -> bool"""
        return __core.ImageHandler_CanReadStream(*args, **kwargs)

    def SetName(*args, **kwargs):
        """SetName(self, String name)"""
        return __core.ImageHandler_SetName(*args, **kwargs)

    def SetExtension(*args, **kwargs):
        """SetExtension(self, String extension)"""
        return __core.ImageHandler_SetExtension(*args, **kwargs)

    def SetAltExtensions(*args, **kwargs):
        """SetAltExtensions(self, wxArrayString exts)"""
        return __core.ImageHandler_SetAltExtensions(*args, **kwargs)

    def SetType(*args, **kwargs):
        """SetType(self, int type)"""
        return __core.ImageHandler_SetType(*args, **kwargs)

    def SetMimeType(*args, **kwargs):
        """SetMimeType(self, String mimetype)"""
        return __core.ImageHandler_SetMimeType(*args, **kwargs)

    Extension = property(GetExtension,SetExtension,doc="See `GetExtension` and `SetExtension`") 
    AltExtensions = property(GetAltExtensions,SetAltExtensions) 
    MimeType = property(GetMimeType,SetMimeType,doc="See `GetMimeType` and `SetMimeType`") 
    Name = property(GetName,SetName,doc="See `GetName` and `SetName`") 
    Type = property(GetType,SetType,doc="See `GetType` and `SetType`") 
__core.ImageHandler_swigregister(ImageHandler)

class PyImageHandler(ImageHandler):
    """
    This is the base class for implementing image file loading/saving, and
    image creation from data, all written in Python.  To create a custom
    image handler derive a new class from wx.PyImageHandler and provide
    the following methods::

        def DoCanRead(self, stream) --> bool
            '''Check if this handler can read the image on the stream'''

        def LoadFile(self, image, stream, verbose, index) --> bool
            '''Load image data from the stream and load it into image.'''

        def SaveFile(self, image, stream, verbose) --> bool
            '''Save the iamge data in image to the stream using
               this handler's image file format.'''

        def GetImageCount(self, stream) --> int
            '''If this image format can hold more than one image,
               how many does the image on the stream have?'''

    To activate your handler create an instance of it and pass it to
    `wx.Image_AddHandler`.  Be sure to call `SetName`, `SetType`, and
    `SetExtension` from your constructor.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PyImageHandler

        This is the base class for implementing image file loading/saving, and
        image creation from data, all written in Python.  To create a custom
        image handler derive a new class from wx.PyImageHandler and provide
        the following methods::

            def DoCanRead(self, stream) --> bool
                '''Check if this handler can read the image on the stream'''

            def LoadFile(self, image, stream, verbose, index) --> bool
                '''Load image data from the stream and load it into image.'''

            def SaveFile(self, image, stream, verbose) --> bool
                '''Save the iamge data in image to the stream using
                   this handler's image file format.'''

            def GetImageCount(self, stream) --> int
                '''If this image format can hold more than one image,
                   how many does the image on the stream have?'''

        To activate your handler create an instance of it and pass it to
        `wx.Image_AddHandler`.  Be sure to call `SetName`, `SetType`, and
        `SetExtension` from your constructor.

        """
        this = __core.new_PyImageHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._SetSelf(self)

    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return __core.PyImageHandler__SetSelf(*args, **kwargs)

__core.PyImageHandler_swigregister(PyImageHandler)

class ImageHistogram(object):
    """Proxy of C++ ImageHistogram class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> ImageHistogram"""
        this = __core.new_ImageHistogram(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def MakeKey(*args, **kwargs):
        """
        MakeKey(byte r, byte g, byte b) -> unsigned long

        Get the key in the histogram for the given RGB values
        """
        return __core.ImageHistogram_MakeKey(*args, **kwargs)

    MakeKey = staticmethod(MakeKey)
    def FindFirstUnusedColour(*args, **kwargs):
        """
        FindFirstUnusedColour(int startR=1, int startG=0, int startB=0) -> (success, r, g, b)

        Find first colour that is not used in the image and has higher RGB
        values than startR, startG, startB.  Returns a tuple consisting of a
        success flag and rgb values.
        """
        return __core.ImageHistogram_FindFirstUnusedColour(*args, **kwargs)

    def GetCount(*args, **kwargs):
        """
        GetCount(self, unsigned long key) -> unsigned long

        Returns the pixel count for the given key.  Use `MakeKey` to create a
        key value from a RGB tripple.
        """
        return __core.ImageHistogram_GetCount(*args, **kwargs)

    def GetCountRGB(*args, **kwargs):
        """
        GetCountRGB(self, byte r, byte g, byte b) -> unsigned long

        Returns the pixel count for the given RGB values.
        """
        return __core.ImageHistogram_GetCountRGB(*args, **kwargs)

    def GetCountColour(*args, **kwargs):
        """
        GetCountColour(self, Colour colour) -> unsigned long

        Returns the pixel count for the given `wx.Colour` value.
        """
        return __core.ImageHistogram_GetCountColour(*args, **kwargs)

__core.ImageHistogram_swigregister(ImageHistogram)

def ImageHistogram_MakeKey(*args, **kwargs):
  """
    ImageHistogram_MakeKey(byte r, byte g, byte b) -> unsigned long

    Get the key in the histogram for the given RGB values
    """
  return __core.ImageHistogram_MakeKey(*args, **kwargs)

class Image_RGBValue(object):
    """
    An object that contains values for red, green and blue which represent
    the value of a color. It is used by `wx.Image.HSVtoRGB` and
    `wx.Image.RGBtoHSV`, which converts between HSV color space and RGB
    color space.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, byte r=0, byte g=0, byte b=0) -> Image_RGBValue

        Constructor.
        """
        this = __core.new_Image_RGBValue(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Image_RGBValue
    __del__ = lambda self : None;
    red = property(__core.Image_RGBValue_red_get, __core.Image_RGBValue_red_set)
    green = property(__core.Image_RGBValue_green_get, __core.Image_RGBValue_green_set)
    blue = property(__core.Image_RGBValue_blue_get, __core.Image_RGBValue_blue_set)
__core.Image_RGBValue_swigregister(Image_RGBValue)

class Image_HSVValue(object):
    """
    An object that contains values for hue, saturation and value which
    represent the value of a color.  It is used by `wx.Image.HSVtoRGB` and
    `wx.Image.RGBtoHSV`, which converts between HSV color space and RGB
    color space.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, double h=0.0, double s=0.0, double v=0.0) -> Image_HSVValue

        Constructor.
        """
        this = __core.new_Image_HSVValue(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Image_HSVValue
    __del__ = lambda self : None;
    hue = property(__core.Image_HSVValue_hue_get, __core.Image_HSVValue_hue_set)
    saturation = property(__core.Image_HSVValue_saturation_get, __core.Image_HSVValue_saturation_set)
    value = property(__core.Image_HSVValue_value_get, __core.Image_HSVValue_value_set)
__core.Image_HSVValue_swigregister(Image_HSVValue)

class Image(Object):
    """
    A platform-independent image class.  An image can be created from
    data, or using `wx.Bitmap.ConvertToImage`, or loaded from a file in a
    variety of formats.  Functions are available to set and get image
    bits, so it can be used for basic image manipulation.

    A wx.Image cannot be drawn directly to a `wx.DC`.  Instead, a
    platform-specific `wx.Bitmap` object must be created from it using the
    `wx.BitmapFromImage` constructor. This bitmap can then be drawn in a
    device context, using `wx.DC.DrawBitmap`.

    One colour value of the image may be used as a mask colour which will
    lead to the automatic creation of a `wx.Mask` object associated to the
    bitmap object.

    wx.Image supports alpha channel data, that is in addition to a byte
    for the red, green and blue colour components for each pixel it also
    stores a byte representing the pixel opacity. An alpha value of 0
    corresponds to a transparent pixel (null opacity) while a value of 255
    means that the pixel is 100% opaque.

    Unlike RGB data, not all images have an alpha channel and before using
    `GetAlpha` you should check if this image contains an alpha channel
    with `HasAlpha`. Note that currently only images loaded from PNG files
    with transparency information will have an alpha channel.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String name, int type=BITMAP_TYPE_ANY, int index=-1) -> Image

        Loads an image from a file.
        """
        this = __core.new_Image(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_Image
    __del__ = lambda self : None;
    def Create(*args, **kwargs):
        """
        Create(self, int width, int height, bool clear=True)

        Creates a fresh image.  If clear is ``True``, the new image will be
        initialized to black. Otherwise, the image data will be uninitialized.
        """
        return __core.Image_Create(*args, **kwargs)

    def Destroy(*args, **kwargs):
        """
        Destroy(self)

        Destroys the image data.
        """
        args[0].this.own(False)
        return __core.Image_Destroy(*args, **kwargs)

    def Scale(*args, **kwargs):
        """
        Scale(self, int width, int height, int quality=IMAGE_QUALITY_NORMAL) -> Image

        Returns a scaled version of the image. This is also useful for scaling
        bitmaps in general as the only other way to scale bitmaps is to blit a
        `wx.MemoryDC` into another `wx.MemoryDC`.  The ``quality`` parameter
        specifies what method to use for resampling the image.  It can be
        either wx.IMAGE_QUALITY_NORMAL, which uses the normal default scaling
        method of pixel replication, or wx.IMAGE_QUALITY_HIGH which uses
        bicubic and box averaging resampling methods for upsampling and
        downsampling respectively.
        """
        return __core.Image_Scale(*args, **kwargs)

    def ResampleNearest(*args, **kwargs):
        """ResampleNearest(self, int width, int height) -> Image"""
        return __core.Image_ResampleNearest(*args, **kwargs)

    def ResampleBox(*args, **kwargs):
        """ResampleBox(self, int width, int height) -> Image"""
        return __core.Image_ResampleBox(*args, **kwargs)

    def ResampleBilinear(*args, **kwargs):
        """ResampleBilinear(self, int width, int height) -> Image"""
        return __core.Image_ResampleBilinear(*args, **kwargs)

    def ResampleBicubic(*args, **kwargs):
        """ResampleBicubic(self, int width, int height) -> Image"""
        return __core.Image_ResampleBicubic(*args, **kwargs)

    def Blur(*args, **kwargs):
        """
        Blur(self, int radius) -> Image

        Blurs the image in both horizontal and vertical directions by the
        specified pixel ``radius``. This should not be used when using a
        single mask colour for transparency.
        """
        return __core.Image_Blur(*args, **kwargs)

    def BlurHorizontal(*args, **kwargs):
        """
        BlurHorizontal(self, int radius) -> Image

        Blurs the image in the horizontal direction only. This should not be
        used when using a single mask colour for transparency.

        """
        return __core.Image_BlurHorizontal(*args, **kwargs)

    def BlurVertical(*args, **kwargs):
        """
        BlurVertical(self, int radius) -> Image

        Blurs the image in the vertical direction only. This should not be
        used when using a single mask colour for transparency.
        """
        return __core.Image_BlurVertical(*args, **kwargs)

    def ShrinkBy(*args, **kwargs):
        """
        ShrinkBy(self, int xFactor, int yFactor) -> Image

        Return a version of the image scaled smaller by the given factors.
        """
        return __core.Image_ShrinkBy(*args, **kwargs)

    def Rescale(*args, **kwargs):
        """
        Rescale(self, int width, int height, int quality=IMAGE_QUALITY_NORMAL) -> Image

        Changes the size of the image in-place by scaling it: after a call to
        this function, the image will have the given width and height.

        Returns the (modified) image itself.
        """
        return __core.Image_Rescale(*args, **kwargs)

    def Resize(*args, **kwargs):
        """
        Resize(self, Size size, Point pos, int r=-1, int g=-1, int b=-1) -> Image

        Changes the size of the image in-place without scaling it, by adding
        either a border with the given colour or cropping as necessary. The
        image is pasted into a new image with the given size and background
        colour at the position pos relative to the upper left of the new
        image. If red = green = blue = -1 then use either the current mask
        colour if set or find, use, and set a suitable mask colour for any
        newly exposed areas.

        Returns the (modified) image itself.
        """
        return __core.Image_Resize(*args, **kwargs)

    def SetRGB(*args, **kwargs):
        """
        SetRGB(self, int x, int y, byte r, byte g, byte b)

        Sets the pixel at the given coordinate. This routine performs
        bounds-checks for the coordinate so it can be considered a safe way to
        manipulate the data, but in some cases this might be too slow so that
        the data will have to be set directly. In that case you will have to
        get access to the image data using the `GetData` method.
        """
        return __core.Image_SetRGB(*args, **kwargs)

    def SetRGBRect(*args, **kwargs):
        """
        SetRGBRect(self, Rect rect, byte r, byte g, byte b)

        Sets the colour of the pixels within the given rectangle. This routine
        performs bounds-checks for the rectangle so it can be considered a
        safe way to manipulate the data.
        """
        return __core.Image_SetRGBRect(*args, **kwargs)

    def GetRed(*args, **kwargs):
        """
        GetRed(self, int x, int y) -> byte

        Returns the red intensity at the given coordinate.
        """
        return __core.Image_GetRed(*args, **kwargs)

    def GetGreen(*args, **kwargs):
        """
        GetGreen(self, int x, int y) -> byte

        Returns the green intensity at the given coordinate.
        """
        return __core.Image_GetGreen(*args, **kwargs)

    def GetBlue(*args, **kwargs):
        """
        GetBlue(self, int x, int y) -> byte

        Returns the blue intensity at the given coordinate.
        """
        return __core.Image_GetBlue(*args, **kwargs)

    def SetAlpha(*args, **kwargs):
        """
        SetAlpha(self, int x, int y, byte alpha)

        Sets the alpha value for the given pixel. This function should only be
        called if the image has alpha channel data, use `HasAlpha` to check
        for this.
        """
        return __core.Image_SetAlpha(*args, **kwargs)

    def GetAlpha(*args, **kwargs):
        """
        GetAlpha(self, int x, int y) -> byte

        Returns the alpha value for the given pixel. This function may only be
        called for the images with alpha channel, use `HasAlpha` to check for
        this.

        The returned value is the *opacity* of the image, i.e. the value of 0
        corresponds to the fully transparent pixels while the value of 255 to
        the fully opaque pixels.
        """
        return __core.Image_GetAlpha(*args, **kwargs)

    def HasAlpha(*args, **kwargs):
        """
        HasAlpha(self) -> bool

        Returns true if this image has alpha channel, false otherwise.
        """
        return __core.Image_HasAlpha(*args, **kwargs)

    def InitAlpha(*args, **kwargs):
        """
        InitAlpha(self)

        Initializes the image alpha channel data. It is an error to call it if
        the image already has alpha data. If it doesn't, alpha data will be by
        default initialized to all pixels being fully opaque. But if the image
        has a a mask colour, all mask pixels will be completely transparent.
        """
        return __core.Image_InitAlpha(*args, **kwargs)

    def ClearAlpha(*args, **kwargs):
        """ClearAlpha(self)"""
        return __core.Image_ClearAlpha(*args, **kwargs)

    def IsTransparent(*args, **kwargs):
        """
        IsTransparent(self, int x, int y, byte threshold=IMAGE_ALPHA_THRESHOLD) -> bool

        Returns ``True`` if this pixel is masked or has an alpha value less
        than the spcified threshold.
        """
        return __core.Image_IsTransparent(*args, **kwargs)

    def FindFirstUnusedColour(*args, **kwargs):
        """
        FindFirstUnusedColour(int startR=1, int startG=0, int startB=0) -> (success, r, g, b)

        Find first colour that is not used in the image and has higher RGB
        values than startR, startG, startB.  Returns a tuple consisting of a
        success flag and rgb values.
        """
        return __core.Image_FindFirstUnusedColour(*args, **kwargs)

    def ConvertAlphaToMask(*args, **kwargs):
        """
        ConvertAlphaToMask(self, byte threshold=IMAGE_ALPHA_THRESHOLD) -> bool

        If the image has alpha channel, this method converts it to mask. All
        pixels with alpha value less than ``threshold`` are replaced with the
        mask colour and the alpha channel is removed. The mask colour is
        chosen automatically using `FindFirstUnusedColour`.

        If the image image doesn't have alpha channel, ConvertAlphaToMask does
        nothing.
        """
        return __core.Image_ConvertAlphaToMask(*args, **kwargs)

    def ConvertColourToAlpha(*args, **kwargs):
        """
        ConvertColourToAlpha(self, byte r, byte g, byte b) -> bool

        This method converts an image where the original alpha information is
        only available as a shades of a colour (actually shades of grey)
        typically when you draw anti-aliased text into a bitmap. The DC
        drawing routines draw grey values on the black background although
        they actually mean to draw white with differnt alpha values.  This
        method reverses it, assuming a black (!) background and white text.
        The method will then fill up the whole image with the colour given.
        """
        return __core.Image_ConvertColourToAlpha(*args, **kwargs)

    def SetMaskFromImage(*args, **kwargs):
        """
        SetMaskFromImage(self, Image mask, byte mr, byte mg, byte mb) -> bool

        Sets the image's mask so that the pixels that have RGB value of
        ``(mr,mg,mb)`` in ``mask`` will be masked in this image. This is done
        by first finding an unused colour in the image, setting this colour as
        the mask colour and then using this colour to draw all pixels in the
        image who corresponding pixel in mask has given RGB value.

        Returns ``False`` if ``mask`` does not have same dimensions as the
        image or if there is no unused colour left. Returns ``True`` if the
        mask was successfully applied.

        Note that this method involves computing the histogram, which is
        computationally intensive operation.
        """
        return __core.Image_SetMaskFromImage(*args, **kwargs)

    def CanRead(*args, **kwargs):
        """
        CanRead(String filename) -> bool

        Returns True if the image handlers can read this file.
        """
        return __core.Image_CanRead(*args, **kwargs)

    CanRead = staticmethod(CanRead)
    def GetImageCount(*args, **kwargs):
        """
        GetImageCount(String filename, int type=BITMAP_TYPE_ANY) -> int

        If the image file contains more than one image and the image handler
        is capable of retrieving these individually, this function will return
        the number of available images.
        """
        return __core.Image_GetImageCount(*args, **kwargs)

    GetImageCount = staticmethod(GetImageCount)
    def LoadFile(*args, **kwargs):
        """
        LoadFile(self, String name, int type=BITMAP_TYPE_ANY, int index=-1) -> bool

        Loads an image from a file. If no handler type is provided, the
        library will try to autodetect the format.
        """
        return __core.Image_LoadFile(*args, **kwargs)

    def LoadMimeFile(*args, **kwargs):
        """
        LoadMimeFile(self, String name, String mimetype, int index=-1) -> bool

        Loads an image from a file, specifying the image type with a MIME type
        string.
        """
        return __core.Image_LoadMimeFile(*args, **kwargs)

    def SaveFile(*args, **kwargs):
        """
        SaveFile(self, String name, int type) -> bool

        Saves an image in the named file.
        """
        return __core.Image_SaveFile(*args, **kwargs)

    def SaveMimeFile(*args, **kwargs):
        """
        SaveMimeFile(self, String name, String mimetype) -> bool

        Saves an image in the named file.
        """
        return __core.Image_SaveMimeFile(*args, **kwargs)

    def SaveStream(*args, **kwargs):
        """
        SaveStream(self, wxOutputStream stream, int type) -> bool

        Saves an image in the named file.
        """
        return __core.Image_SaveStream(*args, **kwargs)

    def SaveMimeStream(*args, **kwargs):
        """
        SaveMimeStream(self, wxOutputStream stream, String mimetype) -> bool

        Saves an image in the named file.
        """
        return __core.Image_SaveMimeStream(*args, **kwargs)

    def CanReadStream(*args, **kwargs):
        """
        CanReadStream(InputStream stream) -> bool

        Returns True if the image handlers can read an image file from the
        data currently on the input stream, or a readable Python file-like
        object.
        """
        return __core.Image_CanReadStream(*args, **kwargs)

    CanReadStream = staticmethod(CanReadStream)
    def LoadStream(*args, **kwargs):
        """
        LoadStream(self, InputStream stream, int type=BITMAP_TYPE_ANY, int index=-1) -> bool

        Loads an image from an input stream or a readable Python file-like
        object. If no handler type is provided, the library will try to
        autodetect the format.
        """
        return __core.Image_LoadStream(*args, **kwargs)

    def LoadMimeStream(*args, **kwargs):
        """
        LoadMimeStream(self, InputStream stream, String mimetype, int index=-1) -> bool

        Loads an image from an input stream or a readable Python file-like
        object, using a MIME type string to specify the image file format.
        """
        return __core.Image_LoadMimeStream(*args, **kwargs)

    def IsOk(*args, **kwargs):
        """
        IsOk(self) -> bool

        Returns true if image data is present.
        """
        return __core.Image_IsOk(*args, **kwargs)

    Ok = IsOk 
    def GetWidth(*args, **kwargs):
        """
        GetWidth(self) -> int

        Gets the width of the image in pixels.
        """
        return __core.Image_GetWidth(*args, **kwargs)

    def GetHeight(*args, **kwargs):
        """
        GetHeight(self) -> int

        Gets the height of the image in pixels.
        """
        return __core.Image_GetHeight(*args, **kwargs)

    def GetType(*args, **kwargs):
        """
        GetType(self) -> int

        Gets the type of image found by LoadFile or specified with SaveFile
        """
        return __core.Image_GetType(*args, **kwargs)

    def SetType(*args, **kwargs):
        """
        SetType(self, int type)

        Set the image type, this is normally only called if the image is being
        created from data in the given format but not using LoadFile() (e.g.
        wxGIFDecoder uses this)

        """
        return __core.Image_SetType(*args, **kwargs)

    def GetSize(*args, **kwargs):
        """
        GetSize(self) -> Size

        Returns the size of the image in pixels.
        """
        return __core.Image_GetSize(*args, **kwargs)

    def GetSubImage(*args, **kwargs):
        """
        GetSubImage(self, Rect rect) -> Image

        Returns a sub image of the current one as long as the rect belongs
        entirely to the image.
        """
        return __core.Image_GetSubImage(*args, **kwargs)

    def Size(*args, **kwargs):
        """
        Size(self, Size size, Point pos, int r=-1, int g=-1, int b=-1) -> Image

        Returns a resized version of this image without scaling it by adding
        either a border with the given colour or cropping as necessary. The
        image is pasted into a new image with the given size and background
        colour at the position ``pos`` relative to the upper left of the new
        image. If red = green = blue = -1 then use either the current mask
        colour if set or find, use, and set a suitable mask colour for any
        newly exposed areas.
        """
        return __core.Image_Size(*args, **kwargs)

    def Clear(*args, **kwargs):
        """
        Clear(self, unsigned char value=0)

        initialize the image data with zeroes
        """
        return __core.Image_Clear(*args, **kwargs)

    def Copy(*args, **kwargs):
        """
        Copy(self) -> Image

        Returns an identical copy of the image.
        """
        return __core.Image_Copy(*args, **kwargs)

    def Paste(*args, **kwargs):
        """
        Paste(self, Image image, int x, int y)

        Pastes ``image`` into this instance and takes care of the mask colour
        and any out of bounds problems.
        """
        return __core.Image_Paste(*args, **kwargs)

    def GetData(*args, **kwargs):
        """
        GetData(self) -> PyObject

        Returns a string containing a copy of the RGB bytes of the image.
        """
        return __core.Image_GetData(*args, **kwargs)

    def SetData(*args, **kwargs):
        """
        SetData(self, buffer data)

        Resets the Image's RGB data from a buffer of RGB bytes.  Accepts
        either a string or a buffer object holding the data and the length of
        the data must be width*height*3.
        """
        return __core.Image_SetData(*args, **kwargs)

    def GetDataBuffer(*args, **kwargs):
        """
        GetDataBuffer(self) -> PyObject

        Returns a writable Python buffer object that is pointing at the RGB
        image data buffer inside the wx.Image. You need to ensure that you do
        not use this buffer object after the image has been destroyed.
        """
        return __core.Image_GetDataBuffer(*args, **kwargs)

    def SetDataBuffer(*args, **kwargs):
        """
        SetDataBuffer(self, buffer data)

        Sets the internal image data pointer to point at a Python buffer
        object.  This can save making an extra copy of the data but you must
        ensure that the buffer object lives longer than the wx.Image does.
        """
        return __core.Image_SetDataBuffer(*args, **kwargs)

    def GetAlphaData(*args, **kwargs):
        """
        GetAlphaData(self) -> PyObject

        Returns a string containing a copy of the alpha bytes of the image.
        """
        return __core.Image_GetAlphaData(*args, **kwargs)

    def SetAlphaData(*args, **kwargs):
        """
        SetAlphaData(self, buffer alpha)

        Resets the Image's alpha data from a buffer of bytes.  Accepts either
        a string or a buffer object holding the data and the length of the
        data must be width*height.
        """
        return __core.Image_SetAlphaData(*args, **kwargs)

    def GetAlphaBuffer(*args, **kwargs):
        """
        GetAlphaBuffer(self) -> PyObject

        Returns a writable Python buffer object that is pointing at the Alpha
        data buffer inside the wx.Image. You need to ensure that you do not
        use this buffer object after the image has been destroyed.
        """
        return __core.Image_GetAlphaBuffer(*args, **kwargs)

    def SetAlphaBuffer(*args, **kwargs):
        """
        SetAlphaBuffer(self, buffer alpha)

        Sets the internal image alpha pointer to point at a Python buffer
        object.  This can save making an extra copy of the data but you must
        ensure that the buffer object lives as long as the wx.Image does.
        """
        return __core.Image_SetAlphaBuffer(*args, **kwargs)

    def SetMaskColour(*args, **kwargs):
        """
        SetMaskColour(self, byte r, byte g, byte b)

        Sets the mask colour for this image (and tells the image to use the
        mask).
        """
        return __core.Image_SetMaskColour(*args, **kwargs)

    def GetOrFindMaskColour(*args, **kwargs):
        """
        GetOrFindMaskColour() -> (r,g,b)

        Get the current mask colour or find a suitable colour.
        """
        return __core.Image_GetOrFindMaskColour(*args, **kwargs)

    def GetMaskRed(*args, **kwargs):
        """
        GetMaskRed(self) -> byte

        Gets the red component of the mask colour.
        """
        return __core.Image_GetMaskRed(*args, **kwargs)

    def GetMaskGreen(*args, **kwargs):
        """
        GetMaskGreen(self) -> byte

        Gets the green component of the mask colour.
        """
        return __core.Image_GetMaskGreen(*args, **kwargs)

    def GetMaskBlue(*args, **kwargs):
        """
        GetMaskBlue(self) -> byte

        Gets the blue component of the mask colour.
        """
        return __core.Image_GetMaskBlue(*args, **kwargs)

    def SetMask(*args, **kwargs):
        """
        SetMask(self, bool mask=True)

        Specifies whether there is a mask or not. The area of the mask is
        determined by the current mask colour.
        """
        return __core.Image_SetMask(*args, **kwargs)

    def HasMask(*args, **kwargs):
        """
        HasMask(self) -> bool

        Returns ``True`` if there is a mask active, ``False`` otherwise.
        """
        return __core.Image_HasMask(*args, **kwargs)

    def Rotate(*args, **kwargs):
        """
        Rotate(self, double angle, Point centre_of_rotation, bool interpolating=True, 
            Point offset_after_rotation=None) -> Image

        Rotates the image about the given point, by ``angle`` radians. Passing
        ``True`` to ``interpolating`` results in better image quality, but is
        slower. If the image has a mask, then the mask colour is used for the
        uncovered pixels in the rotated image background. Otherwise, black
        will be used as the fill colour.

        Returns the rotated image, leaving this image intact.
        """
        return __core.Image_Rotate(*args, **kwargs)

    def Rotate90(*args, **kwargs):
        """
        Rotate90(self, bool clockwise=True) -> Image

        Returns a copy of the image rotated 90 degrees in the direction
        indicated by ``clockwise``.
        """
        return __core.Image_Rotate90(*args, **kwargs)

    def Rotate180(*args, **kwargs):
        """Rotate180(self) -> Image"""
        return __core.Image_Rotate180(*args, **kwargs)

    def Mirror(*args, **kwargs):
        """
        Mirror(self, bool horizontally=True) -> Image

        Returns a mirrored copy of the image. The parameter ``horizontally``
        indicates the orientation.
        """
        return __core.Image_Mirror(*args, **kwargs)

    def Replace(*args, **kwargs):
        """
        Replace(self, byte r1, byte g1, byte b1, byte r2, byte g2, byte b2)

        Replaces the colour specified by ``(r1,g1,b1)`` by the colour
        ``(r2,g2,b2)``.
        """
        return __core.Image_Replace(*args, **kwargs)

    def ConvertToGreyscale(*args):
        """
        ConvertToGreyscale(self) -> Image
        ConvertToGreyscale(self, double lr, double lg, double lb) -> Image

        Convert to greyscale image. Uses the luminance component (Y) of the
        image.  The luma value (YUV) is calculated using (R * lr) + (G * lg) + (B * lb),
        defaults to ITU-T BT.601
        """
        return __core.Image_ConvertToGreyscale(*args)

    def ConvertToMono(*args, **kwargs):
        """
        ConvertToMono(self, byte r, byte g, byte b) -> Image

        Returns monochromatic version of the image. The returned image has
        white colour where the original has ``(r,g,b)`` colour and black
        colour everywhere else.
        """
        return __core.Image_ConvertToMono(*args, **kwargs)

    def ConvertToDisabled(*args, **kwargs):
        """ConvertToDisabled(self, unsigned char brightness=255) -> Image"""
        return __core.Image_ConvertToDisabled(*args, **kwargs)

    def SetOption(*args, **kwargs):
        """
        SetOption(self, String name, String value)

        Sets an image handler defined option.  For example, when saving as a
        JPEG file, the option ``wx.IMAGE_OPTION_QUALITY`` is used, which is a
        number between 0 and 100 (0 is terrible, 100 is very good).
        """
        return __core.Image_SetOption(*args, **kwargs)

    def SetOptionInt(*args, **kwargs):
        """
        SetOptionInt(self, String name, int value)

        Sets an image option as an integer.
        """
        return __core.Image_SetOptionInt(*args, **kwargs)

    def GetOption(*args, **kwargs):
        """
        GetOption(self, String name) -> String

        Gets the value of an image handler option.
        """
        return __core.Image_GetOption(*args, **kwargs)

    def GetOptionInt(*args, **kwargs):
        """
        GetOptionInt(self, String name) -> int

        Gets the value of an image handler option as an integer.  If the given
        option is not present, the function returns 0.
        """
        return __core.Image_GetOptionInt(*args, **kwargs)

    def HasOption(*args, **kwargs):
        """
        HasOption(self, String name) -> bool

        Returns true if the given option is present.
        """
        return __core.Image_HasOption(*args, **kwargs)

    def CountColours(*args, **kwargs):
        """CountColours(self, unsigned long stopafter=(unsigned long) -1) -> unsigned long"""
        return __core.Image_CountColours(*args, **kwargs)

    def ComputeHistogram(*args, **kwargs):
        """ComputeHistogram(self, ImageHistogram h) -> unsigned long"""
        return __core.Image_ComputeHistogram(*args, **kwargs)

    def AddHandler(*args, **kwargs):
        """AddHandler(ImageHandler handler)"""
        return __core.Image_AddHandler(*args, **kwargs)

    AddHandler = staticmethod(AddHandler)
    def InsertHandler(*args, **kwargs):
        """InsertHandler(ImageHandler handler)"""
        return __core.Image_InsertHandler(*args, **kwargs)

    InsertHandler = staticmethod(InsertHandler)
    def RemoveHandler(*args, **kwargs):
        """RemoveHandler(String name) -> bool"""
        return __core.Image_RemoveHandler(*args, **kwargs)

    RemoveHandler = staticmethod(RemoveHandler)
    def GetHandlers(*args, **kwargs):
        """GetHandlers() -> PyObject"""
        return __core.Image_GetHandlers(*args, **kwargs)

    GetHandlers = staticmethod(GetHandlers)
    def GetImageExtWildcard(*args, **kwargs):
        """
        GetImageExtWildcard() -> String

        Iterates all registered wxImageHandler objects, and returns a string
        containing file extension masks suitable for passing to file open/save
        dialog boxes.
        """
        return __core.Image_GetImageExtWildcard(*args, **kwargs)

    GetImageExtWildcard = staticmethod(GetImageExtWildcard)
    def ConvertToBitmap(*args, **kwargs):
        """ConvertToBitmap(self, int depth=-1) -> Bitmap"""
        return __core.Image_ConvertToBitmap(*args, **kwargs)

    def ConvertToMonoBitmap(*args, **kwargs):
        """ConvertToMonoBitmap(self, byte red, byte green, byte blue) -> Bitmap"""
        return __core.Image_ConvertToMonoBitmap(*args, **kwargs)

    def RotateHue(*args, **kwargs):
        """
        RotateHue(self, double angle)

        Rotates the hue of each pixel of the image. Hue is a double in the
        range -1.0..1.0 where -1.0 is -360 degrees and 1.0 is 360 degrees
        """
        return __core.Image_RotateHue(*args, **kwargs)

    def RGBtoHSV(*args, **kwargs):
        """
        RGBtoHSV(Image_RGBValue rgb) -> Image_HSVValue

        Converts a color in RGB color space to HSV color space.
        """
        return __core.Image_RGBtoHSV(*args, **kwargs)

    RGBtoHSV = staticmethod(RGBtoHSV)
    def HSVtoRGB(*args, **kwargs):
        """
        HSVtoRGB(Image_HSVValue hsv) -> Image_RGBValue

        Converts a color in HSV color space to RGB color space.
        """
        return __core.Image_HSVtoRGB(*args, **kwargs)

    HSVtoRGB = staticmethod(HSVtoRGB)
    def __nonzero__(self): return self.IsOk() 
    def AdjustChannels(*args, **kwargs):
        """
        AdjustChannels(self, double factor_red, double factor_green, double factor_blue, 
            double factor_alpha=1.0) -> Image

        This function muliplies all 4 channels (red, green, blue, alpha) with
        a factor (around 1.0). Useful for gamma correction, colour correction
        and to add a certain amount of transparency to a image (fade in fade
        out effects). If factor_alpha is given but the original image has no
        alpha channel then a alpha channel will be added.
        """
        return __core.Image_AdjustChannels(*args, **kwargs)

    AlphaBuffer = property(GetAlphaBuffer,SetAlphaBuffer,doc="See `GetAlphaBuffer` and `SetAlphaBuffer`") 
    AlphaData = property(GetAlphaData,SetAlphaData,doc="See `GetAlphaData` and `SetAlphaData`") 
    Data = property(GetData,SetData,doc="See `GetData` and `SetData`") 
    DataBuffer = property(GetDataBuffer,SetDataBuffer,doc="See `GetDataBuffer` and `SetDataBuffer`") 
    Height = property(GetHeight,doc="See `GetHeight`") 
    MaskBlue = property(GetMaskBlue,doc="See `GetMaskBlue`") 
    MaskGreen = property(GetMaskGreen,doc="See `GetMaskGreen`") 
    MaskRed = property(GetMaskRed,doc="See `GetMaskRed`") 
    Width = property(GetWidth,doc="See `GetWidth`") 
__core.Image_swigregister(Image)

def ImageFromMime(*args, **kwargs):
    """
    ImageFromMime(String name, String mimetype, int index=-1) -> Image

    Loads an image from a file, using a MIME type string (such as
    'image/jpeg') to specify image type.
    """
    val = __core.new_ImageFromMime(*args, **kwargs)
    return val

def ImageFromStream(*args, **kwargs):
    """
    ImageFromStream(InputStream stream, int type=BITMAP_TYPE_ANY, int index=-1) -> Image

    Loads an image from an input stream, or any readable Python file-like
    object.
    """
    val = __core.new_ImageFromStream(*args, **kwargs)
    return val

def ImageFromStreamMime(*args, **kwargs):
    """
    ImageFromStreamMime(InputStream stream, String mimetype, int index=-1) -> Image

    Loads an image from an input stream, or any readable Python file-like
    object, specifying the image format with a MIME type string.
    """
    val = __core.new_ImageFromStreamMime(*args, **kwargs)
    return val

def EmptyImage(*args, **kwargs):
    """
    EmptyImage(int width=0, int height=0, bool clear=True) -> Image

    Construct an empty image of a given size, optionally setting all
    pixels to black.
    """
    val = __core.new_EmptyImage(*args, **kwargs)
    return val

def ImageFromBitmap(*args, **kwargs):
    """
    ImageFromBitmap(Bitmap bitmap) -> Image

    Construct an Image from a `wx.Bitmap`.
    """
    val = __core.new_ImageFromBitmap(*args, **kwargs)
    return val

def ImageFromData(*args, **kwargs):
    """
    ImageFromData(int width, int height, buffer data) -> Image

    Construct an Image from a buffer of RGB bytes.  Accepts either a
    string or a buffer object holding the data and the length of the data
    must be width*height*3.
    """
    val = __core.new_ImageFromData(*args, **kwargs)
    return val

def ImageFromDataWithAlpha(*args, **kwargs):
    """
    ImageFromDataWithAlpha(int width, int height, buffer data, buffer alpha) -> Image

    Construct an Image from a buffer of RGB bytes with an Alpha channel.
    Accepts either a string or a buffer object holding the data and the
    length of the data must be width*height*3 bytes, and the length of the
    alpha data must be width*height bytes.
    """
    val = __core.new_ImageFromDataWithAlpha(*args, **kwargs)
    return val

def Image_CanRead(*args, **kwargs):
  """
    Image_CanRead(String filename) -> bool

    Returns True if the image handlers can read this file.
    """
  return __core.Image_CanRead(*args, **kwargs)

def Image_GetImageCount(*args, **kwargs):
  """
    Image_GetImageCount(String filename, int type=BITMAP_TYPE_ANY) -> int

    If the image file contains more than one image and the image handler
    is capable of retrieving these individually, this function will return
    the number of available images.
    """
  return __core.Image_GetImageCount(*args, **kwargs)

def Image_CanReadStream(*args, **kwargs):
  """
    Image_CanReadStream(InputStream stream) -> bool

    Returns True if the image handlers can read an image file from the
    data currently on the input stream, or a readable Python file-like
    object.
    """
  return __core.Image_CanReadStream(*args, **kwargs)

def Image_AddHandler(*args, **kwargs):
  """Image_AddHandler(ImageHandler handler)"""
  return __core.Image_AddHandler(*args, **kwargs)

def Image_InsertHandler(*args, **kwargs):
  """Image_InsertHandler(ImageHandler handler)"""
  return __core.Image_InsertHandler(*args, **kwargs)

def Image_RemoveHandler(*args, **kwargs):
  """Image_RemoveHandler(String name) -> bool"""
  return __core.Image_RemoveHandler(*args, **kwargs)

def Image_GetHandlers(*args):
  """Image_GetHandlers() -> PyObject"""
  return __core.Image_GetHandlers(*args)

def Image_GetImageExtWildcard(*args):
  """
    Image_GetImageExtWildcard() -> String

    Iterates all registered wxImageHandler objects, and returns a string
    containing file extension masks suitable for passing to file open/save
    dialog boxes.
    """
  return __core.Image_GetImageExtWildcard(*args)

def Image_RGBtoHSV(*args, **kwargs):
  """
    Image_RGBtoHSV(Image_RGBValue rgb) -> Image_HSVValue

    Converts a color in RGB color space to HSV color space.
    """
  return __core.Image_RGBtoHSV(*args, **kwargs)

def Image_HSVtoRGB(*args, **kwargs):
  """
    Image_HSVtoRGB(Image_HSVValue hsv) -> Image_RGBValue

    Converts a color in HSV color space to RGB color space.
    """
  return __core.Image_HSVtoRGB(*args, **kwargs)


def _ImageFromBuffer(*args, **kwargs):
  """_ImageFromBuffer(int width, int height, buffer data, buffer alpha=None) -> Image"""
  return __core._ImageFromBuffer(*args, **kwargs)
def ImageFromBuffer(width, height, dataBuffer, alphaBuffer=None):
    """
    Creates a `wx.Image` from the data in dataBuffer.  The dataBuffer
    parameter must be a Python object that implements the buffer interface,
    such as a string, array, etc.  The dataBuffer object is expected to
    contain a series of RGB bytes and be width*height*3 bytes long.  A buffer
    object can optionally be supplied for the image's alpha channel data, and
    it is expected to be width*height bytes long.

    The wx.Image will be created with its data and alpha pointers initialized
    to the memory address pointed to by the buffer objects, thus saving the
    time needed to copy the image data from the buffer object to the wx.Image.
    While this has advantages, it also has the shoot-yourself-in-the-foot
    risks associated with sharing a C pointer between two objects.

    To help alleviate the risk a reference to the data and alpha buffer
    objects are kept with the wx.Image, so that they won't get deleted until
    after the wx.Image is deleted.  However please be aware that it is not
    guaranteed that an object won't move its memory buffer to a new location
    when it needs to resize its contents.  If that happens then the wx.Image
    will end up referring to an invalid memory location and could cause the
    application to crash.  Therefore care should be taken to not manipulate
    the objects used for the data and alpha buffers in a way that would cause
    them to change size.
    """
    image = _core_._ImageFromBuffer(width, height, dataBuffer, alphaBuffer)
    image._buffer = dataBuffer
    image._alpha = alphaBuffer
    return image

@wx.deprecated
def InitAllImageHandlers():
    """
    The former functionality of InitAllImageHanders is now done internal to
    the _core_ extension module and so this function has become a simple NOP.
    """
    pass

IMAGE_RESOLUTION_NONE = __core.IMAGE_RESOLUTION_NONE
IMAGE_RESOLUTION_INCHES = __core.IMAGE_RESOLUTION_INCHES
IMAGE_RESOLUTION_CM = __core.IMAGE_RESOLUTION_CM
PNG_TYPE_COLOUR = __core.PNG_TYPE_COLOUR
PNG_TYPE_GREY = __core.PNG_TYPE_GREY
PNG_TYPE_GREY_RED = __core.PNG_TYPE_GREY_RED
BMP_24BPP = __core.BMP_24BPP
BMP_8BPP = __core.BMP_8BPP
BMP_8BPP_GREY = __core.BMP_8BPP_GREY
BMP_8BPP_GRAY = __core.BMP_8BPP_GRAY
BMP_8BPP_RED = __core.BMP_8BPP_RED
BMP_8BPP_PALETTE = __core.BMP_8BPP_PALETTE
BMP_4BPP = __core.BMP_4BPP
BMP_1BPP = __core.BMP_1BPP
BMP_1BPP_BW = __core.BMP_1BPP_BW
class BMPHandler(ImageHandler):
    """A `wx.ImageHandler` for \*.bmp bitmap files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> BMPHandler

        A `wx.ImageHandler` for \*.bmp bitmap files.
        """
        this = __core.new_BMPHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.BMPHandler_swigregister(BMPHandler)
NullImage = cvar.NullImage
IMAGE_OPTION_FILENAME = cvar.IMAGE_OPTION_FILENAME
IMAGE_OPTION_BMP_FORMAT = cvar.IMAGE_OPTION_BMP_FORMAT
IMAGE_OPTION_CUR_HOTSPOT_X = cvar.IMAGE_OPTION_CUR_HOTSPOT_X
IMAGE_OPTION_CUR_HOTSPOT_Y = cvar.IMAGE_OPTION_CUR_HOTSPOT_Y
IMAGE_OPTION_RESOLUTION = cvar.IMAGE_OPTION_RESOLUTION
IMAGE_OPTION_RESOLUTIONX = cvar.IMAGE_OPTION_RESOLUTIONX
IMAGE_OPTION_RESOLUTIONY = cvar.IMAGE_OPTION_RESOLUTIONY
IMAGE_OPTION_RESOLUTIONUNIT = cvar.IMAGE_OPTION_RESOLUTIONUNIT
IMAGE_OPTION_QUALITY = cvar.IMAGE_OPTION_QUALITY
IMAGE_OPTION_MAX_WIDTH = cvar.IMAGE_OPTION_MAX_WIDTH
IMAGE_OPTION_MAX_HEIGHT = cvar.IMAGE_OPTION_MAX_HEIGHT
IMAGE_OPTION_ORIGINAL_WIDTH = cvar.IMAGE_OPTION_ORIGINAL_WIDTH
IMAGE_OPTION_ORIGINAL_HEIGHT = cvar.IMAGE_OPTION_ORIGINAL_HEIGHT
IMAGE_OPTION_BITSPERSAMPLE = cvar.IMAGE_OPTION_BITSPERSAMPLE
IMAGE_OPTION_SAMPLESPERPIXEL = cvar.IMAGE_OPTION_SAMPLESPERPIXEL
IMAGE_OPTION_COMPRESSION = cvar.IMAGE_OPTION_COMPRESSION
IMAGE_OPTION_IMAGEDESCRIPTOR = cvar.IMAGE_OPTION_IMAGEDESCRIPTOR
IMAGE_OPTION_PNG_FORMAT = cvar.IMAGE_OPTION_PNG_FORMAT
IMAGE_OPTION_PNG_BITDEPTH = cvar.IMAGE_OPTION_PNG_BITDEPTH

class ICOHandler(BMPHandler):
    """A `wx.ImageHandler` for \*.ico icon files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> ICOHandler

        A `wx.ImageHandler` for \*.ico icon files.
        """
        this = __core.new_ICOHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.ICOHandler_swigregister(ICOHandler)

class CURHandler(ICOHandler):
    """A `wx.ImageHandler` for \*.cur cursor files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> CURHandler

        A `wx.ImageHandler` for \*.cur cursor files.
        """
        this = __core.new_CURHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.CURHandler_swigregister(CURHandler)

class ANIHandler(CURHandler):
    """A `wx.ImageHandler` for \*.ani animated cursor files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> ANIHandler

        A `wx.ImageHandler` for \*.ani animated cursor files.
        """
        this = __core.new_ANIHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.ANIHandler_swigregister(ANIHandler)

class PNGHandler(ImageHandler):
    """A `wx.ImageHandler` for PNG image files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PNGHandler

        A `wx.ImageHandler` for PNG image files.
        """
        this = __core.new_PNGHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.PNGHandler_swigregister(PNGHandler)

class GIFHandler(ImageHandler):
    """A `wx.ImageHandler` for GIF image files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> GIFHandler

        A `wx.ImageHandler` for GIF image files.
        """
        this = __core.new_GIFHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.GIFHandler_swigregister(GIFHandler)

class PCXHandler(ImageHandler):
    """A `wx.ImageHandler` for PCX imager files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PCXHandler

        A `wx.ImageHandler` for PCX imager files.
        """
        this = __core.new_PCXHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.PCXHandler_swigregister(PCXHandler)

class JPEGHandler(ImageHandler):
    """A `wx.ImageHandler` for JPEG/JPG image files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> JPEGHandler

        A `wx.ImageHandler` for JPEG/JPG image files.
        """
        this = __core.new_JPEGHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.JPEGHandler_swigregister(JPEGHandler)

class PNMHandler(ImageHandler):
    """A `wx.ImageHandler` for PNM image files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PNMHandler

        A `wx.ImageHandler` for PNM image files.
        """
        this = __core.new_PNMHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.PNMHandler_swigregister(PNMHandler)

class XPMHandler(ImageHandler):
    """A `wx.ImageHandler` for XPM image."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> XPMHandler

        A `wx.ImageHandler` for XPM image.
        """
        this = __core.new_XPMHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.XPMHandler_swigregister(XPMHandler)

class TIFFHandler(ImageHandler):
    """A `wx.ImageHandler` for TIFF image files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> TIFFHandler

        A `wx.ImageHandler` for TIFF image files.
        """
        this = __core.new_TIFFHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.TIFFHandler_swigregister(TIFFHandler)

class TGAHandler(ImageHandler):
    """A `wx.ImageHandler` for TGA image files."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> TGAHandler

        A `wx.ImageHandler` for TGA image files.
        """
        this = __core.new_TGAHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.TGAHandler_swigregister(TGAHandler)

QUANTIZE_INCLUDE_WINDOWS_COLOURS = __core.QUANTIZE_INCLUDE_WINDOWS_COLOURS
QUANTIZE_FILL_DESTINATION_IMAGE = __core.QUANTIZE_FILL_DESTINATION_IMAGE
class Quantize(object):
    """Performs quantization, or colour reduction, on a wxImage."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def Quantize(*args, **kwargs):
        """
        Quantize(Image src, Image dest, int desiredNoColours=236, int flags=wxQUANTIZE_INCLUDE_WINDOWS_COLOURS|wxQUANTIZE_FILL_DESTINATION_IMAGE) -> bool

        Reduce the colours in the source image and put the result into the
        destination image, setting the palette in the destination if
        needed. Both images may be the same, to overwrite the source image.
        """
        return __core.Quantize_Quantize(*args, **kwargs)

    Quantize = staticmethod(Quantize)
__core.Quantize_swigregister(Quantize)

def Quantize_Quantize(*args, **kwargs):
  """
    Quantize_Quantize(Image src, Image dest, int desiredNoColours=236, int flags=wxQUANTIZE_INCLUDE_WINDOWS_COLOURS|wxQUANTIZE_FILL_DESTINATION_IMAGE) -> bool

    Reduce the colours in the source image and put the result into the
    destination image, setting the palette in the destination if
    needed. Both images may be the same, to overwrite the source image.
    """
  return __core.Quantize_Quantize(*args, **kwargs)

#---------------------------------------------------------------------------

class EvtHandler(Object):
    """Proxy of C++ EvtHandler class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> EvtHandler"""
        this = __core.new_EvtHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def GetNextHandler(*args, **kwargs):
        """GetNextHandler(self) -> EvtHandler"""
        return __core.EvtHandler_GetNextHandler(*args, **kwargs)

    def GetPreviousHandler(*args, **kwargs):
        """GetPreviousHandler(self) -> EvtHandler"""
        return __core.EvtHandler_GetPreviousHandler(*args, **kwargs)

    def SetNextHandler(*args, **kwargs):
        """SetNextHandler(self, EvtHandler handler)"""
        return __core.EvtHandler_SetNextHandler(*args, **kwargs)

    def SetPreviousHandler(*args, **kwargs):
        """SetPreviousHandler(self, EvtHandler handler)"""
        return __core.EvtHandler_SetPreviousHandler(*args, **kwargs)

    def GetEvtHandlerEnabled(*args, **kwargs):
        """GetEvtHandlerEnabled(self) -> bool"""
        return __core.EvtHandler_GetEvtHandlerEnabled(*args, **kwargs)

    def SetEvtHandlerEnabled(*args, **kwargs):
        """SetEvtHandlerEnabled(self, bool enabled)"""
        return __core.EvtHandler_SetEvtHandlerEnabled(*args, **kwargs)

    def Unlink(*args, **kwargs):
        """Unlink(self)"""
        return __core.EvtHandler_Unlink(*args, **kwargs)

    def IsUnlinked(*args, **kwargs):
        """IsUnlinked(self) -> bool"""
        return __core.EvtHandler_IsUnlinked(*args, **kwargs)

    def ProcessEvent(*args, **kwargs):
        """ProcessEvent(self, Event event) -> bool"""
        return __core.EvtHandler_ProcessEvent(*args, **kwargs)

    def SafelyProcessEvent(*args, **kwargs):
        """SafelyProcessEvent(self, Event event) -> bool"""
        return __core.EvtHandler_SafelyProcessEvent(*args, **kwargs)

    def ProcessEventLocally(*args, **kwargs):
        """ProcessEventLocally(self, Event event) -> bool"""
        return __core.EvtHandler_ProcessEventLocally(*args, **kwargs)

    def QueueEvent(*args, **kwargs):
        """QueueEvent(self, Event event)"""
        return __core.EvtHandler_QueueEvent(*args, **kwargs)

    def AddPendingEvent(*args, **kwargs):
        """AddPendingEvent(self, Event event)"""
        return __core.EvtHandler_AddPendingEvent(*args, **kwargs)

    def ProcessPendingEvents(*args, **kwargs):
        """ProcessPendingEvents(self)"""
        return __core.EvtHandler_ProcessPendingEvents(*args, **kwargs)

    def DeletePendingEvents(*args, **kwargs):
        """DeletePendingEvents(self)"""
        return __core.EvtHandler_DeletePendingEvents(*args, **kwargs)

    def Connect(*args, **kwargs):
        """Connect(self, int id, int lastId, EventType eventType, PyObject func)"""
        return __core.EvtHandler_Connect(*args, **kwargs)

    def Disconnect(*args, **kwargs):
        """
        Disconnect(self, int id, int lastId=-1, EventType eventType=wxEVT_NULL, 
            PyObject func=None) -> bool
        """
        return __core.EvtHandler_Disconnect(*args, **kwargs)

    def _setOORInfo(*args, **kwargs):
        """_setOORInfo(self, PyObject _self, bool incref=True)"""
        val = __core.EvtHandler__setOORInfo(*args, **kwargs)
        args[0].this.own(False)
        return val

    def Bind(self, event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY):
        """
        Bind an event to an event handler.

        :param event: One of the EVT_* objects that specifies the
                      type of event to bind,

        :param handler: A callable object to be invoked when the
                      event is delivered to self.  Pass None to
                      disconnect an event handler.

        :param source: Sometimes the event originates from a
                      different window than self, but you still
                      want to catch it in self.  (For example, a
                      button event delivered to a frame.)  By
                      passing the source of the event, the event
                      handling system is able to differentiate
                      between the same event type from different
                      controls.

        :param id: Used to spcify the event source by ID instead
                   of instance.

        :param id2: Used when it is desirable to bind a handler
                      to a range of IDs, such as with EVT_MENU_RANGE.
        """
        assert isinstance(event, wx.PyEventBinder)
        assert handler is None or callable(handler)
        assert source is None or hasattr(source, 'GetId')
        if source is not None:
            id  = source.GetId()
        event.Bind(self, id, id2, handler)              

    def Unbind(self, event, source=None, id=wx.ID_ANY, id2=wx.ID_ANY, handler=None):
        """
        Disconnects the event handler binding for event from self.
        Returns True if successful.
        """
        if source is not None:
            id  = source.GetId()
        return event.Unbind(self, id, id2, handler)              

    EvtHandlerEnabled = property(GetEvtHandlerEnabled,SetEvtHandlerEnabled,doc="See `GetEvtHandlerEnabled` and `SetEvtHandlerEnabled`") 
    NextHandler = property(GetNextHandler,SetNextHandler,doc="See `GetNextHandler` and `SetNextHandler`") 
    PreviousHandler = property(GetPreviousHandler,SetPreviousHandler,doc="See `GetPreviousHandler` and `SetPreviousHandler`") 
__core.EvtHandler_swigregister(EvtHandler)

class PyEvtHandler(EvtHandler):
    """
    The wx.PyEvtHandler class can be used to intercept calls to the
    `ProcessEvent` method.  Simply derive a new class from this one,
    override ProcessEvent, and then push an instance of the class onto the
    event handler chain for a window using `wx.Window.PushEventHandler`.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PyEvtHandler

        The wx.PyEvtHandler class can be used to intercept calls to the
        `ProcessEvent` method.  Simply derive a new class from this one,
        override ProcessEvent, and then push an instance of the class onto the
        event handler chain for a window using `wx.Window.PushEventHandler`.
        """
        this = __core.new_PyEvtHandler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self);PyEvtHandler._setCallbackInfo(self, self, PyEvtHandler)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return __core.PyEvtHandler__setCallbackInfo(*args, **kwargs)

    def ProcessEvent(*args, **kwargs):
        """
        ProcessEvent(self, Event event) -> bool

        Override this method to intercept the events being sent to the window.
        The default implementation searches the event tables and calls event
        handler functions if matching event bindings are found.
        """
        return __core.PyEvtHandler_ProcessEvent(*args, **kwargs)

__core.PyEvtHandler_swigregister(PyEvtHandler)

#---------------------------------------------------------------------------

class KeyboardState(object):
    """wx.KeyboardState stores the state of the keyboard modifier keys"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, bool controlDown=False, bool shiftDown=False, bool altDown=False, 
            bool metaDown=False) -> KeyboardState

        wx.KeyboardState stores the state of the keyboard modifier keys
        """
        this = __core.new_KeyboardState(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_KeyboardState
    __del__ = lambda self : None;
    def GetModifiers(*args, **kwargs):
        """
        GetModifiers(self) -> int

        Returns a bitmask of the current modifier settings.  Can be used to
        check if the key event has exactly the given modifiers without having
        to explicitly check that the other modifiers are not down.  For
        example::

            if event.GetModifers() == wx.MOD_CONTROL:
                DoSomething()

        """
        return __core.KeyboardState_GetModifiers(*args, **kwargs)

    Modifiers = property(GetModifiers,doc="See `GetModifiers`") 
    def ControlDown(*args, **kwargs):
        """
        ControlDown(self) -> bool

        Returns ``True`` if the Control key was down at the time of the event.
        """
        return __core.KeyboardState_ControlDown(*args, **kwargs)

    def RawControlDown(*args, **kwargs):
        """RawControlDown(self) -> bool"""
        return __core.KeyboardState_RawControlDown(*args, **kwargs)

    def SetRawControlDown(*args, **kwargs):
        """SetRawControlDown(self, bool down)"""
        return __core.KeyboardState_SetRawControlDown(*args, **kwargs)

    def MetaDown(*args, **kwargs):
        """
        MetaDown(self) -> bool

        Returns ``True`` if the Meta key was down at the time of the event.
        """
        return __core.KeyboardState_MetaDown(*args, **kwargs)

    def AltDown(*args, **kwargs):
        """
        AltDown(self) -> bool

        Returns ``True`` if the Alt key was down at the time of the event.
        """
        return __core.KeyboardState_AltDown(*args, **kwargs)

    def ShiftDown(*args, **kwargs):
        """
        ShiftDown(self) -> bool

        Returns ``True`` if the Shift key was down at the time of the event.
        """
        return __core.KeyboardState_ShiftDown(*args, **kwargs)

    def CmdDown(*args, **kwargs):
        """
        CmdDown(self) -> bool

        "Cmd" is a pseudo key which is the same as Control for PC and Unix
        platforms but the special "Apple" (a.k.a as "Command") key on
        Macs. It makes often sense to use it instead of, say, `ControlDown`
        because Cmd key is used for the same thing under Mac as Ctrl
        elsewhere. The Ctrl still exists, it's just not used for this
        purpose. So for non-Mac platforms this is the same as `ControlDown`
        and Macs this is the same as `MetaDown`.
        """
        return __core.KeyboardState_CmdDown(*args, **kwargs)

    def HasModifiers(*args, **kwargs):
        """
        HasModifiers(self) -> bool

        Returns true if either CTRL or ALT keys was down at the time of the
        key event. Note that this function does not take into account neither
        SHIFT nor META key states (the reason for ignoring the latter is that
        it is common for NUMLOCK key to be configured as META under X but the
        key presses even while NUMLOCK is on should be still processed
        normally).
        """
        return __core.KeyboardState_HasModifiers(*args, **kwargs)

    def SetControlDown(*args, **kwargs):
        """SetControlDown(self, bool down)"""
        return __core.KeyboardState_SetControlDown(*args, **kwargs)

    def SetShiftDown(*args, **kwargs):
        """SetShiftDown(self, bool down)"""
        return __core.KeyboardState_SetShiftDown(*args, **kwargs)

    def SetAltDown(*args, **kwargs):
        """SetAltDown(self, bool down)"""
        return __core.KeyboardState_SetAltDown(*args, **kwargs)

    def SetMetaDown(*args, **kwargs):
        """SetMetaDown(self, bool down)"""
        return __core.KeyboardState_SetMetaDown(*args, **kwargs)

    controlDown = property(ControlDown, SetControlDown)
    rawControlDown = property(RawControlDown, SetRawControlDown)
    shiftDown = property(ShiftDown, SetShiftDown)
    altDown = property(AltDown, SetAltDown)
    metaDown = property(MetaDown, SetMetaDown)
    cmdDown = property(CmdDown)


    m_controlDown = wx.deprecated(controlDown)
    m_shiftDown = wx.deprecated(shiftDown)
    m_altDown = wx.deprecated(altDown)
    m_metaDown = wx.deprecated(metaDown)            

__core.KeyboardState_swigregister(KeyboardState)

#---------------------------------------------------------------------------

MOUSE_BTN_ANY = __core.MOUSE_BTN_ANY
MOUSE_BTN_NONE = __core.MOUSE_BTN_NONE
MOUSE_BTN_LEFT = __core.MOUSE_BTN_LEFT
MOUSE_BTN_MIDDLE = __core.MOUSE_BTN_MIDDLE
MOUSE_BTN_RIGHT = __core.MOUSE_BTN_RIGHT
MOUSE_BTN_AUX1 = __core.MOUSE_BTN_AUX1
MOUSE_BTN_AUX2 = __core.MOUSE_BTN_AUX2
MOUSE_BTN_MAX = __core.MOUSE_BTN_MAX
class MouseState(KeyboardState):
    """
    `wx.MouseState` is used to hold information about mouse button and
    modifier key states and is what is returned from `wx.GetMouseState`.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> MouseState

        `wx.MouseState` is used to hold information about mouse button and
        modifier key states and is what is returned from `wx.GetMouseState`.
        """
        this = __core.new_MouseState(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_MouseState
    __del__ = lambda self : None;
    def GetX(*args, **kwargs):
        """GetX(self) -> int"""
        return __core.MouseState_GetX(*args, **kwargs)

    def GetY(*args, **kwargs):
        """GetY(self) -> int"""
        return __core.MouseState_GetY(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """GetPosition(self) -> Point"""
        return __core.MouseState_GetPosition(*args, **kwargs)

    def GetPositionTuple(*args, **kwargs):
        """GetPositionTuple() -> (x,y)"""
        return __core.MouseState_GetPositionTuple(*args, **kwargs)

    def LeftIsDown(*args, **kwargs):
        """LeftIsDown(self) -> bool"""
        return __core.MouseState_LeftIsDown(*args, **kwargs)

    def MiddleIsDown(*args, **kwargs):
        """MiddleIsDown(self) -> bool"""
        return __core.MouseState_MiddleIsDown(*args, **kwargs)

    def RightIsDown(*args, **kwargs):
        """RightIsDown(self) -> bool"""
        return __core.MouseState_RightIsDown(*args, **kwargs)

    def Aux1IsDown(*args, **kwargs):
        """Aux1IsDown(self) -> bool"""
        return __core.MouseState_Aux1IsDown(*args, **kwargs)

    def Aux2IsDown(*args, **kwargs):
        """Aux2IsDown(self) -> bool"""
        return __core.MouseState_Aux2IsDown(*args, **kwargs)

    def ButtonIsDown(*args, **kwargs):
        """ButtonIsDown(self, int but) -> bool"""
        return __core.MouseState_ButtonIsDown(*args, **kwargs)

    LeftDown = wx.deprecated(LeftIsDown)
    MiddleDown = wx.deprecated(MiddleIsDown)
    RightDown = wx.deprecated(RightIsDown)            

    def SetX(*args, **kwargs):
        """SetX(self, int x)"""
        return __core.MouseState_SetX(*args, **kwargs)

    def SetY(*args, **kwargs):
        """SetY(self, int y)"""
        return __core.MouseState_SetY(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, Point pos)"""
        return __core.MouseState_SetPosition(*args, **kwargs)

    def SetLeftDown(*args, **kwargs):
        """SetLeftDown(self, bool down)"""
        return __core.MouseState_SetLeftDown(*args, **kwargs)

    def SetMiddleDown(*args, **kwargs):
        """SetMiddleDown(self, bool down)"""
        return __core.MouseState_SetMiddleDown(*args, **kwargs)

    def SetRightDown(*args, **kwargs):
        """SetRightDown(self, bool down)"""
        return __core.MouseState_SetRightDown(*args, **kwargs)

    def SetAux1Down(*args, **kwargs):
        """SetAux1Down(self, bool down)"""
        return __core.MouseState_SetAux1Down(*args, **kwargs)

    def SetAux2Down(*args, **kwargs):
        """SetAux2Down(self, bool down)"""
        return __core.MouseState_SetAux2Down(*args, **kwargs)

    def SetState(*args, **kwargs):
        """SetState(self, MouseState state)"""
        return __core.MouseState_SetState(*args, **kwargs)

    x = property(GetX, SetX)
    y = property(GetY, SetY)
    X = property(GetX, SetX)  # uppercase versions for 2.8 compatibility
    Y = property(GetY, SetY)
    leftIsDown = property(LeftIsDown, SetLeftDown)
    middleIsDown = property(MiddleIsDown, SetMiddleDown)
    rightIsDown = property(RightIsDown, SetRightDown)
    aux1IsDown = property(Aux1IsDown, SetAux1Down)
    aux2IsDown = property(Aux2IsDown, SetAux2Down)


    m_leftDown = wx.deprecated(leftIsDown)
    m_middleDown = wx.deprecated(middleIsDown)
    m_rightDown = wx.deprecated(rightIsDown)
    m_aux1Down = wx.deprecated(aux1IsDown)
    m_aux2Down = wx.deprecated(aux2IsDown)
    m_x = wx.deprecated(x)
    m_y = wx.deprecated(y)

    Position = property(GetPosition,doc="See `GetPosition`") 
__core.MouseState_swigregister(MouseState)


def GetMouseState(*args):
  """
    GetMouseState() -> MouseState

    Returns the current state of the mouse.  Returns an instance of a
    `wx.MouseState` object that contains the current position of the mouse
    pointer in screen coordinants, as well as boolean values indicating
    the up/down status of the mouse buttons and the modifier keys.
    """
  return __core.GetMouseState(*args)
#---------------------------------------------------------------------------

class PyEventBinder(object):
    """
    Instances of this class are used to bind specific events to event
    handlers.
    """
    def __init__(self, evtType, expectedIDs=0):
        if expectedIDs not in [0, 1, 2]:
            raise ValueError, "Invalid number of expectedIDs"
        self.expectedIDs = expectedIDs

        if type(evtType) == list or type(evtType) == tuple:
            self.evtType = evtType
        else:
            self.evtType = [evtType]


    def Bind(self, target, id1, id2, function):
        """Bind this set of event types to target."""
        for et in self.evtType:
            target.Connect(id1, id2, et, function)


    def Unbind(self, target, id1, id2, handler=None):
        """Remove an event binding."""
        success = 0
        for et in self.evtType:
            success += target.Disconnect(id1, id2, et, handler)
        return success != 0

    def _getEvtType(self):
        """
        Make it easy to get to the default wxEventType typeID for this
        event binder.
        """
        return self.evtType[0]
    
    typeId = property(_getEvtType)

    
    def __call__(self, *args):
        """
        For backwards compatibility with the old EVT_* functions.
        Should be called with either (window, func), (window, ID,
        func) or (window, ID1, ID2, func) parameters depending on the
        type of the event.
        """
        assert len(args) == 2 + self.expectedIDs
        id1 = wx.ID_ANY
        id2 = wx.ID_ANY
        target = args[0]
        if self.expectedIDs == 0:
            func = args[1]
        elif self.expectedIDs == 1:
            id1 = args[1]
            func = args[2]
        elif self.expectedIDs == 2:
            id1 = args[1]
            id2 = args[2]
            func = args[3]
        else:
            raise ValueError, "Unexpected number of IDs"

        self.Bind(target, id1, id2, func)


# These two are square pegs that don't fit the PyEventBinder hole...
def EVT_COMMAND(win, id, cmd, func):
    win.Connect(id, -1, cmd, func)
def EVT_COMMAND_RANGE(win, id1, id2, cmd, func):
    win.Connect(id1, id2, cmd, func)

    
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------

EVENT_PROPAGATE_NONE = __core.EVENT_PROPAGATE_NONE
EVENT_PROPAGATE_MAX = __core.EVENT_PROPAGATE_MAX
wxEVT_CATEGORY_UI = __core.wxEVT_CATEGORY_UI
wxEVT_CATEGORY_USER_INPUT = __core.wxEVT_CATEGORY_USER_INPUT
wxEVT_CATEGORY_SOCKET = __core.wxEVT_CATEGORY_SOCKET
wxEVT_CATEGORY_TIMER = __core.wxEVT_CATEGORY_TIMER
wxEVT_CATEGORY_THREAD = __core.wxEVT_CATEGORY_THREAD
wxEVT_CATEGORY_UNKNOWN = __core.wxEVT_CATEGORY_UNKNOWN
wxEVT_CATEGORY_CLIPBOARD = __core.wxEVT_CATEGORY_CLIPBOARD
wxEVT_CATEGORY_NATIVE_EVENTS = __core.wxEVT_CATEGORY_NATIVE_EVENTS
wxEVT_CATEGORY_ALL = __core.wxEVT_CATEGORY_ALL

def NewEventType(*args):
  """NewEventType() -> EventType"""
  return __core.NewEventType(*args)
wxEVT_ANY = __core.wxEVT_ANY
wxEVT_NULL = __core.wxEVT_NULL
wxEVT_FIRST = __core.wxEVT_FIRST
wxEVT_USER_FIRST = __core.wxEVT_USER_FIRST
wxEVT_COMMAND_BUTTON_CLICKED = __core.wxEVT_COMMAND_BUTTON_CLICKED
wxEVT_COMMAND_CHECKBOX_CLICKED = __core.wxEVT_COMMAND_CHECKBOX_CLICKED
wxEVT_COMMAND_CHOICE_SELECTED = __core.wxEVT_COMMAND_CHOICE_SELECTED
wxEVT_COMMAND_LISTBOX_SELECTED = __core.wxEVT_COMMAND_LISTBOX_SELECTED
wxEVT_COMMAND_LISTBOX_DOUBLECLICKED = __core.wxEVT_COMMAND_LISTBOX_DOUBLECLICKED
wxEVT_COMMAND_CHECKLISTBOX_TOGGLED = __core.wxEVT_COMMAND_CHECKLISTBOX_TOGGLED
wxEVT_COMMAND_MENU_SELECTED = __core.wxEVT_COMMAND_MENU_SELECTED
wxEVT_COMMAND_TOOL_CLICKED = __core.wxEVT_COMMAND_TOOL_CLICKED
wxEVT_COMMAND_SLIDER_UPDATED = __core.wxEVT_COMMAND_SLIDER_UPDATED
wxEVT_COMMAND_RADIOBOX_SELECTED = __core.wxEVT_COMMAND_RADIOBOX_SELECTED
wxEVT_COMMAND_RADIOBUTTON_SELECTED = __core.wxEVT_COMMAND_RADIOBUTTON_SELECTED
wxEVT_COMMAND_SCROLLBAR_UPDATED = __core.wxEVT_COMMAND_SCROLLBAR_UPDATED
wxEVT_COMMAND_VLBOX_SELECTED = __core.wxEVT_COMMAND_VLBOX_SELECTED
wxEVT_COMMAND_COMBOBOX_SELECTED = __core.wxEVT_COMMAND_COMBOBOX_SELECTED
wxEVT_COMMAND_TOOL_RCLICKED = __core.wxEVT_COMMAND_TOOL_RCLICKED
wxEVT_COMMAND_TOOL_ENTER = __core.wxEVT_COMMAND_TOOL_ENTER
wxEVT_COMMAND_TOOL_DROPDOWN_CLICKED = __core.wxEVT_COMMAND_TOOL_DROPDOWN_CLICKED
wxEVT_COMMAND_COMBOBOX_DROPDOWN = __core.wxEVT_COMMAND_COMBOBOX_DROPDOWN
wxEVT_COMMAND_COMBOBOX_CLOSEUP = __core.wxEVT_COMMAND_COMBOBOX_CLOSEUP
wxEVT_THREAD = __core.wxEVT_THREAD
wxEVT_LEFT_DOWN = __core.wxEVT_LEFT_DOWN
wxEVT_LEFT_UP = __core.wxEVT_LEFT_UP
wxEVT_MIDDLE_DOWN = __core.wxEVT_MIDDLE_DOWN
wxEVT_MIDDLE_UP = __core.wxEVT_MIDDLE_UP
wxEVT_RIGHT_DOWN = __core.wxEVT_RIGHT_DOWN
wxEVT_RIGHT_UP = __core.wxEVT_RIGHT_UP
wxEVT_MOTION = __core.wxEVT_MOTION
wxEVT_ENTER_WINDOW = __core.wxEVT_ENTER_WINDOW
wxEVT_LEAVE_WINDOW = __core.wxEVT_LEAVE_WINDOW
wxEVT_LEFT_DCLICK = __core.wxEVT_LEFT_DCLICK
wxEVT_MIDDLE_DCLICK = __core.wxEVT_MIDDLE_DCLICK
wxEVT_RIGHT_DCLICK = __core.wxEVT_RIGHT_DCLICK
wxEVT_SET_FOCUS = __core.wxEVT_SET_FOCUS
wxEVT_KILL_FOCUS = __core.wxEVT_KILL_FOCUS
wxEVT_CHILD_FOCUS = __core.wxEVT_CHILD_FOCUS
wxEVT_MOUSEWHEEL = __core.wxEVT_MOUSEWHEEL
wxEVT_AUX1_DOWN = __core.wxEVT_AUX1_DOWN
wxEVT_AUX1_UP = __core.wxEVT_AUX1_UP
wxEVT_AUX1_DCLICK = __core.wxEVT_AUX1_DCLICK
wxEVT_AUX2_DOWN = __core.wxEVT_AUX2_DOWN
wxEVT_AUX2_UP = __core.wxEVT_AUX2_UP
wxEVT_AUX2_DCLICK = __core.wxEVT_AUX2_DCLICK
wxEVT_CHAR = __core.wxEVT_CHAR
wxEVT_CHAR_HOOK = __core.wxEVT_CHAR_HOOK
wxEVT_NAVIGATION_KEY = __core.wxEVT_NAVIGATION_KEY
wxEVT_KEY_DOWN = __core.wxEVT_KEY_DOWN
wxEVT_KEY_UP = __core.wxEVT_KEY_UP
wxEVT_HOTKEY = __core.wxEVT_HOTKEY
wxEVT_SET_CURSOR = __core.wxEVT_SET_CURSOR
wxEVT_SCROLL_TOP = __core.wxEVT_SCROLL_TOP
wxEVT_SCROLL_BOTTOM = __core.wxEVT_SCROLL_BOTTOM
wxEVT_SCROLL_LINEUP = __core.wxEVT_SCROLL_LINEUP
wxEVT_SCROLL_LINEDOWN = __core.wxEVT_SCROLL_LINEDOWN
wxEVT_SCROLL_PAGEUP = __core.wxEVT_SCROLL_PAGEUP
wxEVT_SCROLL_PAGEDOWN = __core.wxEVT_SCROLL_PAGEDOWN
wxEVT_SCROLL_THUMBTRACK = __core.wxEVT_SCROLL_THUMBTRACK
wxEVT_SCROLL_THUMBRELEASE = __core.wxEVT_SCROLL_THUMBRELEASE
wxEVT_SCROLL_CHANGED = __core.wxEVT_SCROLL_CHANGED
wxEVT_SCROLL_ENDSCROLL = wxEVT_SCROLL_CHANGED 
wxEVT_SCROLLWIN_TOP = __core.wxEVT_SCROLLWIN_TOP
wxEVT_SCROLLWIN_BOTTOM = __core.wxEVT_SCROLLWIN_BOTTOM
wxEVT_SCROLLWIN_LINEUP = __core.wxEVT_SCROLLWIN_LINEUP
wxEVT_SCROLLWIN_LINEDOWN = __core.wxEVT_SCROLLWIN_LINEDOWN
wxEVT_SCROLLWIN_PAGEUP = __core.wxEVT_SCROLLWIN_PAGEUP
wxEVT_SCROLLWIN_PAGEDOWN = __core.wxEVT_SCROLLWIN_PAGEDOWN
wxEVT_SCROLLWIN_THUMBTRACK = __core.wxEVT_SCROLLWIN_THUMBTRACK
wxEVT_SCROLLWIN_THUMBRELEASE = __core.wxEVT_SCROLLWIN_THUMBRELEASE
wxEVT_SIZE = __core.wxEVT_SIZE
wxEVT_MOVE = __core.wxEVT_MOVE
wxEVT_CLOSE_WINDOW = __core.wxEVT_CLOSE_WINDOW
wxEVT_END_SESSION = __core.wxEVT_END_SESSION
wxEVT_QUERY_END_SESSION = __core.wxEVT_QUERY_END_SESSION
wxEVT_ACTIVATE_APP = __core.wxEVT_ACTIVATE_APP
wxEVT_ACTIVATE = __core.wxEVT_ACTIVATE
wxEVT_CREATE = __core.wxEVT_CREATE
wxEVT_DESTROY = __core.wxEVT_DESTROY
wxEVT_SHOW = __core.wxEVT_SHOW
wxEVT_ICONIZE = __core.wxEVT_ICONIZE
wxEVT_MAXIMIZE = __core.wxEVT_MAXIMIZE
wxEVT_MOUSE_CAPTURE_CHANGED = __core.wxEVT_MOUSE_CAPTURE_CHANGED
wxEVT_MOUSE_CAPTURE_LOST = __core.wxEVT_MOUSE_CAPTURE_LOST
wxEVT_PAINT = __core.wxEVT_PAINT
wxEVT_ERASE_BACKGROUND = __core.wxEVT_ERASE_BACKGROUND
wxEVT_NC_PAINT = __core.wxEVT_NC_PAINT
wxEVT_MENU_OPEN = __core.wxEVT_MENU_OPEN
wxEVT_MENU_CLOSE = __core.wxEVT_MENU_CLOSE
wxEVT_MENU_HIGHLIGHT = __core.wxEVT_MENU_HIGHLIGHT
wxEVT_CONTEXT_MENU = __core.wxEVT_CONTEXT_MENU
wxEVT_SYS_COLOUR_CHANGED = __core.wxEVT_SYS_COLOUR_CHANGED
wxEVT_DISPLAY_CHANGED = __core.wxEVT_DISPLAY_CHANGED
wxEVT_QUERY_NEW_PALETTE = __core.wxEVT_QUERY_NEW_PALETTE
wxEVT_PALETTE_CHANGED = __core.wxEVT_PALETTE_CHANGED
wxEVT_DROP_FILES = __core.wxEVT_DROP_FILES
wxEVT_INIT_DIALOG = __core.wxEVT_INIT_DIALOG
wxEVT_IDLE = __core.wxEVT_IDLE
wxEVT_UPDATE_UI = __core.wxEVT_UPDATE_UI
wxEVT_SIZING = __core.wxEVT_SIZING
wxEVT_MOVING = __core.wxEVT_MOVING
wxEVT_MOVE_START = __core.wxEVT_MOVE_START
wxEVT_MOVE_END = __core.wxEVT_MOVE_END
wxEVT_HIBERNATE = __core.wxEVT_HIBERNATE
wxEVT_COMMAND_TEXT_COPY = __core.wxEVT_COMMAND_TEXT_COPY
wxEVT_COMMAND_TEXT_CUT = __core.wxEVT_COMMAND_TEXT_CUT
wxEVT_COMMAND_TEXT_PASTE = __core.wxEVT_COMMAND_TEXT_PASTE
wxEVT_COMMAND_LEFT_CLICK = __core.wxEVT_COMMAND_LEFT_CLICK
wxEVT_COMMAND_LEFT_DCLICK = __core.wxEVT_COMMAND_LEFT_DCLICK
wxEVT_COMMAND_RIGHT_CLICK = __core.wxEVT_COMMAND_RIGHT_CLICK
wxEVT_COMMAND_RIGHT_DCLICK = __core.wxEVT_COMMAND_RIGHT_DCLICK
wxEVT_COMMAND_SET_FOCUS = __core.wxEVT_COMMAND_SET_FOCUS
wxEVT_COMMAND_KILL_FOCUS = __core.wxEVT_COMMAND_KILL_FOCUS
wxEVT_COMMAND_ENTER = __core.wxEVT_COMMAND_ENTER
#
# Create some event binders
EVT_SIZE = wx.PyEventBinder( wxEVT_SIZE )
EVT_SIZING = wx.PyEventBinder( wxEVT_SIZING )
EVT_MOVE = wx.PyEventBinder( wxEVT_MOVE )
EVT_MOVING = wx.PyEventBinder( wxEVT_MOVING )
EVT_MOVE_START = wx.PyEventBinder( wxEVT_MOVE_START )
EVT_MOVE_END = wx.PyEventBinder( wxEVT_MOVE_END )
EVT_CLOSE = wx.PyEventBinder( wxEVT_CLOSE_WINDOW )
EVT_END_SESSION = wx.PyEventBinder( wxEVT_END_SESSION )
EVT_QUERY_END_SESSION = wx.PyEventBinder( wxEVT_QUERY_END_SESSION )
EVT_PAINT = wx.PyEventBinder( wxEVT_PAINT )
EVT_NC_PAINT = wx.PyEventBinder( wxEVT_NC_PAINT )
EVT_ERASE_BACKGROUND = wx.PyEventBinder( wxEVT_ERASE_BACKGROUND )
EVT_CHAR = wx.PyEventBinder( wxEVT_CHAR )
EVT_KEY_DOWN = wx.PyEventBinder( wxEVT_KEY_DOWN )
EVT_KEY_UP = wx.PyEventBinder( wxEVT_KEY_UP )
EVT_HOTKEY = wx.PyEventBinder( wxEVT_HOTKEY, 1)
EVT_CHAR_HOOK = wx.PyEventBinder( wxEVT_CHAR_HOOK )
EVT_MENU_OPEN = wx.PyEventBinder( wxEVT_MENU_OPEN )
EVT_MENU_CLOSE = wx.PyEventBinder( wxEVT_MENU_CLOSE )
EVT_MENU_HIGHLIGHT = wx.PyEventBinder( wxEVT_MENU_HIGHLIGHT, 1)
EVT_MENU_HIGHLIGHT_ALL = wx.PyEventBinder( wxEVT_MENU_HIGHLIGHT )
EVT_SET_FOCUS = wx.PyEventBinder( wxEVT_SET_FOCUS )
EVT_KILL_FOCUS = wx.PyEventBinder( wxEVT_KILL_FOCUS )
EVT_CHILD_FOCUS = wx.PyEventBinder( wxEVT_CHILD_FOCUS )
EVT_ACTIVATE = wx.PyEventBinder( wxEVT_ACTIVATE )
EVT_ACTIVATE_APP = wx.PyEventBinder( wxEVT_ACTIVATE_APP )
EVT_HIBERNATE = wx.PyEventBinder( wxEVT_HIBERNATE )
EVT_END_SESSION = wx.PyEventBinder( wxEVT_END_SESSION )
EVT_QUERY_END_SESSION = wx.PyEventBinder( wxEVT_QUERY_END_SESSION )
EVT_DROP_FILES = wx.PyEventBinder( wxEVT_DROP_FILES )
EVT_INIT_DIALOG = wx.PyEventBinder( wxEVT_INIT_DIALOG )
EVT_SYS_COLOUR_CHANGED = wx.PyEventBinder( wxEVT_SYS_COLOUR_CHANGED )
EVT_DISPLAY_CHANGED = wx.PyEventBinder( wxEVT_DISPLAY_CHANGED )
EVT_SHOW = wx.PyEventBinder( wxEVT_SHOW )
EVT_MAXIMIZE = wx.PyEventBinder( wxEVT_MAXIMIZE )
EVT_ICONIZE = wx.PyEventBinder( wxEVT_ICONIZE )
EVT_NAVIGATION_KEY = wx.PyEventBinder( wxEVT_NAVIGATION_KEY )
EVT_PALETTE_CHANGED = wx.PyEventBinder( wxEVT_PALETTE_CHANGED )
EVT_QUERY_NEW_PALETTE = wx.PyEventBinder( wxEVT_QUERY_NEW_PALETTE )
EVT_WINDOW_CREATE = wx.PyEventBinder( wxEVT_CREATE )
EVT_WINDOW_DESTROY = wx.PyEventBinder( wxEVT_DESTROY )
EVT_SET_CURSOR = wx.PyEventBinder( wxEVT_SET_CURSOR )
EVT_MOUSE_CAPTURE_CHANGED = wx.PyEventBinder( wxEVT_MOUSE_CAPTURE_CHANGED )
EVT_MOUSE_CAPTURE_LOST = wx.PyEventBinder( wxEVT_MOUSE_CAPTURE_LOST )

EVT_LEFT_DOWN = wx.PyEventBinder( wxEVT_LEFT_DOWN )
EVT_LEFT_UP = wx.PyEventBinder( wxEVT_LEFT_UP )
EVT_MIDDLE_DOWN = wx.PyEventBinder( wxEVT_MIDDLE_DOWN )
EVT_MIDDLE_UP = wx.PyEventBinder( wxEVT_MIDDLE_UP )
EVT_RIGHT_DOWN = wx.PyEventBinder( wxEVT_RIGHT_DOWN )
EVT_RIGHT_UP = wx.PyEventBinder( wxEVT_RIGHT_UP )
EVT_MOTION = wx.PyEventBinder( wxEVT_MOTION )
EVT_LEFT_DCLICK = wx.PyEventBinder( wxEVT_LEFT_DCLICK )
EVT_MIDDLE_DCLICK = wx.PyEventBinder( wxEVT_MIDDLE_DCLICK )
EVT_RIGHT_DCLICK = wx.PyEventBinder( wxEVT_RIGHT_DCLICK )
EVT_LEAVE_WINDOW = wx.PyEventBinder( wxEVT_LEAVE_WINDOW )
EVT_ENTER_WINDOW = wx.PyEventBinder( wxEVT_ENTER_WINDOW )
EVT_MOUSEWHEEL = wx.PyEventBinder( wxEVT_MOUSEWHEEL )
EVT_MOUSE_AUX1_DOWN = wx.PyEventBinder( wxEVT_AUX1_DOWN )
EVT_MOUSE_AUX1_UP = wx.PyEventBinder( wxEVT_AUX1_UP )
EVT_MOUSE_AUX1_DCLICK = wx.PyEventBinder( wxEVT_AUX1_DCLICK )
EVT_MOUSE_AUX2_DOWN = wx.PyEventBinder( wxEVT_AUX2_DOWN )
EVT_MOUSE_AUX2_UP = wx.PyEventBinder( wxEVT_AUX2_UP )
EVT_MOUSE_AUX2_DCLICK = wx.PyEventBinder( wxEVT_AUX2_DCLICK )

EVT_MOUSE_EVENTS = wx.PyEventBinder([ wxEVT_LEFT_DOWN,
                                      wxEVT_LEFT_UP,
                                      wxEVT_MIDDLE_DOWN,
                                      wxEVT_MIDDLE_UP,
                                      wxEVT_RIGHT_DOWN,
                                      wxEVT_RIGHT_UP,
                                      wxEVT_MOTION,
                                      wxEVT_LEFT_DCLICK,
                                      wxEVT_MIDDLE_DCLICK,
                                      wxEVT_RIGHT_DCLICK,
                                      wxEVT_ENTER_WINDOW,
                                      wxEVT_LEAVE_WINDOW,
                                      wxEVT_MOUSEWHEEL,
                                      wxEVT_AUX1_DOWN,
                                      wxEVT_AUX1_UP,      
                                      wxEVT_AUX1_DCLICK,
                                      wxEVT_AUX2_DOWN,  
                                      wxEVT_AUX2_UP,      
                                      wxEVT_AUX2_DCLICK,
                                     ])


# Scrolling from wxWindow (sent to wxScrolledWindow)
EVT_SCROLLWIN = wx.PyEventBinder([ wxEVT_SCROLLWIN_TOP,
                                  wxEVT_SCROLLWIN_BOTTOM,
                                  wxEVT_SCROLLWIN_LINEUP,
                                  wxEVT_SCROLLWIN_LINEDOWN,
                                  wxEVT_SCROLLWIN_PAGEUP,
                                  wxEVT_SCROLLWIN_PAGEDOWN,
                                  wxEVT_SCROLLWIN_THUMBTRACK,
                                  wxEVT_SCROLLWIN_THUMBRELEASE,
                                  ])

EVT_SCROLLWIN_TOP = wx.PyEventBinder( wxEVT_SCROLLWIN_TOP )
EVT_SCROLLWIN_BOTTOM = wx.PyEventBinder( wxEVT_SCROLLWIN_BOTTOM )
EVT_SCROLLWIN_LINEUP = wx.PyEventBinder( wxEVT_SCROLLWIN_LINEUP )
EVT_SCROLLWIN_LINEDOWN = wx.PyEventBinder( wxEVT_SCROLLWIN_LINEDOWN )
EVT_SCROLLWIN_PAGEUP = wx.PyEventBinder( wxEVT_SCROLLWIN_PAGEUP )
EVT_SCROLLWIN_PAGEDOWN = wx.PyEventBinder( wxEVT_SCROLLWIN_PAGEDOWN )
EVT_SCROLLWIN_THUMBTRACK = wx.PyEventBinder( wxEVT_SCROLLWIN_THUMBTRACK )
EVT_SCROLLWIN_THUMBRELEASE = wx.PyEventBinder( wxEVT_SCROLLWIN_THUMBRELEASE )

# Scrolling from wx.Slider and wx.ScrollBar
EVT_SCROLL = wx.PyEventBinder([ wxEVT_SCROLL_TOP,
                               wxEVT_SCROLL_BOTTOM,
                               wxEVT_SCROLL_LINEUP,
                               wxEVT_SCROLL_LINEDOWN,
                               wxEVT_SCROLL_PAGEUP,
                               wxEVT_SCROLL_PAGEDOWN,
                               wxEVT_SCROLL_THUMBTRACK,
                               wxEVT_SCROLL_THUMBRELEASE,
                               wxEVT_SCROLL_CHANGED,
                               ])

EVT_SCROLL_TOP = wx.PyEventBinder( wxEVT_SCROLL_TOP )
EVT_SCROLL_BOTTOM = wx.PyEventBinder( wxEVT_SCROLL_BOTTOM )
EVT_SCROLL_LINEUP = wx.PyEventBinder( wxEVT_SCROLL_LINEUP )
EVT_SCROLL_LINEDOWN = wx.PyEventBinder( wxEVT_SCROLL_LINEDOWN )
EVT_SCROLL_PAGEUP = wx.PyEventBinder( wxEVT_SCROLL_PAGEUP )
EVT_SCROLL_PAGEDOWN = wx.PyEventBinder( wxEVT_SCROLL_PAGEDOWN )
EVT_SCROLL_THUMBTRACK = wx.PyEventBinder( wxEVT_SCROLL_THUMBTRACK )
EVT_SCROLL_THUMBRELEASE = wx.PyEventBinder( wxEVT_SCROLL_THUMBRELEASE )
EVT_SCROLL_CHANGED = wx.PyEventBinder( wxEVT_SCROLL_CHANGED )
EVT_SCROLL_ENDSCROLL = EVT_SCROLL_CHANGED

# Scrolling from wx.Slider and wx.ScrollBar, with an id
EVT_COMMAND_SCROLL = wx.PyEventBinder([ wxEVT_SCROLL_TOP,
                                       wxEVT_SCROLL_BOTTOM,
                                       wxEVT_SCROLL_LINEUP,
                                       wxEVT_SCROLL_LINEDOWN,
                                       wxEVT_SCROLL_PAGEUP,
                                       wxEVT_SCROLL_PAGEDOWN,
                                       wxEVT_SCROLL_THUMBTRACK,
                                       wxEVT_SCROLL_THUMBRELEASE,
                                       wxEVT_SCROLL_CHANGED,
                                       ], 1)

EVT_COMMAND_SCROLL_TOP = wx.PyEventBinder( wxEVT_SCROLL_TOP, 1)
EVT_COMMAND_SCROLL_BOTTOM = wx.PyEventBinder( wxEVT_SCROLL_BOTTOM, 1)
EVT_COMMAND_SCROLL_LINEUP = wx.PyEventBinder( wxEVT_SCROLL_LINEUP, 1)
EVT_COMMAND_SCROLL_LINEDOWN = wx.PyEventBinder( wxEVT_SCROLL_LINEDOWN, 1)
EVT_COMMAND_SCROLL_PAGEUP = wx.PyEventBinder( wxEVT_SCROLL_PAGEUP, 1)
EVT_COMMAND_SCROLL_PAGEDOWN = wx.PyEventBinder( wxEVT_SCROLL_PAGEDOWN, 1)
EVT_COMMAND_SCROLL_THUMBTRACK = wx.PyEventBinder( wxEVT_SCROLL_THUMBTRACK, 1)
EVT_COMMAND_SCROLL_THUMBRELEASE = wx.PyEventBinder( wxEVT_SCROLL_THUMBRELEASE, 1)
EVT_COMMAND_SCROLL_CHANGED = wx.PyEventBinder( wxEVT_SCROLL_CHANGED, 1)
EVT_COMMAND_SCROLL_ENDSCROLL = EVT_COMMAND_SCROLL_CHANGED

EVT_BUTTON = wx.PyEventBinder( wxEVT_COMMAND_BUTTON_CLICKED, 1)
EVT_CHECKBOX = wx.PyEventBinder( wxEVT_COMMAND_CHECKBOX_CLICKED, 1)
EVT_CHOICE = wx.PyEventBinder( wxEVT_COMMAND_CHOICE_SELECTED, 1)
EVT_LISTBOX = wx.PyEventBinder( wxEVT_COMMAND_LISTBOX_SELECTED, 1)
EVT_LISTBOX_DCLICK = wx.PyEventBinder( wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, 1)
EVT_MENU = wx.PyEventBinder( wxEVT_COMMAND_MENU_SELECTED, 1)
EVT_MENU_RANGE = wx.PyEventBinder( wxEVT_COMMAND_MENU_SELECTED, 2)
EVT_SLIDER = wx.PyEventBinder( wxEVT_COMMAND_SLIDER_UPDATED, 1)
EVT_RADIOBOX = wx.PyEventBinder( wxEVT_COMMAND_RADIOBOX_SELECTED, 1)
EVT_RADIOBUTTON = wx.PyEventBinder( wxEVT_COMMAND_RADIOBUTTON_SELECTED, 1)

EVT_SCROLLBAR = wx.PyEventBinder( wxEVT_COMMAND_SCROLLBAR_UPDATED, 1)
EVT_VLBOX = wx.PyEventBinder( wxEVT_COMMAND_VLBOX_SELECTED, 1)
EVT_COMBOBOX = wx.PyEventBinder( wxEVT_COMMAND_COMBOBOX_SELECTED, 1)
EVT_TOOL = wx.PyEventBinder( wxEVT_COMMAND_TOOL_CLICKED, 1)
EVT_TOOL_RANGE = wx.PyEventBinder( wxEVT_COMMAND_TOOL_CLICKED, 2)
EVT_TOOL_RCLICKED = wx.PyEventBinder( wxEVT_COMMAND_TOOL_RCLICKED, 1)
EVT_TOOL_RCLICKED_RANGE = wx.PyEventBinder( wxEVT_COMMAND_TOOL_RCLICKED, 2)
EVT_TOOL_ENTER = wx.PyEventBinder( wxEVT_COMMAND_TOOL_ENTER, 1)
EVT_TOOL_DROPDOWN = wx.PyEventBinder( wxEVT_COMMAND_TOOL_DROPDOWN_CLICKED, 1)
EVT_CHECKLISTBOX = wx.PyEventBinder( wxEVT_COMMAND_CHECKLISTBOX_TOGGLED, 1)
EVT_COMBOBOX_DROPDOWN = wx.PyEventBinder( wxEVT_COMMAND_COMBOBOX_DROPDOWN , 1)
EVT_COMBOBOX_CLOSEUP  = wx.PyEventBinder( wxEVT_COMMAND_COMBOBOX_CLOSEUP , 1) 

EVT_COMMAND_LEFT_CLICK = wx.PyEventBinder( wxEVT_COMMAND_LEFT_CLICK, 1)
EVT_COMMAND_LEFT_DCLICK = wx.PyEventBinder( wxEVT_COMMAND_LEFT_DCLICK, 1)
EVT_COMMAND_RIGHT_CLICK = wx.PyEventBinder( wxEVT_COMMAND_RIGHT_CLICK, 1)
EVT_COMMAND_RIGHT_DCLICK = wx.PyEventBinder( wxEVT_COMMAND_RIGHT_DCLICK, 1)
EVT_COMMAND_SET_FOCUS = wx.PyEventBinder( wxEVT_COMMAND_SET_FOCUS, 1)
EVT_COMMAND_KILL_FOCUS = wx.PyEventBinder( wxEVT_COMMAND_KILL_FOCUS, 1)
EVT_COMMAND_ENTER = wx.PyEventBinder( wxEVT_COMMAND_ENTER, 1)

EVT_IDLE = wx.PyEventBinder( wxEVT_IDLE )

EVT_UPDATE_UI = wx.PyEventBinder( wxEVT_UPDATE_UI, 1)
EVT_UPDATE_UI_RANGE = wx.PyEventBinder( wxEVT_UPDATE_UI, 2)

EVT_CONTEXT_MENU = wx.PyEventBinder( wxEVT_CONTEXT_MENU )

EVT_TEXT_CUT   =  wx.PyEventBinder( wxEVT_COMMAND_TEXT_CUT )
EVT_TEXT_COPY  =  wx.PyEventBinder( wxEVT_COMMAND_TEXT_COPY )
EVT_TEXT_PASTE =  wx.PyEventBinder( wxEVT_COMMAND_TEXT_PASTE )

EVT_THREAD = wx.PyEventBinder( wxEVT_THREAD )

#---------------------------------------------------------------------------

class Event(Object):
    """
    An event is a structure holding information about an event passed to a
    callback or member function. wx.Event is an abstract base class for
    other event classes
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_Event
    __del__ = lambda self : None;
    def SetEventType(*args, **kwargs):
        """
        SetEventType(self, EventType typ)

        Sets the specific type of the event.
        """
        return __core.Event_SetEventType(*args, **kwargs)

    def GetEventType(*args, **kwargs):
        """
        GetEventType(self) -> EventType

        Returns the identifier of the given event type, such as
        ``wxEVT_COMMAND_BUTTON_CLICKED``.
        """
        return __core.Event_GetEventType(*args, **kwargs)

    def GetEventObject(*args, **kwargs):
        """
        GetEventObject(self) -> Object

        Returns the object (usually a window) associated with the event, if
        any.
        """
        return __core.Event_GetEventObject(*args, **kwargs)

    def SetEventObject(*args, **kwargs):
        """
        SetEventObject(self, Object obj)

        Sets the originating object, or in other words, obj is normally the
        object that is sending the event.
        """
        return __core.Event_SetEventObject(*args, **kwargs)

    def GetTimestamp(*args, **kwargs):
        """GetTimestamp(self) -> long"""
        return __core.Event_GetTimestamp(*args, **kwargs)

    def SetTimestamp(*args, **kwargs):
        """SetTimestamp(self, long ts=0)"""
        return __core.Event_SetTimestamp(*args, **kwargs)

    def GetId(*args, **kwargs):
        """
        GetId(self) -> int

        Returns the identifier associated with this event, such as a button
        command id.
        """
        return __core.Event_GetId(*args, **kwargs)

    def SetId(*args, **kwargs):
        """
        SetId(self, int Id)

        Set's the ID for the event.  This is usually the ID of the window that
        is sending the event, but it can also be a command id from a menu
        item, etc.
        """
        return __core.Event_SetId(*args, **kwargs)

    def GetEventCategory(*args, **kwargs):
        """GetEventCategory(self) -> int"""
        return __core.Event_GetEventCategory(*args, **kwargs)

    def IsCommandEvent(*args, **kwargs):
        """
        IsCommandEvent(self) -> bool

        Returns true if the event is or is derived from `wx.CommandEvent` else
        it returns false. Note: Exists only for optimization purposes.
        """
        return __core.Event_IsCommandEvent(*args, **kwargs)

    def Skip(*args, **kwargs):
        """
        Skip(self, bool skip=True)

        This method can be used inside an event handler to control whether
        further event handlers bound to this event will be called after the
        current one returns. Without Skip() (or equivalently if Skip(False) is
        used), the event will not be processed any more. If Skip(True) is
        called, the event processing system continues searching for a further
        handler function for this event, even though it has been processed
        already in the current handler.
        """
        return __core.Event_Skip(*args, **kwargs)

    def GetSkipped(*args, **kwargs):
        """
        GetSkipped(self) -> bool

        Returns true if the event handler should be skipped, false otherwise.
        :see: `Skip`
        """
        return __core.Event_GetSkipped(*args, **kwargs)

    def ShouldPropagate(*args, **kwargs):
        """
        ShouldPropagate(self) -> bool

        Test if this event should be propagated to the parent window or not,
        i.e. if the propagation level is currently greater than 0.
        """
        return __core.Event_ShouldPropagate(*args, **kwargs)

    def StopPropagation(*args, **kwargs):
        """
        StopPropagation(self) -> int

        Stop the event from propagating to its parent window.  Returns the old
        propagation level value which may be later passed to
        `ResumePropagation` to allow propagating the event again.
        """
        return __core.Event_StopPropagation(*args, **kwargs)

    def ResumePropagation(*args, **kwargs):
        """
        ResumePropagation(self, int propagationLevel)

        Resume the event propagation by restoring the propagation level.  (For
        example, you can use the value returned by an earlier call to
        `StopPropagation`.)

        """
        return __core.Event_ResumePropagation(*args, **kwargs)

    def WasProcessed(*args, **kwargs):
        """WasProcessed(self) -> bool"""
        return __core.Event_WasProcessed(*args, **kwargs)

    def ShouldProcessOnlyIn(*args, **kwargs):
        """ShouldProcessOnlyIn(self, EvtHandler h) -> bool"""
        return __core.Event_ShouldProcessOnlyIn(*args, **kwargs)

    def DidntHonourProcessOnlyIn(*args, **kwargs):
        """DidntHonourProcessOnlyIn(self)"""
        return __core.Event_DidntHonourProcessOnlyIn(*args, **kwargs)

    def Clone(*args, **kwargs):
        """Clone(self) -> Event"""
        return __core.Event_Clone(*args, **kwargs)

    EventObject = property(GetEventObject,SetEventObject,doc="See `GetEventObject` and `SetEventObject`") 
    EventType = property(GetEventType,SetEventType,doc="See `GetEventType` and `SetEventType`") 
    Id = property(GetId,SetId,doc="See `GetId` and `SetId`") 
    Skipped = property(GetSkipped,doc="See `GetSkipped`") 
    Timestamp = property(GetTimestamp,SetTimestamp,doc="See `GetTimestamp` and `SetTimestamp`") 
__core.Event_swigregister(Event)

#---------------------------------------------------------------------------

class PropagationDisabler(object):
    """
    Helper class to temporarily change an event not to propagate.  Simply
    create an instance of this class and then whe it is destroyed the
    propogation of the event will be restored.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Event event) -> PropagationDisabler

        Helper class to temporarily change an event not to propagate.  Simply
        create an instance of this class and then whe it is destroyed the
        propogation of the event will be restored.
        """
        this = __core.new_PropagationDisabler(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_PropagationDisabler
    __del__ = lambda self : None;
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

__core.PropagationDisabler_swigregister(PropagationDisabler)

class PropagateOnce(object):
    """
    A helper class that will temporarily lower propagation level of an
    event.  Simply create an instance of this class and then whe it is
    destroyed the propogation of the event will be restored.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Event event) -> PropagateOnce

        A helper class that will temporarily lower propagation level of an
        event.  Simply create an instance of this class and then whe it is
        destroyed the propogation of the event will be restored.
        """
        this = __core.new_PropagateOnce(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_PropagateOnce
    __del__ = lambda self : None;
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

__core.PropagateOnce_swigregister(PropagateOnce)

class EventProcessInHandlerOnly(object):
    """Proxy of C++ EventProcessInHandlerOnly class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, Event event, EvtHandler handler) -> EventProcessInHandlerOnly"""
        this = __core.new_EventProcessInHandlerOnly(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_EventProcessInHandlerOnly
    __del__ = lambda self : None;
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

__core.EventProcessInHandlerOnly_swigregister(EventProcessInHandlerOnly)

#---------------------------------------------------------------------------

class CommandEvent(Event):
    """
    This event class contains information about command events, which
    originate from a variety of simple controls, as well as menus and
    toolbars.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType commandType=wxEVT_NULL, int winid=0) -> CommandEvent

        This event class contains information about command events, which
        originate from a variety of simple controls, as well as menus and
        toolbars.
        """
        this = __core.new_CommandEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetSelection(*args, **kwargs):
        """
        GetSelection(self) -> int

        Returns item index for a listbox or choice selection event (not valid
        for a deselection).
        """
        return __core.CommandEvent_GetSelection(*args, **kwargs)

    def SetString(*args, **kwargs):
        """SetString(self, String s)"""
        return __core.CommandEvent_SetString(*args, **kwargs)

    def GetString(*args, **kwargs):
        """
        GetString(self) -> String

        Returns item string for a listbox or choice selection event (not valid
        for a deselection).
        """
        return __core.CommandEvent_GetString(*args, **kwargs)

    def IsChecked(*args, **kwargs):
        """
        IsChecked(self) -> bool

        This method can be used with checkbox and menu events: for the
        checkboxes, the method returns true for a selection event and false
        for a deselection one. For the menu events, this method indicates if
        the menu item just has become checked or unchecked (and thus only
        makes sense for checkable menu items).
        """
        return __core.CommandEvent_IsChecked(*args, **kwargs)

    Checked = IsChecked 
    def IsSelection(*args, **kwargs):
        """
        IsSelection(self) -> bool

        For a listbox or similar event, returns true if it is a selection,
        false if it is a deselection.
        """
        return __core.CommandEvent_IsSelection(*args, **kwargs)

    def SetExtraLong(*args, **kwargs):
        """SetExtraLong(self, long extraLong)"""
        return __core.CommandEvent_SetExtraLong(*args, **kwargs)

    def GetExtraLong(*args, **kwargs):
        """
        GetExtraLong(self) -> long

        Returns extra information dependant on the event objects type. If the
        event comes from a listbox selection, it is a boolean determining
        whether the event was a selection (true) or a deselection (false). A
        listbox deselection only occurs for multiple-selection boxes, and in
        this case the index and string values are indeterminate and the
        listbox must be examined by the application.
        """
        return __core.CommandEvent_GetExtraLong(*args, **kwargs)

    def SetInt(*args, **kwargs):
        """SetInt(self, int i)"""
        return __core.CommandEvent_SetInt(*args, **kwargs)

    def GetInt(*args, **kwargs):
        """
        GetInt(self) -> int

        Returns the integer identifier corresponding to a listbox, choice or
        radiobox selection (only if the event was a selection, not a
        deselection), or a boolean value representing the value of a checkbox.
        """
        return __core.CommandEvent_GetInt(*args, **kwargs)

    def GetClientData(*args, **kwargs):
        """
        GetClientData(self) -> PyObject

        Returns the client data object for a listbox or choice selection event, (if any.)
        """
        return __core.CommandEvent_GetClientData(*args, **kwargs)

    def SetClientData(*args, **kwargs):
        """
        SetClientData(self, PyObject clientData)

        Associate the given client data with the item at position n.
        """
        return __core.CommandEvent_SetClientData(*args, **kwargs)

    GetClientObject = GetClientData
    SetClientObject = SetClientData

    def Clone(*args, **kwargs):
        """Clone(self) -> Event"""
        return __core.CommandEvent_Clone(*args, **kwargs)

    ClientData = property(GetClientData,SetClientData,doc="See `GetClientData` and `SetClientData`") 
    ClientObject = property(GetClientObject,SetClientObject,doc="See `GetClientObject` and `SetClientObject`") 
    ExtraLong = property(GetExtraLong,SetExtraLong,doc="See `GetExtraLong` and `SetExtraLong`") 
    Int = property(GetInt,SetInt,doc="See `GetInt` and `SetInt`") 
    Selection = property(GetSelection,doc="See `GetSelection`") 
    String = property(GetString,SetString,doc="See `GetString` and `SetString`") 
__core.CommandEvent_swigregister(CommandEvent)

#---------------------------------------------------------------------------

class NotifyEvent(CommandEvent):
    """
    An instance of this class (or one of its derived classes) is sent from
    a control when the control's state is being changed and the control
    allows that change to be prevented from happening.  The event handler
    can call `Veto` or `Allow` to tell the control what to do.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType commandType=wxEVT_NULL, int winid=0) -> NotifyEvent

        An instance of this class (or one of its derived classes) is sent from
        a control when the control's state is being changed and the control
        allows that change to be prevented from happening.  The event handler
        can call `Veto` or `Allow` to tell the control what to do.
        """
        this = __core.new_NotifyEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def Veto(*args, **kwargs):
        """
        Veto(self)

        Prevents the change announced by this event from happening.

        It is in general a good idea to notify the user about the reasons for
        vetoing the change because otherwise the applications behaviour (which
        just refuses to do what the user wants) might be quite surprising.
        """
        return __core.NotifyEvent_Veto(*args, **kwargs)

    def Allow(*args, **kwargs):
        """
        Allow(self)

        This is the opposite of `Veto`: it explicitly allows the event to be
        processed. For most events it is not necessary to call this method as
        the events are allowed anyhow but some are forbidden by default (this
        will be mentioned in the corresponding event description).
        """
        return __core.NotifyEvent_Allow(*args, **kwargs)

    def IsAllowed(*args, **kwargs):
        """
        IsAllowed(self) -> bool

        Returns true if the change is allowed (`Veto` hasn't been called) or
        false otherwise (if it was).
        """
        return __core.NotifyEvent_IsAllowed(*args, **kwargs)

__core.NotifyEvent_swigregister(NotifyEvent)

#---------------------------------------------------------------------------

class ThreadEvent(Event):
    """Proxy of C++ ThreadEvent class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, EventType eventType=wxEVT_THREAD, int id=ID_ANY) -> ThreadEvent"""
        this = __core.new_ThreadEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetExtraLong(*args, **kwargs):
        """GetExtraLong(self) -> long"""
        return __core.ThreadEvent_GetExtraLong(*args, **kwargs)

    def GetInt(*args, **kwargs):
        """GetInt(self) -> int"""
        return __core.ThreadEvent_GetInt(*args, **kwargs)

    def GetString(*args, **kwargs):
        """GetString(self) -> String"""
        return __core.ThreadEvent_GetString(*args, **kwargs)

    def SetExtraLong(*args, **kwargs):
        """SetExtraLong(self, long extraLong)"""
        return __core.ThreadEvent_SetExtraLong(*args, **kwargs)

    def SetInt(*args, **kwargs):
        """SetInt(self, int intCommand)"""
        return __core.ThreadEvent_SetInt(*args, **kwargs)

    def SetString(*args, **kwargs):
        """SetString(self, String string)"""
        return __core.ThreadEvent_SetString(*args, **kwargs)

    ExtraLong = property(GetExtraLong,SetExtraLong,doc="See `GetExtraLong` and `SetExtraLong`") 
    Int = property(GetInt,SetInt,doc="See `GetInt` and `SetInt`") 
    String = property(GetString,SetString,doc="See `GetString` and `SetString`") 
__core.ThreadEvent_swigregister(ThreadEvent)

#---------------------------------------------------------------------------

class ScrollEvent(CommandEvent):
    """
    A scroll event holds information about events sent from stand-alone
    scrollbars and sliders. Note that scrolled windows do not send
    instances of this event class, but send the `wx.ScrollWinEvent`
    instead.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType commandType=wxEVT_NULL, int winid=0, int pos=0, 
            int orient=0) -> ScrollEvent
        """
        this = __core.new_ScrollEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetOrientation(*args, **kwargs):
        """
        GetOrientation(self) -> int

        Returns wx.HORIZONTAL or wx.VERTICAL, depending on the orientation of
        the scrollbar.
        """
        return __core.ScrollEvent_GetOrientation(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> int

        Returns the position of the scrollbar.
        """
        return __core.ScrollEvent_GetPosition(*args, **kwargs)

    def SetOrientation(*args, **kwargs):
        """SetOrientation(self, int orient)"""
        return __core.ScrollEvent_SetOrientation(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, int pos)"""
        return __core.ScrollEvent_SetPosition(*args, **kwargs)

    Orientation = property(GetOrientation,SetOrientation,doc="See `GetOrientation` and `SetOrientation`") 
    Position = property(GetPosition,SetPosition,doc="See `GetPosition` and `SetPosition`") 
__core.ScrollEvent_swigregister(ScrollEvent)

#---------------------------------------------------------------------------

class ScrollWinEvent(Event):
    """
    A wx.ScrollWinEvent holds information about scrolling and is sent from
    scrolling windows.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType commandType=wxEVT_NULL, int pos=0, int orient=0) -> ScrollWinEvent

        A wx.ScrollWinEvent holds information about scrolling and is sent from
        scrolling windows.
        """
        this = __core.new_ScrollWinEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetOrientation(*args, **kwargs):
        """
        GetOrientation(self) -> int

        Returns wx.HORIZONTAL or wx.VERTICAL, depending on the orientation of
        the scrollbar.
        """
        return __core.ScrollWinEvent_GetOrientation(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> int

        Returns the position of the scrollbar for the thumb track and release
        events. Note that this field can't be used for the other events, you
        need to query the window itself for the current position in that case.
        """
        return __core.ScrollWinEvent_GetPosition(*args, **kwargs)

    def SetOrientation(*args, **kwargs):
        """SetOrientation(self, int orient)"""
        return __core.ScrollWinEvent_SetOrientation(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, int pos)"""
        return __core.ScrollWinEvent_SetPosition(*args, **kwargs)

    Orientation = property(GetOrientation,SetOrientation,doc="See `GetOrientation` and `SetOrientation`") 
    Position = property(GetPosition,SetPosition,doc="See `GetPosition` and `SetPosition`") 
__core.ScrollWinEvent_swigregister(ScrollWinEvent)

#---------------------------------------------------------------------------

MOUSE_WHEEL_VERTICAL = __core.MOUSE_WHEEL_VERTICAL
MOUSE_WHEEL_HORIZONTAL = __core.MOUSE_WHEEL_HORIZONTAL
class MouseEvent(Event,MouseState):
    """
    This event class contains information about the events generated by
    the mouse: they include mouse buttons press and release events and
    mouse move events.

    All mouse events involving the buttons use ``wx.MOUSE_BTN_LEFT`` for
    the left mouse button, ``wx.MOUSE_BTN_MIDDLE`` for the middle one and
    ``wx.MOUSE_BTN_RIGHT`` for the right one. Note that not all mice have
    a middle button so a portable application should avoid relying on the
    events from it.

    Note the difference between methods like `LeftDown` and `LeftIsDown`:
    the former returns true when the event corresponds to the left mouse
    button click while the latter returns true if the left mouse button is
    currently being pressed. For example, when the user is dragging the
    mouse you can use `LeftIsDown` to test whether the left mouse button
    is (still) depressed. Also, by convention, if `LeftDown` returns true,
    `LeftIsDown` will also return true in wxWidgets whatever the
    underlying GUI behaviour is (which is platform-dependent). The same
    applies, of course, to other mouse buttons as well.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType mouseType=wxEVT_NULL) -> MouseEvent

        Constructs a wx.MouseEvent.  Valid event types are:

            * wxEVT_ENTER_WINDOW
            * wxEVT_LEAVE_WINDOW
            * wxEVT_LEFT_DOWN
            * wxEVT_LEFT_UP
            * wxEVT_LEFT_DCLICK
            * wxEVT_MIDDLE_DOWN
            * wxEVT_MIDDLE_UP
            * wxEVT_MIDDLE_DCLICK
            * wxEVT_RIGHT_DOWN
            * wxEVT_RIGHT_UP
            * wxEVT_RIGHT_DCLICK
            * wxEVT_MOTION
            * wxEVT_MOUSEWHEEL 
        """
        this = __core.new_MouseEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def IsButton(*args, **kwargs):
        """
        IsButton(self) -> bool

        Returns true if the event was a mouse button event (not necessarily a
        button down event - that may be tested using `ButtonDown`).
        """
        return __core.MouseEvent_IsButton(*args, **kwargs)

    def ButtonDown(*args, **kwargs):
        """
        ButtonDown(self, int but=MOUSE_BTN_ANY) -> bool

        If the argument is omitted, this returns true if the event was any
        mouse button down event. Otherwise the argument specifies which
        button-down event shold be checked for (see `Button` for the possible
        values).
        """
        return __core.MouseEvent_ButtonDown(*args, **kwargs)

    def ButtonDClick(*args, **kwargs):
        """
        ButtonDClick(self, int but=MOUSE_BTN_ANY) -> bool

        If the argument is omitted, this returns true if the event was any
        mouse double click event. Otherwise the argument specifies which
        double click event to check for (see `Button` for the possible
        values).
        """
        return __core.MouseEvent_ButtonDClick(*args, **kwargs)

    def ButtonUp(*args, **kwargs):
        """
        ButtonUp(self, int but=MOUSE_BTN_ANY) -> bool

        If the argument is omitted, this returns true if the event was any
        mouse button up event. Otherwise the argument specifies which button
        up event to check for (see `Button` for the possible values).
        """
        return __core.MouseEvent_ButtonUp(*args, **kwargs)

    def Button(*args, **kwargs):
        """
        Button(self, int button) -> bool

        Returns true if the identified mouse button is changing state. Valid
        values of button are:

             ====================      =====================================
             wx.MOUSE_BTN_LEFT         check if left button was pressed
             wx.MOUSE_BTN_MIDDLE       check if middle button was pressed
             wx.MOUSE_BTN_RIGHT        check if right button was pressed
             wx.MOUSE_BTN_ANY          check if any button was pressed
             ====================      =====================================

        """
        return __core.MouseEvent_Button(*args, **kwargs)

    def GetButton(*args, **kwargs):
        """
        GetButton(self) -> int

        Returns the mouse button which generated this event or
        wx.MOUSE_BTN_NONE if no button is involved (for mouse move, enter or
        leave event, for example). Otherwise wx.MOUSE_BTN_LEFT is returned for
        the left button down, up and double click events, wx.MOUSE_BTN_MIDDLE
        and wx.MOUSE_BTN_RIGHT for the same events for the middle and the
        right buttons respectively.
        """
        return __core.MouseEvent_GetButton(*args, **kwargs)

    def LeftDown(*args, **kwargs):
        """
        LeftDown(self) -> bool

        Returns true if the left mouse button state changed to down.
        """
        return __core.MouseEvent_LeftDown(*args, **kwargs)

    def MiddleDown(*args, **kwargs):
        """
        MiddleDown(self) -> bool

        Returns true if the middle mouse button state changed to down.
        """
        return __core.MouseEvent_MiddleDown(*args, **kwargs)

    def RightDown(*args, **kwargs):
        """
        RightDown(self) -> bool

        Returns true if the right mouse button state changed to down.
        """
        return __core.MouseEvent_RightDown(*args, **kwargs)

    def Aux1Down(*args, **kwargs):
        """
        Aux1Down(self) -> bool

        Returns true if the AUX1 mouse button state changed to down.
        """
        return __core.MouseEvent_Aux1Down(*args, **kwargs)

    def Aux2Down(*args, **kwargs):
        """
        Aux2Down(self) -> bool

        Returns true if the AUX2 mouse button state changed to down.
        """
        return __core.MouseEvent_Aux2Down(*args, **kwargs)

    def LeftUp(*args, **kwargs):
        """
        LeftUp(self) -> bool

        Returns true if the left mouse button state changed to up.
        """
        return __core.MouseEvent_LeftUp(*args, **kwargs)

    def MiddleUp(*args, **kwargs):
        """
        MiddleUp(self) -> bool

        Returns true if the middle mouse button state changed to up.
        """
        return __core.MouseEvent_MiddleUp(*args, **kwargs)

    def RightUp(*args, **kwargs):
        """
        RightUp(self) -> bool

        Returns true if the right mouse button state changed to up.
        """
        return __core.MouseEvent_RightUp(*args, **kwargs)

    def Aux1Up(*args, **kwargs):
        """
        Aux1Up(self) -> bool

        Returns true if the AUX1  mouse button state changed to up.
        """
        return __core.MouseEvent_Aux1Up(*args, **kwargs)

    def Aux2Up(*args, **kwargs):
        """
        Aux2Up(self) -> bool

        Returns true if the AUX2 mouse button state changed to up.
        """
        return __core.MouseEvent_Aux2Up(*args, **kwargs)

    def LeftDClick(*args, **kwargs):
        """
        LeftDClick(self) -> bool

        Returns true if the event was a left button double click.
        """
        return __core.MouseEvent_LeftDClick(*args, **kwargs)

    def MiddleDClick(*args, **kwargs):
        """
        MiddleDClick(self) -> bool

        Returns true if the event was a middle button double click.
        """
        return __core.MouseEvent_MiddleDClick(*args, **kwargs)

    def RightDClick(*args, **kwargs):
        """
        RightDClick(self) -> bool

        Returns true if the event was a right button double click.
        """
        return __core.MouseEvent_RightDClick(*args, **kwargs)

    def Aux1DClick(*args, **kwargs):
        """
        Aux1DClick(self) -> bool

        Returns true if the event was a AUX2 button double click.
        """
        return __core.MouseEvent_Aux1DClick(*args, **kwargs)

    def Aux2DClick(*args, **kwargs):
        """
        Aux2DClick(self) -> bool

        Returns true if the event was a AUX2 button double click.
        """
        return __core.MouseEvent_Aux2DClick(*args, **kwargs)

    def Dragging(*args, **kwargs):
        """
        Dragging(self) -> bool

        Returns true if this was a dragging event (motion while a button is
        depressed).
        """
        return __core.MouseEvent_Dragging(*args, **kwargs)

    def Moving(*args, **kwargs):
        """
        Moving(self) -> bool

        Returns true if this was a motion event and no mouse buttons were
        pressed. If any mouse button is held pressed, then this method returns
        false and Dragging returns true.
        """
        return __core.MouseEvent_Moving(*args, **kwargs)

    def Entering(*args, **kwargs):
        """
        Entering(self) -> bool

        Returns true if the mouse was entering the window.
        """
        return __core.MouseEvent_Entering(*args, **kwargs)

    def Leaving(*args, **kwargs):
        """
        Leaving(self) -> bool

        Returns true if the mouse was leaving the window.
        """
        return __core.MouseEvent_Leaving(*args, **kwargs)

    def GetClickCount(*args, **kwargs):
        """
        GetClickCount(self) -> int

        Returns the number of mouse clicks associated with this event.
        """
        return __core.MouseEvent_GetClickCount(*args, **kwargs)

    def GetLogicalPosition(*args, **kwargs):
        """
        GetLogicalPosition(self, DC dc) -> Point

        Returns the logical mouse position in pixels (i.e. translated
        according to the translation set for the DC, which usually indicates
        that the window has been scrolled).
        """
        return __core.MouseEvent_GetLogicalPosition(*args, **kwargs)

    def GetWheelRotation(*args, **kwargs):
        """
        GetWheelRotation(self) -> int

        Get wheel rotation, positive or negative indicates direction of
        rotation. Current devices all send an event when rotation is equal to
        +/-WheelDelta, but this allows for finer resolution devices to be
        created in the future. Because of this you shouldn't assume that one
        event is equal to 1 line or whatever, but you should be able to either
        do partial line scrolling or wait until +/-WheelDelta rotation values
        have been accumulated before scrolling.
        """
        return __core.MouseEvent_GetWheelRotation(*args, **kwargs)

    def GetWheelDelta(*args, **kwargs):
        """
        GetWheelDelta(self) -> int

        Get wheel delta, normally 120. This is the threshold for action to be
        taken, and one such action (for example, scrolling one increment)
        should occur for each delta.
        """
        return __core.MouseEvent_GetWheelDelta(*args, **kwargs)

    def GetWheelAxis(*args, **kwargs):
        """
        GetWheelAxis(self) -> int

        Gets the axis the wheel operation concerns, 0 being the y axis as on
        most mouse wheels, 1 is the x axis for things like MightyMouse scrolls
        or horizontal trackpad scrolling.
        """
        return __core.MouseEvent_GetWheelAxis(*args, **kwargs)

    def GetLinesPerAction(*args, **kwargs):
        """
        GetLinesPerAction(self) -> int

        Returns the configured number of lines (or whatever) to be scrolled
        per wheel action. Defaults to three.
        """
        return __core.MouseEvent_GetLinesPerAction(*args, **kwargs)

    def IsPageScroll(*args, **kwargs):
        """
        IsPageScroll(self) -> bool

        Returns true if the system has been setup to do page scrolling with
        the mouse wheel instead of line scrolling.
        """
        return __core.MouseEvent_IsPageScroll(*args, **kwargs)

    LinesPerAction = property(GetLinesPerAction,doc="See `GetLinesPerAction`") 
    LogicalPosition = property(GetLogicalPosition,doc="See `GetLogicalPosition`") 
    WheelDelta = property(GetWheelDelta,doc="See `GetWheelDelta`") 
    WheelRotation = property(GetWheelRotation,doc="See `GetWheelRotation`") 
__core.MouseEvent_swigregister(MouseEvent)

#---------------------------------------------------------------------------

class SetCursorEvent(Event):
    """
    A SetCursorEvent is generated when the mouse cursor is about to be set
    as a result of mouse motion. This event gives the application the
    chance to perform specific mouse cursor processing based on the
    current position of the mouse within the window. Use the `SetCursor`
    method to specify the cursor you want to be displayed.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int x=0, int y=0) -> SetCursorEvent

        Construct a new `wx.SetCursorEvent`.
        """
        this = __core.new_SetCursorEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetX(*args, **kwargs):
        """
        GetX(self) -> int

        Returns the X coordinate of the mouse in client coordinates.
        """
        return __core.SetCursorEvent_GetX(*args, **kwargs)

    def GetY(*args, **kwargs):
        """
        GetY(self) -> int

        Returns the Y coordinate of the mouse in client coordinates.
        """
        return __core.SetCursorEvent_GetY(*args, **kwargs)

    def SetCursor(*args, **kwargs):
        """
        SetCursor(self, Cursor cursor)

        Sets the cursor associated with this event.
        """
        return __core.SetCursorEvent_SetCursor(*args, **kwargs)

    def GetCursor(*args, **kwargs):
        """
        GetCursor(self) -> Cursor

        Returns a reference to the cursor specified by this event.
        """
        return __core.SetCursorEvent_GetCursor(*args, **kwargs)

    def HasCursor(*args, **kwargs):
        """
        HasCursor(self) -> bool

        Returns true if the cursor specified by this event is a valid cursor.
        """
        return __core.SetCursorEvent_HasCursor(*args, **kwargs)

    Cursor = property(GetCursor,SetCursor,doc="See `GetCursor` and `SetCursor`") 
    X = property(GetX,doc="See `GetX`") 
    Y = property(GetY,doc="See `GetY`") 
__core.SetCursorEvent_swigregister(SetCursorEvent)

#---------------------------------------------------------------------------

WXK_CATEGORY_ARROW = __core.WXK_CATEGORY_ARROW
WXK_CATEGORY_PAGING = __core.WXK_CATEGORY_PAGING
WXK_CATEGORY_JUMP = __core.WXK_CATEGORY_JUMP
WXK_CATEGORY_TAB = __core.WXK_CATEGORY_TAB
WXK_CATEGORY_CUT = __core.WXK_CATEGORY_CUT
WXK_CATEGORY_NAVIGATION = __core.WXK_CATEGORY_NAVIGATION
class KeyEvent(Event,KeyboardState):
    """
    This event class contains information about keypress and character
    events.  These events are only sent to the widget that currently has
    the keyboard focus.

    Notice that there are three different kinds of keyboard events in
    wxWidgets: key down and up events and char events. The difference
    between the first two is clear - the first corresponds to a key press
    and the second to a key release - otherwise they are identical. Just
    note that if the key is maintained in a pressed state you will
    typically get a lot of (automatically generated) down events but only
    one up so it is wrong to assume that there is one up event
    corresponding to each down one.

    Both key events provide untranslated key codes while the char event
    carries the translated one. The untranslated code for alphanumeric
    keys is always an upper case value. For the other keys it is one of
    WXK_XXX values from the keycodes table. The translated key is, in
    general, the character the user expects to appear as the result of the
    key combination when typing the text into a text entry zone, for
    example.

    A few examples to clarify this (all assume that CAPS LOCK is unpressed
    and the standard US keyboard): when the 'A' key is pressed, the key
    down event key code is equal to ASCII A == 65. But the char event key
    code is ASCII a == 97. On the other hand, if you press both SHIFT and
    'A' keys simultaneously , the key code in key down event will still be
    just 'A' while the char event key code parameter will now be 'A' as
    well.

    Although in this simple case it is clear that the correct key code
    could be found in the key down event handler by checking the value
    returned by `ShiftDown`, in general you should use EVT_CHAR for this
    as for non alphanumeric keys or non-US keyboard layouts the
    translation is keyboard-layout dependent and can only be done properly
    by the system itself.

    Another kind of translation is done when the control key is pressed:
    for example, for CTRL-A key press the key down event still carries the
    same key code 'A' as usual but the char event will have key code of 1,
    the ASCII value of this key combination.

    You may discover how the other keys on your system behave
    interactively by running the KeyEvents sample in the wxPython demo and
    pressing some keys while the blue box at the top has the keyboard
    focus.

    **Note**: If a key down event is caught and the event handler does not
    call event.Skip() then the coresponding char event will not
    happen. This is by design and enables the programs that handle both
    types of events to be a bit simpler.

    **Note for Windows programmers**: The key and char events in wxWidgets
    are similar to but slightly different from Windows WM_KEYDOWN and
    WM_CHAR events. In particular, Alt-x combination will generate a char
    event in wxWidgets (unless it is used as an accelerator).

    **Tip**: be sure to call event.Skip() for events that you don't
    process in key event function, otherwise menu shortcuts may cease to
    work under Windows.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType eventType=wxEVT_NULL) -> KeyEvent

        Construct a new `wx.KeyEvent`.  Valid event types are:
            * 
        """
        this = __core.new_KeyEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetKeyCode(*args, **kwargs):
        """
        GetKeyCode(self) -> int

        Returns the virtual key code. ASCII events return normal ASCII values,
        while non-ASCII events return values such as WXK_LEFT for the left
        cursor key. See `wx.KeyEvent` for a full list of the virtual key
        codes.

        Note that in Unicode build, the returned value is meaningful only if
        the user entered a character that can be represented in current
        locale's default charset. You can obtain the corresponding Unicode
        character using `GetUnicodeKey`.
        """
        return __core.KeyEvent_GetKeyCode(*args, **kwargs)

    def IsKeyInCategory(*args, **kwargs):
        """IsKeyInCategory(self, int category) -> bool"""
        return __core.KeyEvent_IsKeyInCategory(*args, **kwargs)

    def GetUnicodeKey(*args, **kwargs):
        """
        GetUnicodeKey(self) -> int

        Returns the Unicode character corresponding to this key event.  This
        function is only meaningful in a Unicode build of wxPython.
        """
        return __core.KeyEvent_GetUnicodeKey(*args, **kwargs)

    GetUniChar = GetUnicodeKey 
    def SetUnicodeKey(*args, **kwargs):
        """
        SetUnicodeKey(self, int uniChar)

        Set the Unicode value of the key event, but only if this is a Unicode
        build of wxPython.
        """
        return __core.KeyEvent_SetUnicodeKey(*args, **kwargs)

    def GetRawKeyCode(*args, **kwargs):
        """
        GetRawKeyCode(self) -> unsigned int

        Returns the raw key code for this event. This is a platform-dependent
        scan code which should only be used in advanced
        applications. Currently the raw key codes are not supported by all
        ports.
        """
        return __core.KeyEvent_GetRawKeyCode(*args, **kwargs)

    def GetRawKeyFlags(*args, **kwargs):
        """
        GetRawKeyFlags(self) -> unsigned int

        Returns the low level key flags for this event. The flags are
        platform-dependent and should only be used in advanced applications.
        Currently the raw key flags are not supported by all ports.
        """
        return __core.KeyEvent_GetRawKeyFlags(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> Point

        Find the position of the event, if applicable.
        """
        return __core.KeyEvent_GetPosition(*args, **kwargs)

    def GetPositionTuple(*args, **kwargs):
        """
        GetPositionTuple() -> (x,y)

        Find the position of the event, if applicable.
        """
        return __core.KeyEvent_GetPositionTuple(*args, **kwargs)

    def GetX(*args, **kwargs):
        """
        GetX(self) -> int

        Returns the X position (in client coordinates) of the event, if
        applicable.
        """
        return __core.KeyEvent_GetX(*args, **kwargs)

    def GetY(*args, **kwargs):
        """
        GetY(self) -> int

        Returns the Y position (in client coordinates) of the event, if
        applicable.
        """
        return __core.KeyEvent_GetY(*args, **kwargs)

    def DoAllowNextEvent(*args, **kwargs):
        """DoAllowNextEvent(self)"""
        return __core.KeyEvent_DoAllowNextEvent(*args, **kwargs)

    def IsNextEventAllowed(*args, **kwargs):
        """IsNextEventAllowed(self) -> bool"""
        return __core.KeyEvent_IsNextEventAllowed(*args, **kwargs)

    m_x = property(__core.KeyEvent_m_x_get, __core.KeyEvent_m_x_set)
    m_y = property(__core.KeyEvent_m_y_get, __core.KeyEvent_m_y_set)
    m_keyCode = property(__core.KeyEvent_m_keyCode_get, __core.KeyEvent_m_keyCode_set)
    m_rawCode = property(__core.KeyEvent_m_rawCode_get, __core.KeyEvent_m_rawCode_set)
    m_rawFlags = property(__core.KeyEvent_m_rawFlags_get, __core.KeyEvent_m_rawFlags_set)
    KeyCode = property(GetKeyCode,doc="See `GetKeyCode`") 
    Position = property(GetPosition,doc="See `GetPosition`") 
    RawKeyCode = property(GetRawKeyCode,doc="See `GetRawKeyCode`") 
    RawKeyFlags = property(GetRawKeyFlags,doc="See `GetRawKeyFlags`") 
    UnicodeKey = property(GetUnicodeKey,SetUnicodeKey,doc="See `GetUnicodeKey` and `SetUnicodeKey`") 
    X = property(GetX,doc="See `GetX`") 
    Y = property(GetY,doc="See `GetY`") 
__core.KeyEvent_swigregister(KeyEvent)

#---------------------------------------------------------------------------

class SizeEvent(Event):
    """
    A size event holds information about size change events.  The EVT_SIZE
    handler function will be called when the window it is bound to has
    been resized.

    Note that the size passed is of the whole window: call
    `wx.Window.GetClientSize` for the area which may be used by the
    application.

    When a window is resized, usually only a small part of the window is
    damaged and and that area is all that is in the update region for the
    next paint event. However, if your drawing depends on the size of the
    window, you may need to clear the DC explicitly and repaint the whole
    window. In which case, you may need to call `wx.Window.Refresh` to
    invalidate the entire window.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Size sz=DefaultSize, int winid=0) -> SizeEvent

        Construct a new ``wx.SizeEvent``.
        """
        this = __core.new_SizeEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetSize(*args, **kwargs):
        """
        GetSize(self) -> Size

        Returns the entire size of the window generating the size change
        event.
        """
        return __core.SizeEvent_GetSize(*args, **kwargs)

    def GetRect(*args, **kwargs):
        """GetRect(self) -> Rect"""
        return __core.SizeEvent_GetRect(*args, **kwargs)

    def SetRect(*args, **kwargs):
        """SetRect(self, Rect rect)"""
        return __core.SizeEvent_SetRect(*args, **kwargs)

    def SetSize(*args, **kwargs):
        """SetSize(self, Size size)"""
        return __core.SizeEvent_SetSize(*args, **kwargs)

    m_size = property(__core.SizeEvent_m_size_get, __core.SizeEvent_m_size_set)
    m_rect = property(__core.SizeEvent_m_rect_get, __core.SizeEvent_m_rect_set)
    Rect = property(GetRect,SetRect,doc="See `GetRect` and `SetRect`") 
    Size = property(GetSize,SetSize,doc="See `GetSize` and `SetSize`") 
__core.SizeEvent_swigregister(SizeEvent)

#---------------------------------------------------------------------------

class MoveEvent(Event):
    """
    This event object is sent for EVT_MOVE event bindings when a window is
    moved to a new position.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Point pos=DefaultPosition, int winid=0) -> MoveEvent

        Constructor.
        """
        this = __core.new_MoveEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> Point

        Returns the position of the window generating the move change event.
        """
        return __core.MoveEvent_GetPosition(*args, **kwargs)

    def GetRect(*args, **kwargs):
        """GetRect(self) -> Rect"""
        return __core.MoveEvent_GetRect(*args, **kwargs)

    def SetRect(*args, **kwargs):
        """SetRect(self, Rect rect)"""
        return __core.MoveEvent_SetRect(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """SetPosition(self, Point pos)"""
        return __core.MoveEvent_SetPosition(*args, **kwargs)

    m_pos =  property(GetPosition, SetPosition)
    m_rect = property(GetRect, SetRect)

    Position = property(GetPosition,SetPosition,doc="See `GetPosition` and `SetPosition`") 
    Rect = property(GetRect,SetRect,doc="See `GetRect` and `SetRect`") 
__core.MoveEvent_swigregister(MoveEvent)

#---------------------------------------------------------------------------

class PaintEvent(Event):
    """
    A paint event is sent when a window's contents needs to be repainted.
    Note that in an EVT_PAINT handler the application must *always* create
    a `wx.PaintDC` object, even if you do not use it.  Otherwise MS
    Windows assumes that the window has not been painted yet and will send
    the event again, causing endless refreshes.

    You can optimize painting by retrieving the rectangles that have been
    damaged using `wx.Window.GetUpdateRegion` and/or `wx.RegionIterator`,
    and only repainting these rectangles. The rectangles are in terms of
    the client area, and are unscrolled, so you will need to do some
    calculations using the current view position to obtain logical,
    scrolled units.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, int Id=0) -> PaintEvent"""
        this = __core.new_PaintEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.PaintEvent_swigregister(PaintEvent)

class NcPaintEvent(Event):
    """Proxy of C++ NcPaintEvent class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, int winid=0) -> NcPaintEvent"""
        this = __core.new_NcPaintEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.NcPaintEvent_swigregister(NcPaintEvent)

#---------------------------------------------------------------------------

class EraseEvent(Event):
    """
    An erase event is sent whenever the background of a window needs to be
    repainted.  To intercept this event use the EVT_ERASE_BACKGROUND event
    binder.  On some platforms, such as GTK+, this event is simulated
    (simply generated just before the paint event) and may cause flicker.

    To paint a custom background use the `GetDC` method and use the returned
    device context if it is not ``None``, otherwise create a temporary
    `wx.ClientDC` and draw on that.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int Id=0, DC dc=None) -> EraseEvent

        Constructor
        """
        this = __core.new_EraseEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetDC(*args, **kwargs):
        """
        GetDC(self) -> DC

        Returns the device context the event handler should draw upon.  If
        ``None`` is returned then create a temporary `wx.ClientDC` and use
        that instead.
        """
        return __core.EraseEvent_GetDC(*args, **kwargs)

    DC = property(GetDC,doc="See `GetDC`") 
__core.EraseEvent_swigregister(EraseEvent)

#---------------------------------------------------------------------------

class FocusEvent(Event):
    """
    A focus event is sent when a window's focus changes. The window losing
    focus receives an EVT_KILL_FOCUS event while the window gaining it
    gets an EVT_SET_FOCUS event.

    Notice that the set focus event happens both when the user gives focus
    to the window (whether using the mouse or keyboard) and when it is
    done from the program itself using `wx.Window.SetFocus`.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType type=wxEVT_NULL, int winid=0) -> FocusEvent

        Constructor
        """
        this = __core.new_FocusEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetWindow(*args, **kwargs):
        """
        GetWindow(self) -> Window

        Returns the other window associated with this event, that is the
        window which had the focus before for the EVT_SET_FOCUS event and the
        window which is going to receive focus for the wxEVT_KILL_FOCUS event.

        Warning: the window returned may be None!
        """
        return __core.FocusEvent_GetWindow(*args, **kwargs)

    def SetWindow(*args, **kwargs):
        """SetWindow(self, Window win)"""
        return __core.FocusEvent_SetWindow(*args, **kwargs)

    Window = property(GetWindow,SetWindow,doc="See `GetWindow` and `SetWindow`") 
__core.FocusEvent_swigregister(FocusEvent)

#---------------------------------------------------------------------------

class ChildFocusEvent(CommandEvent):
    """
    A child focus event is sent to a (parent-)window when one of its child
    windows gains focus, so that the window could restore the focus back
    to its corresponding child if it loses it now and regains later.

    Notice that child window is the direct child of the window receiving
    the event, and so may not be the actual widget recieving focus if it
    is further down the containment heirarchy.  Use `wx.Window.FindFocus`
    to get the widget that is actually receiving focus.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window win=None) -> ChildFocusEvent

        Constructor
        """
        this = __core.new_ChildFocusEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetWindow(*args, **kwargs):
        """
        GetWindow(self) -> Window

        The window, or (grand)parent of the window which has just received the
        focus.
        """
        return __core.ChildFocusEvent_GetWindow(*args, **kwargs)

    Window = property(GetWindow,doc="See `GetWindow`") 
__core.ChildFocusEvent_swigregister(ChildFocusEvent)

#---------------------------------------------------------------------------

class ActivateEvent(Event):
    """
    An activate event is sent when a top-level window or the entire
    application is being activated or deactivated.

    A top-level window (a dialog or frame) receives an activate event when
    is being activated or deactivated. This is indicated visually by the
    title bar changing colour, and a subwindow gaining the keyboard focus.
    An application is activated or deactivated when one of its frames
    becomes activated, or a frame becomes inactivate resulting in all
    application frames being inactive.

    Please note that usually you should call event.Skip() in your handlers
    for these events so the default handlers will still be called, as not
    doing so can result in strange effects.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType type=wxEVT_NULL, bool active=True, int Id=0) -> ActivateEvent

        Constructor
        """
        this = __core.new_ActivateEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetActive(*args, **kwargs):
        """
        GetActive(self) -> bool

        Returns true if the application or window is being activated, false
        otherwise.
        """
        return __core.ActivateEvent_GetActive(*args, **kwargs)

    Active = property(GetActive,doc="See `GetActive`") 
__core.ActivateEvent_swigregister(ActivateEvent)

#---------------------------------------------------------------------------

class InitDialogEvent(Event):
    """
    A wx.InitDialogEvent is sent as a dialog is being initialised, or for
    any window when `wx.Window.InitDialog` is called.  Handlers for this
    event can transfer data to the window, or anything else that should be
    done before the user begins editing the form. The default handler
    calls `wx.Window.TransferDataToWindow`.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int Id=0) -> InitDialogEvent

        Constructor
        """
        this = __core.new_InitDialogEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.InitDialogEvent_swigregister(InitDialogEvent)

#---------------------------------------------------------------------------

class MenuEvent(Event):
    """
    This class is used for a variety of menu-related events.  Note that
    these do not include menu command events, which are handled by sending
    `wx.CommandEvent` objects.

    The default handler for wx.EVT_MENU_HIGHLIGHT displays menu item help
    text in the first field of the status bar.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType type=wxEVT_NULL, int winid=0, Menu menu=None) -> MenuEvent

        Constructor
        """
        this = __core.new_MenuEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetMenuId(*args, **kwargs):
        """
        GetMenuId(self) -> int

        Returns the menu identifier associated with the event. This method
        should be only used with the HIGHLIGHT events.
        """
        return __core.MenuEvent_GetMenuId(*args, **kwargs)

    def IsPopup(*args, **kwargs):
        """
        IsPopup(self) -> bool

        Returns ``True`` if the menu which is being opened or closed is a
        popup menu, ``False`` if it is a normal one.  This method should only
        be used with the OPEN and CLOSE events.
        """
        return __core.MenuEvent_IsPopup(*args, **kwargs)

    def GetMenu(*args, **kwargs):
        """
        GetMenu(self) -> Menu

        Returns the menu which is being opened or closed. This method should
        only be used with the OPEN and CLOSE events.
        """
        return __core.MenuEvent_GetMenu(*args, **kwargs)

    Menu = property(GetMenu,doc="See `GetMenu`") 
    MenuId = property(GetMenuId,doc="See `GetMenuId`") 
__core.MenuEvent_swigregister(MenuEvent)

#---------------------------------------------------------------------------

class CloseEvent(Event):
    """
    This event class contains information about window and session close
    events.

    The handler function for EVT_CLOSE is called when the user has tried
    to close a a frame or dialog box using the window manager controls or
    the system menu. It can also be invoked by the application itself
    programmatically, for example by calling the `wx.Window.Close`
    function.

    You should check whether the application is forcing the deletion of
    the window using `CanVeto`. If it returns ``False``, you must destroy
    the window using `wx.Window.Destroy`. If the return value is ``True``,
    it is up to you whether you respond by destroying the window or not.
    For example you may wish to display a message dialog prompting to save
    files or to cancel the close.

    If you don't destroy the window, you should call `Veto` to let the
    calling code know that you did not destroy the window. This allows the
    `wx.Window.Close` function to return ``True`` or ``False`` depending
    on whether the close instruction was honored or not.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType type=wxEVT_NULL, int winid=0) -> CloseEvent

        Constructor.
        """
        this = __core.new_CloseEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def SetLoggingOff(*args, **kwargs):
        """
        SetLoggingOff(self, bool logOff)

        Sets the 'logging off' flag.
        """
        return __core.CloseEvent_SetLoggingOff(*args, **kwargs)

    def GetLoggingOff(*args, **kwargs):
        """
        GetLoggingOff(self) -> bool

        Returns ``True`` if the user is logging off or ``False`` if the
        system is shutting down. This method can only be called for end
        session and query end session events, it doesn't make sense for close
        window event.
        """
        return __core.CloseEvent_GetLoggingOff(*args, **kwargs)

    def Veto(*args, **kwargs):
        """
        Veto(self, bool veto=True)

        Call this from your event handler to veto a system shutdown or to
        signal to the calling application that a window close did not happen.

        You can only veto a shutdown or close if `CanVeto` returns true.
        """
        return __core.CloseEvent_Veto(*args, **kwargs)

    def GetVeto(*args, **kwargs):
        """GetVeto(self) -> bool"""
        return __core.CloseEvent_GetVeto(*args, **kwargs)

    def SetCanVeto(*args, **kwargs):
        """
        SetCanVeto(self, bool canVeto)

        Sets the 'can veto' flag.
        """
        return __core.CloseEvent_SetCanVeto(*args, **kwargs)

    def CanVeto(*args, **kwargs):
        """
        CanVeto(self) -> bool

        Returns true if you can veto a system shutdown or a window close
        event. Vetoing a window close event is not possible if the calling
        code wishes to force the application to exit, and so this function
        must be called to check this.
        """
        return __core.CloseEvent_CanVeto(*args, **kwargs)

    LoggingOff = property(GetLoggingOff,SetLoggingOff,doc="See `GetLoggingOff` and `SetLoggingOff`") 
__core.CloseEvent_swigregister(CloseEvent)

#---------------------------------------------------------------------------

class ShowEvent(Event):
    """An EVT_SHOW event is sent when a window is shown or hidden."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int winid=0, bool show=False) -> ShowEvent

        An EVT_SHOW event is sent when a window is shown or hidden.
        """
        this = __core.new_ShowEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def SetShow(*args, **kwargs):
        """SetShow(self, bool show)"""
        return __core.ShowEvent_SetShow(*args, **kwargs)

    def IsShown(*args, **kwargs):
        """IsShown(self) -> bool"""
        return __core.ShowEvent_IsShown(*args, **kwargs)

    GetShow = IsShown 
    Show = property(IsShown,SetShow,doc="See `GetShow` and `SetShow`") 
__core.ShowEvent_swigregister(ShowEvent)

#---------------------------------------------------------------------------

class IconizeEvent(Event):
    """
    An EVT_ICONIZE event is sent when a frame is iconized (minimized) or
    restored.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int id=0, bool iconized=True) -> IconizeEvent

        An EVT_ICONIZE event is sent when a frame is iconized (minimized) or
        restored.
        """
        this = __core.new_IconizeEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def IsIconized(*args, **kwargs):
        """
        IsIconized(self) -> bool

        Returns ``True`` if the frame has been iconized, ``False`` if it has
        been restored.
        """
        return __core.IconizeEvent_IsIconized(*args, **kwargs)

    Iconized = IsIconized 
__core.IconizeEvent_swigregister(IconizeEvent)

#---------------------------------------------------------------------------

class MaximizeEvent(Event):
    """An EVT_MAXIMIZE event is sent when a frame is maximized or restored."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int id=0) -> MaximizeEvent

        An EVT_MAXIMIZE event is sent when a frame is maximized or restored.
        """
        this = __core.new_MaximizeEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.MaximizeEvent_swigregister(MaximizeEvent)

#---------------------------------------------------------------------------

class DropFilesEvent(Event):
    """
    This class is used for drop files events, that is, when files have
    been dropped onto the window. This functionality is only available
    under Windows. The window must have previously been enabled for
    dropping by calling `wx.Window.DragAcceptFiles`.

    Important note: this is a separate implementation to the more general
    drag and drop implementation using `wx.FileDropTarget`, and etc. This
    implementation uses the older, Windows message-based approach of
    dropping files.

    Use wx.EVT_DROP_FILES to bind an event handler to receive file drop
    events.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> Point

        Returns the position at which the files were dropped.
        """
        return __core.DropFilesEvent_GetPosition(*args, **kwargs)

    def GetNumberOfFiles(*args, **kwargs):
        """
        GetNumberOfFiles(self) -> int

        Returns the number of files dropped.
        """
        return __core.DropFilesEvent_GetNumberOfFiles(*args, **kwargs)

    def GetFiles(*args, **kwargs):
        """
        GetFiles(self) -> PyObject

        Returns a list of the filenames that were dropped.
        """
        return __core.DropFilesEvent_GetFiles(*args, **kwargs)

    Files = property(GetFiles,doc="See `GetFiles`") 
    NumberOfFiles = property(GetNumberOfFiles,doc="See `GetNumberOfFiles`") 
    Position = property(GetPosition,doc="See `GetPosition`") 
__core.DropFilesEvent_swigregister(DropFilesEvent)

#---------------------------------------------------------------------------

UPDATE_UI_PROCESS_ALL = __core.UPDATE_UI_PROCESS_ALL
UPDATE_UI_PROCESS_SPECIFIED = __core.UPDATE_UI_PROCESS_SPECIFIED
class UpdateUIEvent(CommandEvent):
    """
    This class is used for EVT_UPDATE_UI pseudo-events which are sent by
    wxWidgets to give an application the chance to update various user
    interface elements.

    Without update UI events, an application has to work hard to
    check/uncheck, enable/disable, and set the text for elements such as
    menu items and toolbar buttons. The code for doing this has to be
    mixed up with the code that is invoked when an action is invoked for a
    menu item or button.

    With update UI events, you define an event handler to look at the
    state of the application and change UI elements accordingly. wxWidgets
    will call your handler functions in idle time, so you don't have to
    worry where to call this code. In addition to being a clearer and more
    declarative method, it also means you don't have to worry whether
    you're updating a toolbar or menubar identifier. The same handler can
    update a menu item and toolbar button, if the ID values are the same.

    Instead of directly manipulating the menu or button, you call
    functions in the event object, such as `Check`. wxWidgets will
    determine whether such a call has been made, and which UI element to
    update.

    These events will work for popup menus as well as menubars. Just
    before a menu is popped up, `wx.Menu.UpdateUI` is called to process
    any UI events for the window that owns the menu.

    If you find that the overhead of UI update processing is affecting
    your application, you can do one or both of the following:

       1. Call `wx.UpdateUIEvent.SetMode` with a value of
          wx.UPDATE_UI_PROCESS_SPECIFIED, and set the extra style
          wx.WS_EX_PROCESS_UPDATE_EVENTS for every window that should
          receive update events. No other windows will receive update
          events.

       2. Call `wx.UpdateUIEvent.SetUpdateInterval` with a millisecond
          value to set the delay between updates. You may need to call
          `wx.Window.UpdateWindowUI` at critical points, for example when
          a dialog is about to be shown, in case the user sees a slight
          delay before windows are updated.

    Note that although events are sent in idle time, defining a EVT_IDLE
    handler for a window does not affect this because the events are sent
    from an internal idle handler.

    wxWidgets tries to optimize update events on some platforms. On
    Windows and GTK+, events for menubar items are only sent when the menu
    is about to be shown, and not in idle time.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int commandId=0) -> UpdateUIEvent

        Constructor
        """
        this = __core.new_UpdateUIEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetChecked(*args, **kwargs):
        """
        GetChecked(self) -> bool

        Returns ``True`` if the UI element should be checked.
        """
        return __core.UpdateUIEvent_GetChecked(*args, **kwargs)

    def GetEnabled(*args, **kwargs):
        """
        GetEnabled(self) -> bool

        Returns ``True`` if the UI element should be enabled.
        """
        return __core.UpdateUIEvent_GetEnabled(*args, **kwargs)

    def GetShown(*args, **kwargs):
        """
        GetShown(self) -> bool

        Returns ``True`` if the UI element should be shown.
        """
        return __core.UpdateUIEvent_GetShown(*args, **kwargs)

    def GetText(*args, **kwargs):
        """
        GetText(self) -> String

        Returns the text that should be set for the UI element.
        """
        return __core.UpdateUIEvent_GetText(*args, **kwargs)

    def GetSetText(*args, **kwargs):
        """
        GetSetText(self) -> bool

        Returns ``True`` if the application has called `SetText`. For
        wxWidgets internal use only.
        """
        return __core.UpdateUIEvent_GetSetText(*args, **kwargs)

    def GetSetChecked(*args, **kwargs):
        """
        GetSetChecked(self) -> bool

        Returns ``True`` if the application has called `Check`. For wxWidgets
        internal use only.
        """
        return __core.UpdateUIEvent_GetSetChecked(*args, **kwargs)

    def GetSetEnabled(*args, **kwargs):
        """
        GetSetEnabled(self) -> bool

        Returns ``True`` if the application has called `Enable`. For wxWidgets
        internal use only.
        """
        return __core.UpdateUIEvent_GetSetEnabled(*args, **kwargs)

    def GetSetShown(*args, **kwargs):
        """
        GetSetShown(self) -> bool

        Returns ``True`` if the application has called `Show`. For wxWidgets
        internal use only.
        """
        return __core.UpdateUIEvent_GetSetShown(*args, **kwargs)

    def Check(*args, **kwargs):
        """
        Check(self, bool check)

        Check or uncheck the UI element.
        """
        return __core.UpdateUIEvent_Check(*args, **kwargs)

    def Enable(*args, **kwargs):
        """
        Enable(self, bool enable)

        Enable or disable the UI element.
        """
        return __core.UpdateUIEvent_Enable(*args, **kwargs)

    def Show(*args, **kwargs):
        """
        Show(self, bool show)

        Show or hide the UI element.
        """
        return __core.UpdateUIEvent_Show(*args, **kwargs)

    def SetText(*args, **kwargs):
        """
        SetText(self, String text)

        Sets the text for this UI element.
        """
        return __core.UpdateUIEvent_SetText(*args, **kwargs)

    def SetUpdateInterval(*args, **kwargs):
        """
        SetUpdateInterval(long updateInterval)

        Sets the interval between updates in milliseconds. Set to -1 to
        disable updates, or to 0 to update as frequently as possible. The
        default is 0.

        Use this to reduce the overhead of UI update events if your
        application has a lot of windows. If you set the value to -1 or
        greater than 0, you may also need to call `wx.Window.UpdateWindowUI`
        at appropriate points in your application, such as when a dialog is
        about to be shown.
        """
        return __core.UpdateUIEvent_SetUpdateInterval(*args, **kwargs)

    SetUpdateInterval = staticmethod(SetUpdateInterval)
    def GetUpdateInterval(*args, **kwargs):
        """
        GetUpdateInterval() -> long

        Returns the current interval between updates in milliseconds. -1
        disables updates, 0 updates as frequently as possible.
        """
        return __core.UpdateUIEvent_GetUpdateInterval(*args, **kwargs)

    GetUpdateInterval = staticmethod(GetUpdateInterval)
    def CanUpdate(*args, **kwargs):
        """
        CanUpdate(Window win) -> bool

        Returns ``True`` if it is appropriate to update (send UI update events
        to) this window.

        This function looks at the mode used (see `wx.UpdateUIEvent.SetMode`),
        the wx.WS_EX_PROCESS_UPDATE_EVENTS flag in window, the time update
        events were last sent in idle time, and the update interval, to
        determine whether events should be sent to this window now. By default
        this will always return true because the update mode is initially
        wx.UPDATE_UI_PROCESS_ALL and the interval is set to 0; so update
        events will be sent as often as possible. You can reduce the frequency
        that events are sent by changing the mode and/or setting an update
        interval.

        """
        return __core.UpdateUIEvent_CanUpdate(*args, **kwargs)

    CanUpdate = staticmethod(CanUpdate)
    def ResetUpdateTime(*args, **kwargs):
        """
        ResetUpdateTime()

        Used internally to reset the last-updated time to the current time. It
        is assumed that update events are normally sent in idle time, so this
        is called at the end of idle processing.
        """
        return __core.UpdateUIEvent_ResetUpdateTime(*args, **kwargs)

    ResetUpdateTime = staticmethod(ResetUpdateTime)
    def SetMode(*args, **kwargs):
        """
        SetMode(int mode)

        Specify how wxWidgets will send update events: to all windows, or only
        to those which specify that they will process the events.

        The mode may be one of the following values:

            =============================   ==========================================
            wxUPDATE_UI_PROCESS_ALL         Send UI update events to all windows.  This
                                            is the default setting.
            wxUPDATE_UI_PROCESS_SPECIFIED   Send UI update events only to windows that
                                            have the wx.WS_EX_PROCESS_UI_UPDATES extra
                                            style set.
            =============================   ==========================================

        """
        return __core.UpdateUIEvent_SetMode(*args, **kwargs)

    SetMode = staticmethod(SetMode)
    def GetMode(*args, **kwargs):
        """
        GetMode() -> int

        Returns a value specifying how wxWidgets will send update events: to
        all windows, or only to those which specify that they will process the
        events.
        """
        return __core.UpdateUIEvent_GetMode(*args, **kwargs)

    GetMode = staticmethod(GetMode)
    Checked = property(GetChecked,Check,doc="See `GetChecked`") 
    Enabled = property(GetEnabled,Enable,doc="See `GetEnabled`") 
    Shown = property(GetShown,Show,doc="See `GetShown`") 
    Text = property(GetText,SetText,doc="See `GetText` and `SetText`") 
__core.UpdateUIEvent_swigregister(UpdateUIEvent)

def UpdateUIEvent_SetUpdateInterval(*args, **kwargs):
  """
    UpdateUIEvent_SetUpdateInterval(long updateInterval)

    Sets the interval between updates in milliseconds. Set to -1 to
    disable updates, or to 0 to update as frequently as possible. The
    default is 0.

    Use this to reduce the overhead of UI update events if your
    application has a lot of windows. If you set the value to -1 or
    greater than 0, you may also need to call `wx.Window.UpdateWindowUI`
    at appropriate points in your application, such as when a dialog is
    about to be shown.
    """
  return __core.UpdateUIEvent_SetUpdateInterval(*args, **kwargs)

def UpdateUIEvent_GetUpdateInterval(*args):
  """
    UpdateUIEvent_GetUpdateInterval() -> long

    Returns the current interval between updates in milliseconds. -1
    disables updates, 0 updates as frequently as possible.
    """
  return __core.UpdateUIEvent_GetUpdateInterval(*args)

def UpdateUIEvent_CanUpdate(*args, **kwargs):
  """
    UpdateUIEvent_CanUpdate(Window win) -> bool

    Returns ``True`` if it is appropriate to update (send UI update events
    to) this window.

    This function looks at the mode used (see `wx.UpdateUIEvent.SetMode`),
    the wx.WS_EX_PROCESS_UPDATE_EVENTS flag in window, the time update
    events were last sent in idle time, and the update interval, to
    determine whether events should be sent to this window now. By default
    this will always return true because the update mode is initially
    wx.UPDATE_UI_PROCESS_ALL and the interval is set to 0; so update
    events will be sent as often as possible. You can reduce the frequency
    that events are sent by changing the mode and/or setting an update
    interval.

    """
  return __core.UpdateUIEvent_CanUpdate(*args, **kwargs)

def UpdateUIEvent_ResetUpdateTime(*args):
  """
    UpdateUIEvent_ResetUpdateTime()

    Used internally to reset the last-updated time to the current time. It
    is assumed that update events are normally sent in idle time, so this
    is called at the end of idle processing.
    """
  return __core.UpdateUIEvent_ResetUpdateTime(*args)

def UpdateUIEvent_SetMode(*args, **kwargs):
  """
    UpdateUIEvent_SetMode(int mode)

    Specify how wxWidgets will send update events: to all windows, or only
    to those which specify that they will process the events.

    The mode may be one of the following values:

        =============================   ==========================================
        wxUPDATE_UI_PROCESS_ALL         Send UI update events to all windows.  This
                                        is the default setting.
        wxUPDATE_UI_PROCESS_SPECIFIED   Send UI update events only to windows that
                                        have the wx.WS_EX_PROCESS_UI_UPDATES extra
                                        style set.
        =============================   ==========================================

    """
  return __core.UpdateUIEvent_SetMode(*args, **kwargs)

def UpdateUIEvent_GetMode(*args):
  """
    UpdateUIEvent_GetMode() -> int

    Returns a value specifying how wxWidgets will send update events: to
    all windows, or only to those which specify that they will process the
    events.
    """
  return __core.UpdateUIEvent_GetMode(*args)

#---------------------------------------------------------------------------

class SysColourChangedEvent(Event):
    """
    This class is used for EVT_SYS_COLOUR_CHANGED, which are generated
    when the user changes the colour settings using the control
    panel. This is only applicable under Windows.

    The default event handler for this event propagates the event to child
    windows, since Windows only sends the events to top-level windows. If
    intercepting this event for a top-level window, remember to call
    `Skip` so the the base class handler will still be executed, or to
    pass the event on to the window's children explicitly.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> SysColourChangedEvent

        Constructor
        """
        this = __core.new_SysColourChangedEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.SysColourChangedEvent_swigregister(SysColourChangedEvent)

#---------------------------------------------------------------------------

class MouseCaptureChangedEvent(Event):
    """
    An mouse capture changed event (EVT_MOUSE_CAPTURE_CHANGED) is sent to
    a window that loses its mouse capture. This is called even if
    `wx.Window.ReleaseMouse` was called by the application code. Handling
    this event allows an application to cater for unexpected capture
    releases which might otherwise confuse mouse handling code.

    This event is implemented under Windows only.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int winid=0, Window gainedCapture=None) -> MouseCaptureChangedEvent

        Constructor
        """
        this = __core.new_MouseCaptureChangedEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetCapturedWindow(*args, **kwargs):
        """
        GetCapturedWindow(self) -> Window

        Returns the window that gained the capture, or ``None`` if it was a
        non-wxWidgets window.
        """
        return __core.MouseCaptureChangedEvent_GetCapturedWindow(*args, **kwargs)

    CapturedWindow = property(GetCapturedWindow,doc="See `GetCapturedWindow`") 
__core.MouseCaptureChangedEvent_swigregister(MouseCaptureChangedEvent)

#---------------------------------------------------------------------------

class MouseCaptureLostEvent(Event):
    """
    A mouse capture lost event is sent to a window that obtained mouse
    capture, which was subsequently loss due to "external" event, for
    example when a dialog box is shown or if another application captures
    the mouse.

    If this happens, this event is sent to all windows that are on the
    capture stack (i.e. a window that called `wx.Window.CaptureMouse`, but
    didn't call `wx.Window.ReleaseMouse` yet). The event is *not* sent
    if the capture changes because of a call to CaptureMouse or
    ReleaseMouse.

    This event is currently emitted under Windows only.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int winid=0) -> MouseCaptureLostEvent

        A mouse capture lost event is sent to a window that obtained mouse
        capture, which was subsequently loss due to "external" event, for
        example when a dialog box is shown or if another application captures
        the mouse.

        If this happens, this event is sent to all windows that are on the
        capture stack (i.e. a window that called `wx.Window.CaptureMouse`, but
        didn't call `wx.Window.ReleaseMouse` yet). The event is *not* sent
        if the capture changes because of a call to CaptureMouse or
        ReleaseMouse.

        This event is currently emitted under Windows only.

        """
        this = __core.new_MouseCaptureLostEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.MouseCaptureLostEvent_swigregister(MouseCaptureLostEvent)

#---------------------------------------------------------------------------

class DisplayChangedEvent(Event):
    """
    An EVT_DISPLAY_CHANGED event is sent to all windows when the display
    resolution has changed.

    This event is implemented under Windows only.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> DisplayChangedEvent"""
        this = __core.new_DisplayChangedEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.DisplayChangedEvent_swigregister(DisplayChangedEvent)

#---------------------------------------------------------------------------

class PaletteChangedEvent(Event):
    """
    An EVT_PALETTE_CHANGED event is sent when the system palette has
    changed, thereby giving each window a chance to redo their own to
    match.

    This event is implemented under Windows only.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int id=0) -> PaletteChangedEvent

        An EVT_PALETTE_CHANGED event is sent when the system palette has
        changed, thereby giving each window a chance to redo their own to
        match.

        This event is implemented under Windows only.
        """
        this = __core.new_PaletteChangedEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def SetChangedWindow(*args, **kwargs):
        """SetChangedWindow(self, Window win)"""
        return __core.PaletteChangedEvent_SetChangedWindow(*args, **kwargs)

    def GetChangedWindow(*args, **kwargs):
        """GetChangedWindow(self) -> Window"""
        return __core.PaletteChangedEvent_GetChangedWindow(*args, **kwargs)

    ChangedWindow = property(GetChangedWindow,SetChangedWindow,doc="See `GetChangedWindow` and `SetChangedWindow`") 
__core.PaletteChangedEvent_swigregister(PaletteChangedEvent)

#---------------------------------------------------------------------------

class QueryNewPaletteEvent(Event):
    """
    An EVT_QUERY_NEW_PALETE event indicates the window is getting keyboard
    focus and should re-do its palette.

    This event is implemented under Windows only.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int winid=0) -> QueryNewPaletteEvent

        Constructor.
        """
        this = __core.new_QueryNewPaletteEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def SetPaletteRealized(*args, **kwargs):
        """
        SetPaletteRealized(self, bool realized)

        App should set this if it changes the palette.
        """
        return __core.QueryNewPaletteEvent_SetPaletteRealized(*args, **kwargs)

    def GetPaletteRealized(*args, **kwargs):
        """GetPaletteRealized(self) -> bool"""
        return __core.QueryNewPaletteEvent_GetPaletteRealized(*args, **kwargs)

    PaletteRealized = property(GetPaletteRealized,SetPaletteRealized,doc="See `GetPaletteRealized` and `SetPaletteRealized`") 
__core.QueryNewPaletteEvent_swigregister(QueryNewPaletteEvent)

#---------------------------------------------------------------------------

class NavigationKeyEvent(Event):
    """
    EVT_NAVIGATION_KEY events are used to control moving the focus between
    widgets, otherwise known as tab-traversal.  You woudl normally not
    catch navigation events in applications as there are already
    appropriate handlers in `wx.Dialog` and `wx.Panel`, but you may find
    it useful to send navigation events in certain situations to change
    the focus in certain ways, although it's probably easier to just call
    `wx.Window.Navigate`.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> NavigationKeyEvent"""
        this = __core.new_NavigationKeyEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetDirection(*args, **kwargs):
        """
        GetDirection(self) -> bool

        Returns ``True`` if the direction is forward, ``False`` otherwise.
        """
        return __core.NavigationKeyEvent_GetDirection(*args, **kwargs)

    def SetDirection(*args, **kwargs):
        """
        SetDirection(self, bool forward)

        Specify the direction that the navigation should take.  Usually the
        difference between using Tab and Shift-Tab.
        """
        return __core.NavigationKeyEvent_SetDirection(*args, **kwargs)

    def IsWindowChange(*args, **kwargs):
        """
        IsWindowChange(self) -> bool

        Returns ``True`` if window change is allowed.
        """
        return __core.NavigationKeyEvent_IsWindowChange(*args, **kwargs)

    def SetWindowChange(*args, **kwargs):
        """
        SetWindowChange(self, bool ischange)

        Specify if the navigation should be able to change parent windows.
        For example, changing notebook pages, etc. This is usually implemented
        by using Control-Tab.
        """
        return __core.NavigationKeyEvent_SetWindowChange(*args, **kwargs)

    def IsFromTab(*args, **kwargs):
        """
        IsFromTab(self) -> bool

        Returns ``True`` if the navigation event is originated from the Tab
        key.
        """
        return __core.NavigationKeyEvent_IsFromTab(*args, **kwargs)

    def SetFromTab(*args, **kwargs):
        """
        SetFromTab(self, bool bIs)

        Set to true under MSW if the event was generated using the tab key.
        This is required for proper navogation over radio buttons.
        """
        return __core.NavigationKeyEvent_SetFromTab(*args, **kwargs)

    def SetFlags(*args, **kwargs):
        """
        SetFlags(self, long flags)

        Set the navigation flags to a combination of the following:

            * wx.NavigationKeyEvent.IsBackward
            * wx.NavigationKeyEvent.IsForward
            * wx.NavigationKeyEvent.WinChange
            * wx.NavigationKeyEvent.FromTab

        """
        return __core.NavigationKeyEvent_SetFlags(*args, **kwargs)

    def GetCurrentFocus(*args, **kwargs):
        """
        GetCurrentFocus(self) -> Window

        Returns the child window which currenty has the focus.  May be
        ``None``.
        """
        return __core.NavigationKeyEvent_GetCurrentFocus(*args, **kwargs)

    def SetCurrentFocus(*args, **kwargs):
        """
        SetCurrentFocus(self, Window win)

        Set the window that has the focus.
        """
        return __core.NavigationKeyEvent_SetCurrentFocus(*args, **kwargs)

    IsBackward = __core.NavigationKeyEvent_IsBackward
    IsForward = __core.NavigationKeyEvent_IsForward
    WinChange = __core.NavigationKeyEvent_WinChange
    FromTab = __core.NavigationKeyEvent_FromTab
    CurrentFocus = property(GetCurrentFocus,SetCurrentFocus,doc="See `GetCurrentFocus` and `SetCurrentFocus`") 
    Direction = property(GetDirection,SetDirection,doc="See `GetDirection` and `SetDirection`") 
__core.NavigationKeyEvent_swigregister(NavigationKeyEvent)

#---------------------------------------------------------------------------

class WindowCreateEvent(CommandEvent):
    """
    The EVT_WINDOW_CREATE event is sent as soon as the window object (the
    underlying GUI object) exists.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window win=None) -> WindowCreateEvent

        The EVT_WINDOW_CREATE event is sent as soon as the window object (the
        underlying GUI object) exists.
        """
        this = __core.new_WindowCreateEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetWindow(*args, **kwargs):
        """
        GetWindow(self) -> Window

        Returns the window that this event refers to.
        """
        return __core.WindowCreateEvent_GetWindow(*args, **kwargs)

    Window = property(GetWindow,doc="See `GetWindow`") 
__core.WindowCreateEvent_swigregister(WindowCreateEvent)

class WindowDestroyEvent(CommandEvent):
    """
    The EVT_WINDOW_DESTROY event is sent from the `wx.Window` destructor
    when the GUI window is destroyed.

    When a class derived from `wx.Window` is destroyed its destructor will
    have already run by the time this event is sent. Therefore this event
    will not usually be received at all by the window itself.  Since it is
    received after the destructor has run, an object should not try to
    handle its own wx.WindowDestroyEvent, but it can be used to get
    notification of the destruction of another window.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window win=None) -> WindowDestroyEvent

        The EVT_WINDOW_DESTROY event is sent from the `wx.Window` destructor
        when the GUI window is destroyed.

        When a class derived from `wx.Window` is destroyed its destructor will
        have already run by the time this event is sent. Therefore this event
        will not usually be received at all by the window itself.  Since it is
        received after the destructor has run, an object should not try to
        handle its own wx.WindowDestroyEvent, but it can be used to get
        notification of the destruction of another window.
        """
        this = __core.new_WindowDestroyEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetWindow(*args, **kwargs):
        """
        GetWindow(self) -> Window

        Returns the window that this event refers to.
        """
        return __core.WindowDestroyEvent_GetWindow(*args, **kwargs)

    Window = property(GetWindow,doc="See `GetWindow`") 
__core.WindowDestroyEvent_swigregister(WindowDestroyEvent)

#---------------------------------------------------------------------------

class ContextMenuEvent(CommandEvent):
    """
    This class is used for context menu events (EVT_CONTECT_MENU,) sent to
    give the application a chance to show a context (popup) menu.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType type=wxEVT_NULL, int winid=0, Point pt=DefaultPosition) -> ContextMenuEvent

        Constructor.
        """
        this = __core.new_ContextMenuEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> Point

        Returns the position (in screen coordinants) at which the menu should
        be shown.
        """
        return __core.ContextMenuEvent_GetPosition(*args, **kwargs)

    def SetPosition(*args, **kwargs):
        """
        SetPosition(self, Point pos)

        Sets the position at which the menu should be shown.
        """
        return __core.ContextMenuEvent_SetPosition(*args, **kwargs)

    Position = property(GetPosition,SetPosition,doc="See `GetPosition` and `SetPosition`") 
__core.ContextMenuEvent_swigregister(ContextMenuEvent)

#---------------------------------------------------------------------------

IDLE_PROCESS_ALL = __core.IDLE_PROCESS_ALL
IDLE_PROCESS_SPECIFIED = __core.IDLE_PROCESS_SPECIFIED
class IdleEvent(Event):
    """
    This class is used for EVT_IDLE events, which are generated and sent
    when the application *becomes* idle.  In other words, the when the
    event queue becomes empty then idle events are sent to all windows (by
    default) and as long as none of them call `RequestMore` then there are
    no more idle events until after the system event queue has some normal
    events and then becomes empty again.

    By default, idle events are sent to all windows. If this is causing a
    significant overhead in your application, you can call
    `wx.IdleEvent.SetMode` with the value wx.IDLE_PROCESS_SPECIFIED, and
    set the wx.WS_EX_PROCESS_IDLE extra window style for every window
    which should receive idle events.  Then idle events will only be sent
    to those windows and not to any others.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> IdleEvent

        Constructor
        """
        this = __core.new_IdleEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def RequestMore(*args, **kwargs):
        """
        RequestMore(self, bool needMore=True)

        Tells wxWidgets that more processing is required. This function can be
        called by an EVT_IDLE handler for a window to indicate that the
        application should forward the EVT_IDLE event once more to the
        application windows. If no window calls this function during its
        EVT_IDLE handler, then the application will remain in a passive event
        loop until a new event is posted to the application by the windowing
        system.
        """
        return __core.IdleEvent_RequestMore(*args, **kwargs)

    def MoreRequested(*args, **kwargs):
        """
        MoreRequested(self) -> bool

        Returns ``True`` if the OnIdle function processing this event
        requested more processing time.
        """
        return __core.IdleEvent_MoreRequested(*args, **kwargs)

    def SetMode(*args, **kwargs):
        """
        SetMode(int mode)

        Static method for specifying how wxWidgets will send idle events: to
        all windows, or only to those which specify that they will process the
        events.

        The mode can be one of the following values:

            =========================   ========================================
            wx.IDLE_PROCESS_ALL         Send idle events to all windows
            wx.IDLE_PROCESS_SPECIFIED   Send idle events only to windows that have
                                        the wx.WS_EX_PROCESS_IDLE extra style
                                        flag set.
            =========================   ========================================

        """
        return __core.IdleEvent_SetMode(*args, **kwargs)

    SetMode = staticmethod(SetMode)
    def GetMode(*args, **kwargs):
        """
        GetMode() -> int

        Static method returning a value specifying how wxWidgets will send
        idle events: to all windows, or only to those which specify that they
        will process the events.
        """
        return __core.IdleEvent_GetMode(*args, **kwargs)

    GetMode = staticmethod(GetMode)
__core.IdleEvent_swigregister(IdleEvent)

def IdleEvent_SetMode(*args, **kwargs):
  """
    IdleEvent_SetMode(int mode)

    Static method for specifying how wxWidgets will send idle events: to
    all windows, or only to those which specify that they will process the
    events.

    The mode can be one of the following values:

        =========================   ========================================
        wx.IDLE_PROCESS_ALL         Send idle events to all windows
        wx.IDLE_PROCESS_SPECIFIED   Send idle events only to windows that have
                                    the wx.WS_EX_PROCESS_IDLE extra style
                                    flag set.
        =========================   ========================================

    """
  return __core.IdleEvent_SetMode(*args, **kwargs)

def IdleEvent_GetMode(*args):
  """
    IdleEvent_GetMode() -> int

    Static method returning a value specifying how wxWidgets will send
    idle events: to all windows, or only to those which specify that they
    will process the events.
    """
  return __core.IdleEvent_GetMode(*args)

#---------------------------------------------------------------------------

class ClipboardTextEvent(CommandEvent):
    """
    A Clipboard Text event is sent when a window intercepts a text
    copy/cut/paste message, i.e. the user has cut/copied/pasted data
    from/into a text control via ctrl-C/X/V, ctrl/shift-del/insert, a
    popup menu command, etc.  NOTE : under windows these events are *NOT*
    generated automatically for a Rich Edit text control.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType type=wxEVT_NULL, int winid=0) -> ClipboardTextEvent

        A Clipboard Text event is sent when a window intercepts a text
        copy/cut/paste message, i.e. the user has cut/copied/pasted data
        from/into a text control via ctrl-C/X/V, ctrl/shift-del/insert, a
        popup menu command, etc.  NOTE : under windows these events are *NOT*
        generated automatically for a Rich Edit text control.
        """
        this = __core.new_ClipboardTextEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.ClipboardTextEvent_swigregister(ClipboardTextEvent)

#---------------------------------------------------------------------------

class PyEvent(Event):
    """
    wx.PyEvent can be used as a base class for implementing custom event
    types in Python.  You should derived from this class instead of
    `wx.Event` because this class is Python-aware and is able to transport
    its Python bits safely through the wxWidgets event system and have
    them still be there when the event handler is invoked.

    :see: `wx.PyCommandEvent`

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, int winid=0, EventType eventType=wxEVT_NULL) -> PyEvent"""
        this = __core.new_PyEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._SetSelf(self)

    __swig_destroy__ = __core.delete_PyEvent
    __del__ = lambda self : None;
    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return __core.PyEvent__SetSelf(*args, **kwargs)

    def _GetSelf(*args, **kwargs):
        """_GetSelf(self) -> PyObject"""
        return __core.PyEvent__GetSelf(*args, **kwargs)

__core.PyEvent_swigregister(PyEvent)

class PyCommandEvent(CommandEvent):
    """
    wx.PyCommandEvent can be used as a base class for implementing custom
    event types in Python, where the event should travel up to parent
    windows looking for a handler.  You should derived from this class
    instead of `wx.CommandEvent` because this class is Python-aware and is
    able to transport its Python bits safely through the wxWidgets event
    system and have them still be there when the event handler is invoked.

    :see: `wx.PyEvent`

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, EventType eventType=wxEVT_NULL, int id=0) -> PyCommandEvent"""
        this = __core.new_PyCommandEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._SetSelf(self)

    __swig_destroy__ = __core.delete_PyCommandEvent
    __del__ = lambda self : None;
    def _SetSelf(*args, **kwargs):
        """_SetSelf(self, PyObject self)"""
        return __core.PyCommandEvent__SetSelf(*args, **kwargs)

    def _GetSelf(*args, **kwargs):
        """_GetSelf(self) -> PyObject"""
        return __core.PyCommandEvent__GetSelf(*args, **kwargs)

__core.PyCommandEvent_swigregister(PyCommandEvent)

class DateEvent(CommandEvent):
    """
    This event class holds information about a date change event and is
    used together with `wx.DatePickerCtrl`. It also serves as a base class
    for `wx.calendar.CalendarEvent`.  Bind these event types with
    EVT_DATE_CHANGED.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, Window win, DateTime dt, EventType type) -> DateEvent"""
        this = __core.new_DateEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetDate(*args, **kwargs):
        """
        GetDate(self) -> DateTime

        Returns the date.
        """
        return __core.DateEvent_GetDate(*args, **kwargs)

    def SetDate(*args, **kwargs):
        """
        SetDate(self, DateTime date)

        Sets the date carried by the event, normally only used by the library
        internally.
        """
        return __core.DateEvent_SetDate(*args, **kwargs)

    Date = property(GetDate,SetDate,doc="See `GetDate` and `SetDate`") 
__core.DateEvent_swigregister(DateEvent)

wxEVT_DATE_CHANGED = __core.wxEVT_DATE_CHANGED
EVT_DATE_CHANGED = wx.PyEventBinder( wxEVT_DATE_CHANGED, 1 )

class EventBlocker(EvtHandler):
    """Helper class to temporarily disable event handling for a window."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window win, EventType type=wxEVT_ANY) -> EventBlocker

        Helper class to temporarily disable event handling for a window.
        """
        this = __core.new_EventBlocker(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_EventBlocker
    __del__ = lambda self : None;
    def Block(*args, **kwargs):
        """Block(self, EventType type)"""
        return __core.EventBlocker_Block(*args, **kwargs)

__core.EventBlocker_swigregister(EventBlocker)

#---------------------------------------------------------------------------

PYAPP_ASSERT_SUPPRESS = __core.PYAPP_ASSERT_SUPPRESS
PYAPP_ASSERT_EXCEPTION = __core.PYAPP_ASSERT_EXCEPTION
PYAPP_ASSERT_DIALOG = __core.PYAPP_ASSERT_DIALOG
PYAPP_ASSERT_LOG = __core.PYAPP_ASSERT_LOG
PRINT_WINDOWS = __core.PRINT_WINDOWS
PRINT_POSTSCRIPT = __core.PRINT_POSTSCRIPT
class PyApp(EvtHandler):
    """
    The ``wx.PyApp`` class is an *implementation detail*, please use the
    `wx.App` class (or some other derived class) instead.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PyApp

        Create a new application object, starting the bootstrap process.
        """
        this = __core.new_PyApp(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self, False);PyApp._setCallbackInfo(self, self, PyApp);self.this.own(True)

    __swig_destroy__ = __core.delete_PyApp
    __del__ = lambda self : None;
    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class, bool incref=False)"""
        return __core.PyApp__setCallbackInfo(*args, **kwargs)

    def GetAppName(*args, **kwargs):
        """
        GetAppName(self) -> String

        Get the application name.
        """
        return __core.PyApp_GetAppName(*args, **kwargs)

    def SetAppName(*args, **kwargs):
        """
        SetAppName(self, String name)

        Set the application name. This value may be used automatically by
        `wx.Config` and such.
        """
        return __core.PyApp_SetAppName(*args, **kwargs)

    def GetAppDisplayName(*args, **kwargs):
        """
        GetAppDisplayName(self) -> String

        Get the application display name.
        """
        return __core.PyApp_GetAppDisplayName(*args, **kwargs)

    def SetAppDisplayName(*args, **kwargs):
        """
        SetAppDisplayName(self, String name)

        Set the application display name.  The display name is the name shown
        to the user in titles, reports, etc while the app name is used for
        paths, config, and other places the user doesn't see, for example the
        app name could be myapp while display name could be 'My App'

        """
        return __core.PyApp_SetAppDisplayName(*args, **kwargs)

    def GetClassName(*args, **kwargs):
        """
        GetClassName(self) -> String

        Get the application's class name.
        """
        return __core.PyApp_GetClassName(*args, **kwargs)

    def SetClassName(*args, **kwargs):
        """
        SetClassName(self, String name)

        Set the application's class name. This value may be used for
        X-resources if applicable for the platform
        """
        return __core.PyApp_SetClassName(*args, **kwargs)

    def GetVendorName(*args, **kwargs):
        """
        GetVendorName(self) -> String

        Get the application's vendor name.
        """
        return __core.PyApp_GetVendorName(*args, **kwargs)

    def SetVendorName(*args, **kwargs):
        """
        SetVendorName(self, String name)

        Set the application's vendor name. This value may be used
        automatically by `wx.Config` and such.
        """
        return __core.PyApp_SetVendorName(*args, **kwargs)

    def GetVendorDisplayName(*args, **kwargs):
        """
        GetVendorDisplayName(self) -> String

        Get the vendor display name.
        """
        return __core.PyApp_GetVendorDisplayName(*args, **kwargs)

    def SetVendorDisplayName(*args, **kwargs):
        """
        SetVendorDisplayName(self, String name)

        Set the vendor display name.  The display name is shown in
        titles/reports/dialogs to the user, while the vendor name is used in
        some areas such as wxConfig, wxStandardPaths, etc.
        """
        return __core.PyApp_SetVendorDisplayName(*args, **kwargs)

    def GetTraits(*args, **kwargs):
        """
        GetTraits(self) -> wxAppTraits

        Return (and create if necessary) the app traits object to which we
        delegate for everything which either should be configurable by the
        user (then he can change the default behaviour simply by overriding
        CreateTraits() and returning his own traits object) or which is
        GUI/console dependent as then wx.AppTraits allows us to abstract the
        differences behind the common facade.

        :todo: Add support for overriding CreateAppTraits in wxPython.
        """
        return __core.PyApp_GetTraits(*args, **kwargs)

    def GetTraitsIfExists(*args, **kwargs):
        """
        GetTraitsIfExists() -> wxAppTraits

        This function provides safer access to traits object than
        wx.GetApp().GetTraits() during startup or termination when the global
        application object itself may be unavailable.
        """
        return __core.PyApp_GetTraitsIfExists(*args, **kwargs)

    GetTraitsIfExists = staticmethod(GetTraitsIfExists)
    def GetMainLoop(*args, **kwargs):
        """
        GetMainLoop(self) -> EventLoopBase

        Returns the main event loop instance, i.e. the event loop which is started
        by OnRun() and which dispatches all events sent from the native toolkit
        to the application (except when new event loops are temporarily set-up).
        The returned value maybe None. Put initialization code which needs a
        non-None main event loop into OnEventLoopEnter().
        """
        return __core.PyApp_GetMainLoop(*args, **kwargs)

    def SuspendProcessingOfPendingEvents(*args, **kwargs):
        """
        SuspendProcessingOfPendingEvents(self)

        Temporarily suspends the processing of pending events.
        """
        return __core.PyApp_SuspendProcessingOfPendingEvents(*args, **kwargs)

    def ResumeProcessingOfPendingEvents(*args, **kwargs):
        """
        ResumeProcessingOfPendingEvents(self)

        Resume (after having been suspended) the processing of pending events.
        """
        return __core.PyApp_ResumeProcessingOfPendingEvents(*args, **kwargs)

    def ProcessPendingEvents(*args, **kwargs):
        """
        ProcessPendingEvents(self)

        Process all events in the Pending Events list -- it is necessary to
        call this function to process posted events. This normally happens
        during each event loop iteration.
        """
        return __core.PyApp_ProcessPendingEvents(*args, **kwargs)

    def HasPendingEvents(*args, **kwargs):
        """
        HasPendingEvents(self) -> bool

        Check if there are pending events on global pending event list
        """
        return __core.PyApp_HasPendingEvents(*args, **kwargs)

    def RemovePendingEventHandler(*args, **kwargs):
        """RemovePendingEventHandler(self, EvtHandler toRemove)"""
        return __core.PyApp_RemovePendingEventHandler(*args, **kwargs)

    def AppendPendingEventHandler(*args, **kwargs):
        """AppendPendingEventHandler(self, EvtHandler toAppend)"""
        return __core.PyApp_AppendPendingEventHandler(*args, **kwargs)

    def DelayPendingEventHandler(*args, **kwargs):
        """DelayPendingEventHandler(self, EvtHandler toDelay)"""
        return __core.PyApp_DelayPendingEventHandler(*args, **kwargs)

    def DeletePendingEvents(*args, **kwargs):
        """DeletePendingEvents(self)"""
        return __core.PyApp_DeletePendingEvents(*args, **kwargs)

    def ScheduleForDestruction(*args, **kwargs):
        """ScheduleForDestruction(self, Object object)"""
        return __core.PyApp_ScheduleForDestruction(*args, **kwargs)

    def IsScheduledForDestruction(*args, **kwargs):
        """IsScheduledForDestruction(self, Object object) -> bool"""
        return __core.PyApp_IsScheduledForDestruction(*args, **kwargs)

    def Yield(*args, **kwargs):
        """
        Yield(self, bool onlyIfNeeded=False) -> bool

        Process all currently pending events right now, instead of waiting
        until return to the event loop.  It is an error to call ``Yield``
        recursively unless the value of ``onlyIfNeeded`` is True.

        :warning: This function is dangerous as it can lead to unexpected
              reentrancies (i.e. when called from an event handler it may
              result in calling the same event handler again), use with
              extreme care or, better, don't use at all!

        :see: `wx.Yield`, `wx.YieldIfNeeded`, `wx.SafeYield`

        """
        return __core.PyApp_Yield(*args, **kwargs)

    def SafeYield(*args, **kwargs):
        """SafeYield(self, Window win, bool onlyIfNeeded) -> bool"""
        return __core.PyApp_SafeYield(*args, **kwargs)

    def SafeYieldFor(*args, **kwargs):
        """SafeYieldFor(self, Window win, long eventsToProcess) -> bool"""
        return __core.PyApp_SafeYieldFor(*args, **kwargs)

    def WakeUpIdle(*args, **kwargs):
        """
        WakeUpIdle(self)

        Make sure that idle events are sent again.
        :see: `wx.WakeUpIdle`
        """
        return __core.PyApp_WakeUpIdle(*args, **kwargs)

    def IsMainLoopRunning(*args, **kwargs):
        """
        IsMainLoopRunning() -> bool

        Returns True if we're running the main loop, i.e. if the events can
        currently be dispatched.
        """
        return __core.PyApp_IsMainLoopRunning(*args, **kwargs)

    IsMainLoopRunning = staticmethod(IsMainLoopRunning)
    def MainLoop(*args, **kwargs):
        """
        MainLoop(self) -> int

        Execute the main GUI loop, the function doesn't normally return until
        all top level windows have been closed and destroyed.
        """
        return __core.PyApp_MainLoop(*args, **kwargs)

    def Exit(*args, **kwargs):
        """
        Exit(self)

        Exit the main loop thus terminating the application.
        :see: `wx.Exit`
        """
        return __core.PyApp_Exit(*args, **kwargs)

    def GetLayoutDirection(*args, **kwargs):
        """
        GetLayoutDirection(self) -> int

        Return the layout direction for the current locale.
        """
        return __core.PyApp_GetLayoutDirection(*args, **kwargs)

    def SetNativeTheme(*args, **kwargs):
        """
        SetNativeTheme(self, String theme) -> bool

        Change the theme used by the application, return true on success.
        """
        return __core.PyApp_SetNativeTheme(*args, **kwargs)

    def ExitMainLoop(*args, **kwargs):
        """
        ExitMainLoop(self)

        Exit the main GUI loop during the next iteration of the main
        loop, (i.e. it does not stop the program immediately!)
        """
        return __core.PyApp_ExitMainLoop(*args, **kwargs)

    def FilterEvent(*args, **kwargs):
        """
        FilterEvent(self, Event event) -> int

        Filters all events. `SetCallFilterEvent` controls whether or not your
        override is called.
        """
        return __core.PyApp_FilterEvent(*args, **kwargs)

    def GetCallFilterEvent(*args, **kwargs):
        """
        GetCallFilterEvent(self) -> bool

        Returns the state of the Call FilterEvent flag.
        """
        return __core.PyApp_GetCallFilterEvent(*args, **kwargs)

    def SetCallFilterEvent(*args, **kwargs):
        """
        SetCallFilterEvent(self, bool callFilterEvent=True)

        Set the Call FilterEvent flag. When set your override of FilterEvent
        will be called.  SetCallFilterEvent's purpose is to avoid any
        performance penalty when you have overriden FilterEvent, but don't
        want it to be called, and also to reduce the runtime overhead when it
        is not overridden.
        """
        return __core.PyApp_SetCallFilterEvent(*args, **kwargs)

    def Pending(*args, **kwargs):
        """
        Pending(self) -> bool

        Returns True if there are unprocessed events in the event queue.
        """
        return __core.PyApp_Pending(*args, **kwargs)

    def Dispatch(*args, **kwargs):
        """
        Dispatch(self) -> bool

        Process the first event in the event queue (blocks until an event
        appears if there are none currently)
        """
        return __core.PyApp_Dispatch(*args, **kwargs)

    def ProcessIdle(*args, **kwargs):
        """
        ProcessIdle(self) -> bool

        Called from the MainLoop when the application becomes idle (there are
        no pending events) and sends a `wx.IdleEvent` to all interested
        parties.  Returns True if more idle events are needed, False if not.
        """
        return __core.PyApp_ProcessIdle(*args, **kwargs)

    def IsActive(*args, **kwargs):
        """
        IsActive(self) -> bool

        Return True if our app has focus.
        """
        return __core.PyApp_IsActive(*args, **kwargs)

    def SetTopWindow(*args, **kwargs):
        """
        SetTopWindow(self, Window win)

        Set the *main* top level window
        """
        return __core.PyApp_SetTopWindow(*args, **kwargs)

    def GetTopWindow(*args, **kwargs):
        """
        GetTopWindow(self) -> Window

        Return the *main* top level window (if it hadn't been set previously
        with SetTopWindow(), will return just some top level window and, if
        there not any, will return None)
        """
        return __core.PyApp_GetTopWindow(*args, **kwargs)

    def SetExitOnFrameDelete(*args, **kwargs):
        """
        SetExitOnFrameDelete(self, bool flag)

        Control the exit behaviour: by default, the program will exit the main
        loop (and so, usually, terminate) when the last top-level program
        window is deleted.  Beware that if you disable this behaviour (with
        SetExitOnFrameDelete(False)), you'll have to call ExitMainLoop()
        explicitly from somewhere.
        """
        return __core.PyApp_SetExitOnFrameDelete(*args, **kwargs)

    def GetExitOnFrameDelete(*args, **kwargs):
        """
        GetExitOnFrameDelete(self) -> bool

        Get the current exit behaviour setting.
        """
        return __core.PyApp_GetExitOnFrameDelete(*args, **kwargs)

    def SetUseBestVisual(*args, **kwargs):
        """
        SetUseBestVisual(self, bool flag, bool forceTrueColour=False)

        Set whether the app should try to use the best available visual on
        systems where more than one is available, (Sun, SGI, XFree86 4, etc.)
        """
        return __core.PyApp_SetUseBestVisual(*args, **kwargs)

    def GetUseBestVisual(*args, **kwargs):
        """
        GetUseBestVisual(self) -> bool

        Get current UseBestVisual setting.
        """
        return __core.PyApp_GetUseBestVisual(*args, **kwargs)

    def SetPrintMode(*args, **kwargs):
        """SetPrintMode(self, int mode)"""
        return __core.PyApp_SetPrintMode(*args, **kwargs)

    def GetPrintMode(*args, **kwargs):
        """GetPrintMode(self) -> int"""
        return __core.PyApp_GetPrintMode(*args, **kwargs)

    def SetAssertMode(*args, **kwargs):
        """
        SetAssertMode(self, int mode)

        Set the OnAssert behaviour for debug and hybrid builds.
        """
        return __core.PyApp_SetAssertMode(*args, **kwargs)

    def GetAssertMode(*args, **kwargs):
        """
        GetAssertMode(self) -> int

        Get the current OnAssert behaviour setting.
        """
        return __core.PyApp_GetAssertMode(*args, **kwargs)

    def MacHideApp(*args, **kwargs):
        """
        MacHideApp(self)

        Hide all application windows just as the user can do with the system
        Hide command.  Mac only.
        """
        return __core.PyApp_MacHideApp(*args, **kwargs)

    def GetMacSupportPCMenuShortcuts(*args, **kwargs):
        """GetMacSupportPCMenuShortcuts() -> bool"""
        return __core.PyApp_GetMacSupportPCMenuShortcuts(*args, **kwargs)

    GetMacSupportPCMenuShortcuts = staticmethod(GetMacSupportPCMenuShortcuts)
    def GetMacAboutMenuItemId(*args, **kwargs):
        """GetMacAboutMenuItemId() -> long"""
        return __core.PyApp_GetMacAboutMenuItemId(*args, **kwargs)

    GetMacAboutMenuItemId = staticmethod(GetMacAboutMenuItemId)
    def GetMacPreferencesMenuItemId(*args, **kwargs):
        """GetMacPreferencesMenuItemId() -> long"""
        return __core.PyApp_GetMacPreferencesMenuItemId(*args, **kwargs)

    GetMacPreferencesMenuItemId = staticmethod(GetMacPreferencesMenuItemId)
    def GetMacExitMenuItemId(*args, **kwargs):
        """GetMacExitMenuItemId() -> long"""
        return __core.PyApp_GetMacExitMenuItemId(*args, **kwargs)

    GetMacExitMenuItemId = staticmethod(GetMacExitMenuItemId)
    def GetMacHelpMenuTitleName(*args, **kwargs):
        """GetMacHelpMenuTitleName() -> String"""
        return __core.PyApp_GetMacHelpMenuTitleName(*args, **kwargs)

    GetMacHelpMenuTitleName = staticmethod(GetMacHelpMenuTitleName)
    def SetMacSupportPCMenuShortcuts(*args, **kwargs):
        """SetMacSupportPCMenuShortcuts(bool val)"""
        return __core.PyApp_SetMacSupportPCMenuShortcuts(*args, **kwargs)

    SetMacSupportPCMenuShortcuts = staticmethod(SetMacSupportPCMenuShortcuts)
    def SetMacAboutMenuItemId(*args, **kwargs):
        """SetMacAboutMenuItemId(long val)"""
        return __core.PyApp_SetMacAboutMenuItemId(*args, **kwargs)

    SetMacAboutMenuItemId = staticmethod(SetMacAboutMenuItemId)
    def SetMacPreferencesMenuItemId(*args, **kwargs):
        """SetMacPreferencesMenuItemId(long val)"""
        return __core.PyApp_SetMacPreferencesMenuItemId(*args, **kwargs)

    SetMacPreferencesMenuItemId = staticmethod(SetMacPreferencesMenuItemId)
    def SetMacExitMenuItemId(*args, **kwargs):
        """SetMacExitMenuItemId(long val)"""
        return __core.PyApp_SetMacExitMenuItemId(*args, **kwargs)

    SetMacExitMenuItemId = staticmethod(SetMacExitMenuItemId)
    def SetMacHelpMenuTitleName(*args, **kwargs):
        """SetMacHelpMenuTitleName(String val)"""
        return __core.PyApp_SetMacHelpMenuTitleName(*args, **kwargs)

    SetMacHelpMenuTitleName = staticmethod(SetMacHelpMenuTitleName)
    def _BootstrapApp(*args, **kwargs):
        """
        _BootstrapApp(self)

        For internal use only
        """
        return __core.PyApp__BootstrapApp(*args, **kwargs)

    def GetComCtl32Version(*args, **kwargs):
        """
        GetComCtl32Version() -> int

        Returns 400, 470, 471, etc. for comctl32.dll 4.00, 4.70, 4.71 or 0 if
        it wasn't found at all.  Raises an exception on non-Windows platforms.
        """
        return __core.PyApp_GetComCtl32Version(*args, **kwargs)

    GetComCtl32Version = staticmethod(GetComCtl32Version)
    def GetShell32Version(*args, **kwargs):
        """
        GetShell32Version() -> int

        Returns 400, 470, 471, etc. for shell32.dll 4.00, 4.70, 4.71 or 0 if
        it wasn't found at all.  Raises an exception on non-Windows platforms.
        """
        return __core.PyApp_GetShell32Version(*args, **kwargs)

    GetShell32Version = staticmethod(GetShell32Version)
    def IsDisplayAvailable(*args, **kwargs):
        """
        IsDisplayAvailable() -> bool

        Tests if it is possible to create a GUI in the current environment.
        This will mean different things on the different platforms.

           * On X Windows systems this function will return ``False`` if it is
             not able to open a connection to the X server, which can happen
             if $DISPLAY is not set, or is not set correctly.

           * On Mac OS X a ``False`` return value will mean that wx is not
             able to access the window manager, which can happen if logged in
             remotely or if running from the normal version of python instead
             of the framework version, (i.e., pythonw.)

           * On MS Windows...

        """
        return __core.PyApp_IsDisplayAvailable(*args, **kwargs)

    IsDisplayAvailable = staticmethod(IsDisplayAvailable)
    AppName = property(GetAppName,SetAppName,doc="See `GetAppName` and `SetAppName`") 
    AssertMode = property(GetAssertMode,SetAssertMode,doc="See `GetAssertMode` and `SetAssertMode`") 
    ClassName = property(GetClassName,SetClassName,doc="See `GetClassName` and `SetClassName`") 
    ExitOnFrameDelete = property(GetExitOnFrameDelete,SetExitOnFrameDelete,doc="See `GetExitOnFrameDelete` and `SetExitOnFrameDelete`") 
    LayoutDirection = property(GetLayoutDirection,doc="See `GetLayoutDirection`") 
    PrintMode = property(GetPrintMode,SetPrintMode,doc="See `GetPrintMode` and `SetPrintMode`") 
    TopWindow = property(GetTopWindow,SetTopWindow,doc="See `GetTopWindow` and `SetTopWindow`") 
    Traits = property(GetTraits,doc="See `GetTraits`") 
    UseBestVisual = property(GetUseBestVisual,SetUseBestVisual,doc="See `GetUseBestVisual` and `SetUseBestVisual`") 
    VendorName = property(GetVendorName,SetVendorName,doc="See `GetVendorName` and `SetVendorName`") 
    Active = property(IsActive) 
    AppDisplayName = property(GetAppDisplayName,SetAppDisplayName) 
    VendorDisplayName = property(GetVendorDisplayName,SetVendorDisplayName) 
__core.PyApp_swigregister(PyApp)

def PyApp_GetTraitsIfExists(*args):
  """
    PyApp_GetTraitsIfExists() -> wxAppTraits

    This function provides safer access to traits object than
    wx.GetApp().GetTraits() during startup or termination when the global
    application object itself may be unavailable.
    """
  return __core.PyApp_GetTraitsIfExists(*args)

def PyApp_IsMainLoopRunning(*args):
  """
    PyApp_IsMainLoopRunning() -> bool

    Returns True if we're running the main loop, i.e. if the events can
    currently be dispatched.
    """
  return __core.PyApp_IsMainLoopRunning(*args)

def PyApp_GetMacSupportPCMenuShortcuts(*args):
  """PyApp_GetMacSupportPCMenuShortcuts() -> bool"""
  return __core.PyApp_GetMacSupportPCMenuShortcuts(*args)

def PyApp_GetMacAboutMenuItemId(*args):
  """PyApp_GetMacAboutMenuItemId() -> long"""
  return __core.PyApp_GetMacAboutMenuItemId(*args)

def PyApp_GetMacPreferencesMenuItemId(*args):
  """PyApp_GetMacPreferencesMenuItemId() -> long"""
  return __core.PyApp_GetMacPreferencesMenuItemId(*args)

def PyApp_GetMacExitMenuItemId(*args):
  """PyApp_GetMacExitMenuItemId() -> long"""
  return __core.PyApp_GetMacExitMenuItemId(*args)

def PyApp_GetMacHelpMenuTitleName(*args):
  """PyApp_GetMacHelpMenuTitleName() -> String"""
  return __core.PyApp_GetMacHelpMenuTitleName(*args)

def PyApp_SetMacSupportPCMenuShortcuts(*args, **kwargs):
  """PyApp_SetMacSupportPCMenuShortcuts(bool val)"""
  return __core.PyApp_SetMacSupportPCMenuShortcuts(*args, **kwargs)

def PyApp_SetMacAboutMenuItemId(*args, **kwargs):
  """PyApp_SetMacAboutMenuItemId(long val)"""
  return __core.PyApp_SetMacAboutMenuItemId(*args, **kwargs)

def PyApp_SetMacPreferencesMenuItemId(*args, **kwargs):
  """PyApp_SetMacPreferencesMenuItemId(long val)"""
  return __core.PyApp_SetMacPreferencesMenuItemId(*args, **kwargs)

def PyApp_SetMacExitMenuItemId(*args, **kwargs):
  """PyApp_SetMacExitMenuItemId(long val)"""
  return __core.PyApp_SetMacExitMenuItemId(*args, **kwargs)

def PyApp_SetMacHelpMenuTitleName(*args, **kwargs):
  """PyApp_SetMacHelpMenuTitleName(String val)"""
  return __core.PyApp_SetMacHelpMenuTitleName(*args, **kwargs)

def PyApp_GetComCtl32Version(*args):
  """
    PyApp_GetComCtl32Version() -> int

    Returns 400, 470, 471, etc. for comctl32.dll 4.00, 4.70, 4.71 or 0 if
    it wasn't found at all.  Raises an exception on non-Windows platforms.
    """
  return __core.PyApp_GetComCtl32Version(*args)

def PyApp_GetShell32Version(*args):
  """
    PyApp_GetShell32Version() -> int

    Returns 400, 470, 471, etc. for shell32.dll 4.00, 4.70, 4.71 or 0 if
    it wasn't found at all.  Raises an exception on non-Windows platforms.
    """
  return __core.PyApp_GetShell32Version(*args)

def PyApp_IsDisplayAvailable(*args):
  """
    PyApp_IsDisplayAvailable() -> bool

    Tests if it is possible to create a GUI in the current environment.
    This will mean different things on the different platforms.

       * On X Windows systems this function will return ``False`` if it is
         not able to open a connection to the X server, which can happen
         if $DISPLAY is not set, or is not set correctly.

       * On Mac OS X a ``False`` return value will mean that wx is not
         able to access the window manager, which can happen if logged in
         remotely or if running from the normal version of python instead
         of the framework version, (i.e., pythonw.)

       * On MS Windows...

    """
  return __core.PyApp_IsDisplayAvailable(*args)

#---------------------------------------------------------------------------


def Exit(*args):
  """
    Exit()

    Force an exit of the application.  Convenience for wx.GetApp().Exit()
    """
  return __core.Exit(*args)

def Yield(*args):
  """
    Yield() -> bool

    Yield to other apps/messages.  Convenience for wx.GetApp().Yield()
    """
  return __core.Yield(*args)

def YieldIfNeeded(*args):
  """
    YieldIfNeeded() -> bool

    Yield to other apps/messages.  Convenience for wx.GetApp().Yield(True)
    """
  return __core.YieldIfNeeded(*args)

def SafeYield(*args, **kwargs):
  """
    SafeYield(Window win=None, bool onlyIfNeeded=False) -> bool

    This function is similar to `wx.Yield`, except that it disables the
    user input to all program windows before calling `wx.Yield` and
    re-enables it again afterwards. If ``win`` is not None, this window
    will remain enabled, allowing the implementation of some limited user
    interaction.

    :Returns: the result of the call to `wx.Yield`.
    """
  return __core.SafeYield(*args, **kwargs)

def WakeUpIdle(*args):
  """
    WakeUpIdle()

    Cause the message queue to become empty again, so idle events will be
    sent.
    """
  return __core.WakeUpIdle(*args)

def PostEvent(*args, **kwargs):
  """
    PostEvent(EvtHandler dest, Event event)

    Send an event to a window or other wx.EvtHandler to be processed
    later.
    """
  return __core.PostEvent(*args, **kwargs)

def App_CleanUp(*args):
  """
    App_CleanUp()

    For internal use only, it is used to cleanup after wxWidgets when
    Python shuts down.
    """
  return __core.App_CleanUp(*args)

def GetApp(*args):
  """
    GetApp() -> PyApp

    Return a reference to the current wx.App object.
    """
  return __core.GetApp(*args)

def SetDefaultPyEncoding(*args, **kwargs):
  """
    SetDefaultPyEncoding(string encoding)

    Sets the encoding that wxPython will use when it needs to convert a
    Python string or unicode object to or from a wxString.

    The default encoding is the value of ``locale.getdefaultlocale()[1]``
    but please be aware that the default encoding within the same locale
    may be slightly different on different platforms.  For example, please
    see http://www.alanwood.net/demos/charsetdiffs.html for differences
    between the common latin/roman encodings.
    """
  return __core.SetDefaultPyEncoding(*args, **kwargs)

def GetDefaultPyEncoding(*args):
  """
    GetDefaultPyEncoding() -> string

    Gets the current encoding that wxPython will use when it needs to
    convert a Python string or unicode object to or from a wxString.
    """
  return __core.GetDefaultPyEncoding(*args)
#----------------------------------------------------------------------

class PyOnDemandOutputWindow:
    """
    A class that can be used for redirecting Python's stdout and
    stderr streams.  It will do nothing until something is wrriten to
    the stream at which point it will create a Frame with a text area
    and write the text there.
    """
    def __init__(self, title = "wxPython: stdout/stderr"):
        self.frame  = None
        self.title  = title
        self.pos    = wx.DefaultPosition
        self.size   = (450, 300)
        self.parent = None

    def SetParent(self, parent):
        """Set the window to be used as the popup Frame's parent."""
        self.parent = parent


    def CreateOutputWindow(self, st):
        self.frame = wx.Frame(self.parent, -1, self.title, self.pos, self.size,
                              style=wx.DEFAULT_FRAME_STYLE)
        self.text  = wx.TextCtrl(self.frame, -1, "",
                                 style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.text.AppendText(st)
        self.frame.Show(True)
        self.frame.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        

    def OnCloseWindow(self, event):
        if self.frame is not None:
            self.frame.Destroy()
        self.frame = None
        self.text  = None
        self.parent = None


    # These methods provide the file-like output behaviour.
    def write(self, text):
        """
        Create the output window if needed and write the string to it.
        If not called in the context of the gui thread then uses
        CallAfter to do the work there.
        """        
        if self.frame is None:
            if not wx.Thread_IsMain():
                wx.CallAfter(self.CreateOutputWindow, text)
            else:
                self.CreateOutputWindow(text)
        else:
            if not wx.Thread_IsMain():
                wx.CallAfter(self.text.AppendText, text)
            else:
                self.text.AppendText(text)


    def close(self):
        if self.frame is not None:
            wx.CallAfter(self.frame.Close)


    def flush(self):
        pass
    


#----------------------------------------------------------------------

class App(wx.PyApp):
    """
    The ``wx.App`` class represents the application and is used to:

      * bootstrap the wxPython system and initialize the underlying
        gui toolkit
      * set and get application-wide properties
      * implement the windowing system main message or event loop,
        and to dispatch events to window instances
      * etc.

    Every application must have a ``wx.App`` instance, and all
    creation of UI objects should be delayed until after the
    ``wx.App`` object has been created in order to ensure that the gui
    platform and wxWidgets have been fully initialized.

    Normally you would derive from this class and implement an
    ``OnInit`` method that creates a frame and then calls
    ``self.SetTopWindow(frame)``.
    """
    
    outputWindowClass = PyOnDemandOutputWindow

    def __init__(self,
                 redirect=False,
                 filename=None,
                 useBestVisual=False,
                 clearSigInt=True):
        """
        Construct a ``wx.App`` object.  

        :param redirect: Should ``sys.stdout`` and ``sys.stderr`` be
            redirected?  Defaults to False. If ``filename`` is None
            then output will be redirected to a window that pops up
            as needed.  (You can control what kind of window is created
            for the output by resetting the class variable
            ``outputWindowClass`` to a class of your choosing.)

        :param filename: The name of a file to redirect output to, if
            redirect is True.

        :param useBestVisual: Should the app try to use the best
            available visual provided by the system (only relevant on
            systems that have more than one visual.)  This parameter
            must be used instead of calling `SetUseBestVisual` later
            on because it must be set before the underlying GUI
            toolkit is initialized.

        :param clearSigInt: Should SIGINT be cleared?  This allows the
            app to terminate upon a Ctrl-C in the console like other
            GUI apps will.

        :note: You should override OnInit to do applicaition
            initialization to ensure that the system, toolkit and
            wxWidgets are fully initialized.
        """
        
        wx.PyApp.__init__(self)

        # make sure we can create a GUI
        if not self.IsDisplayAvailable():
            
            if wx.Platform == "__WXMAC__":
                msg = """This program needs access to the screen.
Please run with a Framework build of python, and only when you are
logged in on the main display of your Mac."""
                
            elif wx.Platform == "__WXGTK__":
                msg ="Unable to access the X Display, is $DISPLAY set properly?"

            else:
                msg = "Unable to create GUI"
                # TODO: more description is needed for wxMSW...

            raise SystemExit(msg)
        
        # This has to be done before OnInit
        self.SetUseBestVisual(useBestVisual)

        # Set the default handler for SIGINT.  This fixes a problem
        # where if Ctrl-C is pressed in the console that started this
        # app then it will not appear to do anything, (not even send
        # KeyboardInterrupt???)  but will later segfault on exit.  By
        # setting the default handler then the app will exit, as
        # expected (depending on platform.)
        if clearSigInt:
            try:
                import signal
                signal.signal(signal.SIGINT, signal.SIG_DFL)
            except:
                pass

        # Save and redirect the stdio to a window?
        self.stdioWin = None
        self.saveStdio = (_sys.stdout, _sys.stderr)
        if redirect:
            self.RedirectStdio(filename)

        # Use Python's install prefix as the default  
        wx.StandardPaths.Get().SetInstallPrefix(_sys.prefix)

        # Until the new native control for wxMac is up to par, still use the generic one.
        wx.SystemOptions.SetOptionInt("mac.listctrl.always_use_generic", 1)

        # This finishes the initialization of wxWindows and then calls
        # the OnInit that should be present in the derived class
        self._BootstrapApp()


    def OnPreInit(self):
        """
        Things that must be done after _BootstrapApp has done its
        thing, but would be nice if they were already done by the time
        that OnInit is called.
        """
        wx.StockGDI._initStockObjects()
        

    def __del__(self, destroy=wx.PyApp.__del__):
        self.RestoreStdio()  # Just in case the MainLoop was overridden
        destroy(self)

    def Destroy(self):
        self.this.own(False)
        wx.PyApp.Destroy(self)

    def SetTopWindow(self, frame):
        """Set the \"main\" top level window"""
        if self.stdioWin:
            self.stdioWin.SetParent(frame)
        wx.PyApp.SetTopWindow(self, frame)


    def MainLoop(self):
        """Execute the main GUI event loop"""
        wx.PyApp.MainLoop(self)
        self.RestoreStdio()


    def RedirectStdio(self, filename=None):
        """Redirect sys.stdout and sys.stderr to a file or a popup window."""
        if filename:
            _sys.stdout = _sys.stderr = open(filename, 'a')
        else:
            self.stdioWin = self.outputWindowClass()
            _sys.stdout = _sys.stderr = self.stdioWin


    def RestoreStdio(self):
        try:
            _sys.stdout, _sys.stderr = self.saveStdio
        except:
            pass


    def SetOutputWindowAttributes(self, title=None, pos=None, size=None):
        """
        Set the title, position and/or size of the output window if
        the stdio has been redirected.  This should be called before
        any output would cause the output window to be created.
        """
        if self.stdioWin:
            if title is not None:
                self.stdioWin.title = title
            if pos is not None:
                self.stdioWin.pos = pos
            if size is not None:
                self.stdioWin.size = size
            

    @staticmethod
    def Get():
        return wx.GetApp()

# change from wx.PyApp_XX to wx.App_XX
App_GetMacSupportPCMenuShortcuts = _core_.PyApp_GetMacSupportPCMenuShortcuts
App_GetMacAboutMenuItemId        = _core_.PyApp_GetMacAboutMenuItemId
App_GetMacPreferencesMenuItemId  = _core_.PyApp_GetMacPreferencesMenuItemId
App_GetMacExitMenuItemId         = _core_.PyApp_GetMacExitMenuItemId
App_GetMacHelpMenuTitleName      = _core_.PyApp_GetMacHelpMenuTitleName
App_SetMacSupportPCMenuShortcuts = _core_.PyApp_SetMacSupportPCMenuShortcuts
App_SetMacAboutMenuItemId        = _core_.PyApp_SetMacAboutMenuItemId
App_SetMacPreferencesMenuItemId  = _core_.PyApp_SetMacPreferencesMenuItemId
App_SetMacExitMenuItemId         = _core_.PyApp_SetMacExitMenuItemId
App_SetMacHelpMenuTitleName      = _core_.PyApp_SetMacHelpMenuTitleName
App_GetComCtl32Version           = _core_.PyApp_GetComCtl32Version

#----------------------------------------------------------------------------

@wx.deprecated
class PySimpleApp(wx.App):
    """
    A simple application class.  You can just create one of these and
    then then make your top level windows later, and not have to worry
    about OnInit.  For example::

        app = wx.PySimpleApp()
        frame = wx.Frame(None, title='Hello World')
        frame.Show()
        app.MainLoop()

    :see: `wx.App` 
    """

    def __init__(self, redirect=False, filename=None,
                 useBestVisual=False, clearSigInt=True):
        """
        :see: `wx.App.__init__`
        """
        wx.App.__init__(self, redirect, filename, useBestVisual, clearSigInt)
        
    def OnInit(self):
        return True



# Is anybody using this one?
class PyWidgetTester(wx.App):
    def __init__(self, size = (250, 100)):
        self.size = size
        wx.App.__init__(self, 0)

    def OnInit(self):
        self.frame = wx.Frame(None, -1, "Widget Tester", pos=(0,0), size=self.size)
        self.SetTopWindow(self.frame)
        return True

    def SetWidget(self, widgetClass, *args, **kwargs):
        w = widgetClass(self.frame, *args, **kwargs)
        self.frame.Show(True)

#----------------------------------------------------------------------------
# Make sure that system resources allocated by wx are properly cleaned
# up when the Python interpreter exits.
        
import atexit
atexit.register(_core_.App_CleanUp)
del atexit

#----------------------------------------------------------------------------

#---------------------------------------------------------------------------

class EventLoopBase(object):
    """Proxy of C++ EventLoopBase class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_EventLoopBase
    __del__ = lambda self : None;
    def IsOk(*args, **kwargs):
        """IsOk(self) -> bool"""
        return __core.EventLoopBase_IsOk(*args, **kwargs)

    def IsMain(*args, **kwargs):
        """IsMain(self) -> bool"""
        return __core.EventLoopBase_IsMain(*args, **kwargs)

    def Run(*args, **kwargs):
        """Run(self) -> int"""
        return __core.EventLoopBase_Run(*args, **kwargs)

    def IsRunning(*args, **kwargs):
        """IsRunning(self) -> bool"""
        return __core.EventLoopBase_IsRunning(*args, **kwargs)

    def Exit(*args, **kwargs):
        """Exit(self, int rc=0)"""
        return __core.EventLoopBase_Exit(*args, **kwargs)

    def Pending(*args, **kwargs):
        """Pending(self) -> bool"""
        return __core.EventLoopBase_Pending(*args, **kwargs)

    def Dispatch(*args, **kwargs):
        """Dispatch(self) -> bool"""
        return __core.EventLoopBase_Dispatch(*args, **kwargs)

    def DispatchTimeout(*args, **kwargs):
        """DispatchTimeout(self, unsigned long timeout) -> int"""
        return __core.EventLoopBase_DispatchTimeout(*args, **kwargs)

    def WakeUp(*args, **kwargs):
        """WakeUp(self)"""
        return __core.EventLoopBase_WakeUp(*args, **kwargs)

    def WakeUpIdle(*args, **kwargs):
        """WakeUpIdle(self)"""
        return __core.EventLoopBase_WakeUpIdle(*args, **kwargs)

    def ProcessIdle(*args, **kwargs):
        """ProcessIdle(self) -> bool"""
        return __core.EventLoopBase_ProcessIdle(*args, **kwargs)

    def Yield(*args, **kwargs):
        """Yield(self, bool onlyIfNeeded=False) -> bool"""
        return __core.EventLoopBase_Yield(*args, **kwargs)

    def YieldFor(*args, **kwargs):
        """YieldFor(self, long eventsToProcess) -> bool"""
        return __core.EventLoopBase_YieldFor(*args, **kwargs)

    def IsYielding(*args, **kwargs):
        """IsYielding(self) -> bool"""
        return __core.EventLoopBase_IsYielding(*args, **kwargs)

    def IsEventAllowedInsideYield(*args, **kwargs):
        """IsEventAllowedInsideYield(self, int cat) -> bool"""
        return __core.EventLoopBase_IsEventAllowedInsideYield(*args, **kwargs)

    def GetActive(*args, **kwargs):
        """GetActive() -> EventLoopBase"""
        return __core.EventLoopBase_GetActive(*args, **kwargs)

    GetActive = staticmethod(GetActive)
    def SetActive(*args, **kwargs):
        """SetActive(EventLoopBase loop)"""
        return __core.EventLoopBase_SetActive(*args, **kwargs)

    SetActive = staticmethod(SetActive)
__core.EventLoopBase_swigregister(EventLoopBase)

def EventLoopBase_GetActive(*args):
  """EventLoopBase_GetActive() -> EventLoopBase"""
  return __core.EventLoopBase_GetActive(*args)

def EventLoopBase_SetActive(*args, **kwargs):
  """EventLoopBase_SetActive(EventLoopBase loop)"""
  return __core.EventLoopBase_SetActive(*args, **kwargs)

class GUIEventLoop(EventLoopBase):
    """Proxy of C++ GUIEventLoop class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> GUIEventLoop"""
        this = __core.new_GUIEventLoop(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.GUIEventLoop_swigregister(GUIEventLoop)

class EventLoop(GUIEventLoop):
    """Class using the old name for compatibility."""
    pass

class ModalEventLoop(GUIEventLoop):
    """Proxy of C++ ModalEventLoop class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, Window winModal) -> ModalEventLoop"""
        this = __core.new_ModalEventLoop(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.ModalEventLoop_swigregister(ModalEventLoop)

class EventLoopActivator(object):
    """Proxy of C++ EventLoopActivator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, EventLoopBase evtLoop) -> EventLoopActivator"""
        this = __core.new_EventLoopActivator(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_EventLoopActivator
    __del__ = lambda self : None;
__core.EventLoopActivator_swigregister(EventLoopActivator)

#---------------------------------------------------------------------------

ACCEL_ALT = __core.ACCEL_ALT
ACCEL_CTRL = __core.ACCEL_CTRL
ACCEL_SHIFT = __core.ACCEL_SHIFT
ACCEL_NORMAL = __core.ACCEL_NORMAL
ACCEL_RAW_CTRL = __core.ACCEL_RAW_CTRL
ACCEL_CMD = __core.ACCEL_CMD
class AcceleratorEntry(object):
    """
    A class used to define items in an `wx.AcceleratorTable`.  wxPython
    programs can choose to use wx.AcceleratorEntry objects, but using a
    list of 3-tuple of integers (flags, keyCode, cmdID) usually works just
    as well.  See `__init__` for  of the tuple values.

    :see: `wx.AcceleratorTable`
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int flags=0, int keyCode=0, int cmdID=0) -> AcceleratorEntry

        Construct a wx.AcceleratorEntry.
        """
        this = __core.new_AcceleratorEntry(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_AcceleratorEntry
    __del__ = lambda self : None;
    def Set(*args, **kwargs):
        """
        Set(self, int flags, int keyCode, int cmd)

        (Re)set the attributes of a wx.AcceleratorEntry.
        :see `__init__`
        """
        return __core.AcceleratorEntry_Set(*args, **kwargs)

    def Create(*args, **kwargs):
        """
        Create(String str) -> AcceleratorEntry

        Create accelerator corresponding to the specified string, or None if
        it coulnd't be parsed.
        """
        return __core.AcceleratorEntry_Create(*args, **kwargs)

    Create = staticmethod(Create)
    def GetFlags(*args, **kwargs):
        """
        GetFlags(self) -> int

        Get the AcceleratorEntry's flags.
        """
        return __core.AcceleratorEntry_GetFlags(*args, **kwargs)

    def GetKeyCode(*args, **kwargs):
        """
        GetKeyCode(self) -> int

        Get the AcceleratorEntry's keycode.
        """
        return __core.AcceleratorEntry_GetKeyCode(*args, **kwargs)

    def GetCommand(*args, **kwargs):
        """
        GetCommand(self) -> int

        Get the AcceleratorEntry's command ID.
        """
        return __core.AcceleratorEntry_GetCommand(*args, **kwargs)

    def IsOk(*args, **kwargs):
        """IsOk(self) -> bool"""
        return __core.AcceleratorEntry_IsOk(*args, **kwargs)

    def ToString(*args, **kwargs):
        """
        ToString(self) -> String

        Returns a string representation for the this accelerator.  The string
        is formatted using the <flags>-<keycode> format where <flags> maybe a
        hyphen-separed list of "shift|alt|ctrl"

        """
        return __core.AcceleratorEntry_ToString(*args, **kwargs)

    def FromString(*args, **kwargs):
        """
        FromString(self, String str) -> bool

        Returns true if the given string correctly initialized this object.
        """
        return __core.AcceleratorEntry_FromString(*args, **kwargs)

    Command = property(GetCommand,doc="See `GetCommand`") 
    Flags = property(GetFlags,doc="See `GetFlags`") 
    KeyCode = property(GetKeyCode,doc="See `GetKeyCode`") 
__core.AcceleratorEntry_swigregister(AcceleratorEntry)

def AcceleratorEntry_Create(*args, **kwargs):
  """
    AcceleratorEntry_Create(String str) -> AcceleratorEntry

    Create accelerator corresponding to the specified string, or None if
    it coulnd't be parsed.
    """
  return __core.AcceleratorEntry_Create(*args, **kwargs)

class AcceleratorTable(Object):
    """
    An accelerator table allows the application to specify a table of
    keyboard shortcuts for menus or other commands. On Windows, menu or
    button commands are supported; on GTK, only menu commands are
    supported.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(entries) -> AcceleratorTable

        Construct an AcceleratorTable from a list of `wx.AcceleratorEntry`
        items or or of 3-tuples (flags, keyCode, cmdID)

        :see: `wx.AcceleratorEntry`
        """
        this = __core.new_AcceleratorTable(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_AcceleratorTable
    __del__ = lambda self : None;
    def IsOk(*args, **kwargs):
        """IsOk(self) -> bool"""
        return __core.AcceleratorTable_IsOk(*args, **kwargs)

    Ok = IsOk 
__core.AcceleratorTable_swigregister(AcceleratorTable)

def GetAccelFromString(label):
    entry = AcceleratorEntry()
    if '\t' in label:
        entry.FromString(label)
    return entry

#---------------------------------------------------------------------------

class WindowList_iterator(object):
    """This class serves as an iterator for a wxWindowList object."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_WindowList_iterator
    __del__ = lambda self : None;
    def next(*args, **kwargs):
        """next(self) -> Window"""
        return __core.WindowList_iterator_next(*args, **kwargs)

__core.WindowList_iterator_swigregister(WindowList_iterator)
NullAcceleratorTable = cvar.NullAcceleratorTable
PanelNameStr = cvar.PanelNameStr

class WindowList(object):
    """
    This class wraps a wxList-based class and gives it a Python
    sequence-like interface.  Sequence operations supported are length,
    index access and iteration.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_WindowList
    __del__ = lambda self : None;
    def __len__(*args, **kwargs):
        """__len__(self) -> size_t"""
        return __core.WindowList___len__(*args, **kwargs)

    def __getitem__(*args, **kwargs):
        """__getitem__(self, size_t index) -> Window"""
        return __core.WindowList___getitem__(*args, **kwargs)

    def __contains__(*args, **kwargs):
        """__contains__(self, Window obj) -> bool"""
        return __core.WindowList___contains__(*args, **kwargs)

    def __iter__(*args, **kwargs):
        """__iter__(self) -> WindowList_iterator"""
        return __core.WindowList___iter__(*args, **kwargs)

    def index(*args, **kwargs):
        """index(self, Window obj) -> int"""
        return __core.WindowList_index(*args, **kwargs)

    def __repr__(self):
        return "wxWindowList: " + repr(list(self))

__core.WindowList_swigregister(WindowList)

class VisualAttributes(object):
    """struct containing all the visual attributes of a control"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> VisualAttributes

        struct containing all the visual attributes of a control
        """
        this = __core.new_VisualAttributes(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_VisualAttributes
    __del__ = lambda self : None;
    def _get_font(*args, **kwargs):
        """_get_font(self) -> Font"""
        return __core.VisualAttributes__get_font(*args, **kwargs)

    def _get_colFg(*args, **kwargs):
        """_get_colFg(self) -> Colour"""
        return __core.VisualAttributes__get_colFg(*args, **kwargs)

    def _get_colBg(*args, **kwargs):
        """_get_colBg(self) -> Colour"""
        return __core.VisualAttributes__get_colBg(*args, **kwargs)

    font = property(_get_font) 
    colFg = property(_get_colFg) 
    colBg = property(_get_colBg) 
__core.VisualAttributes_swigregister(VisualAttributes)

WINDOW_VARIANT_NORMAL = __core.WINDOW_VARIANT_NORMAL
WINDOW_VARIANT_SMALL = __core.WINDOW_VARIANT_SMALL
WINDOW_VARIANT_MINI = __core.WINDOW_VARIANT_MINI
WINDOW_VARIANT_LARGE = __core.WINDOW_VARIANT_LARGE
WINDOW_VARIANT_MAX = __core.WINDOW_VARIANT_MAX
SHOW_EFFECT_NONE = __core.SHOW_EFFECT_NONE
SHOW_EFFECT_ROLL_TO_LEFT = __core.SHOW_EFFECT_ROLL_TO_LEFT
SHOW_EFFECT_ROLL_TO_RIGHT = __core.SHOW_EFFECT_ROLL_TO_RIGHT
SHOW_EFFECT_ROLL_TO_TOP = __core.SHOW_EFFECT_ROLL_TO_TOP
SHOW_EFFECT_ROLL_TO_BOTTOM = __core.SHOW_EFFECT_ROLL_TO_BOTTOM
SHOW_EFFECT_SLIDE_TO_LEFT = __core.SHOW_EFFECT_SLIDE_TO_LEFT
SHOW_EFFECT_SLIDE_TO_RIGHT = __core.SHOW_EFFECT_SLIDE_TO_RIGHT
SHOW_EFFECT_SLIDE_TO_TOP = __core.SHOW_EFFECT_SLIDE_TO_TOP
SHOW_EFFECT_SLIDE_TO_BOTTOM = __core.SHOW_EFFECT_SLIDE_TO_BOTTOM
SHOW_EFFECT_BLEND = __core.SHOW_EFFECT_BLEND
SHOW_EFFECT_EXPAND = __core.SHOW_EFFECT_EXPAND
SHOW_EFFECT_MAX = __core.SHOW_EFFECT_MAX
SEND_EVENT_POST = __core.SEND_EVENT_POST
class Window(EvtHandler):
    """
    wx.Window is the base class for all windows and represents any visible
    object on the screen. All controls, top level windows and so on are
    wx.Windows. Sizers and device contexts are not however, as they don't
    appear on screen themselves.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=0, String name=PanelNameStr) -> Window

        Construct and show a generic Window.
        """
        this = __core.new_Window(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=0, String name=PanelNameStr) -> bool

        Create the GUI part of the Window for 2-phase creation mode.
        """
        return __core.Window_Create(*args, **kwargs)

    def Close(*args, **kwargs):
        """
        Close(self, bool force=False) -> bool

        This function simply generates a EVT_CLOSE event whose handler usually
        tries to close the window. It doesn't close the window itself,
        however.  If force is False (the default) then the window's close
        handler will be allowed to veto the destruction of the window.
        """
        return __core.Window_Close(*args, **kwargs)

    def Destroy(*args, **kwargs):
        """
        Destroy(self) -> bool

        Destroys the window safely.  Frames and dialogs are not destroyed
        immediately when this function is called -- they are added to a list
        of windows to be deleted on idle time, when all the window's events
        have been processed. This prevents problems with events being sent to
        non-existent windows.

        Returns True if the window has either been successfully deleted, or it
        has been added to the list of windows pending real deletion.
        """
        args[0].this.own(False)
        return __core.Window_Destroy(*args, **kwargs)

    def DestroyChildren(*args, **kwargs):
        """
        DestroyChildren(self) -> bool

        Destroys all children of a window. Called automatically by the
        destructor.
        """
        return __core.Window_DestroyChildren(*args, **kwargs)

    def IsBeingDeleted(*args, **kwargs):
        """
        IsBeingDeleted(self) -> bool

        Is the window in the process of being deleted?
        """
        return __core.Window_IsBeingDeleted(*args, **kwargs)

    def SetLabel(*args, **kwargs):
        """
        SetLabel(self, String label)

        Set the text which the window shows in its label if applicable.
        """
        return __core.Window_SetLabel(*args, **kwargs)

    def GetLabel(*args, **kwargs):
        """
        GetLabel(self) -> String

        Generic way of getting a label from any window, for identification
        purposes.  The interpretation of this function differs from class to
        class. For frames and dialogs, the value returned is the title. For
        buttons or static text controls, it is the button text. This function
        can be useful for meta-programs such as testing tools or special-needs
        access programs)which need to identify windows by name.
        """
        return __core.Window_GetLabel(*args, **kwargs)

    def SetName(*args, **kwargs):
        """
        SetName(self, String name)

        Sets the window's name.  The window name is used for ressource setting
        in X, it is not the same as the window title/label
        """
        return __core.Window_SetName(*args, **kwargs)

    def GetName(*args, **kwargs):
        """
        GetName(self) -> String

        Returns the windows name.  This name is not guaranteed to be unique;
        it is up to the programmer to supply an appropriate name in the window
        constructor or via wx.Window.SetName.
        """
        return __core.Window_GetName(*args, **kwargs)

    def SetWindowVariant(*args, **kwargs):
        """
        SetWindowVariant(self, int variant)

        Sets the variant of the window/font size to use for this window, if
        the platform supports variants, for example, wxMac.
        """
        return __core.Window_SetWindowVariant(*args, **kwargs)

    def GetWindowVariant(*args, **kwargs):
        """GetWindowVariant(self) -> int"""
        return __core.Window_GetWindowVariant(*args, **kwargs)

    def SetId(*args, **kwargs):
        """
        SetId(self, int winid)

        Sets the identifier of the window.  Each window has an integer
        identifier. If the application has not provided one, an identifier
        will be generated. Normally, the identifier should be provided on
        creation and should not be modified subsequently.
        """
        return __core.Window_SetId(*args, **kwargs)

    def GetId(*args, **kwargs):
        """
        GetId(self) -> int

        Returns the identifier of the window.  Each window has an integer
        identifier. If the application has not provided one (or the default Id
        -1 is used) then an unique identifier with a negative value will be
        generated.
        """
        return __core.Window_GetId(*args, **kwargs)

    def NewControlId(*args, **kwargs):
        """
        NewControlId(int count=1) -> int

        Generate a unique id (or count of them consecutively), returns a
        valid id in the auto-id range or wxID_NONE if failed.  If using
        autoid management, it will mark the id as reserved until it is
        used (by assigning it to a wxWindowIDRef) or unreserved.
        """
        return __core.Window_NewControlId(*args, **kwargs)

    NewControlId = staticmethod(NewControlId)
    def UnreserveControlId(*args, **kwargs):
        """
        UnreserveControlId(int id, int count=1)

        If an ID generated from NewControlId is not assigned to a wxWindowIDRef,
        it must be unreserved.
        """
        return __core.Window_UnreserveControlId(*args, **kwargs)

    UnreserveControlId = staticmethod(UnreserveControlId)
    def ReleaseControlId(id):
        UnreserveControlId(id)
    ReleaseControlId = staticmethod(ReleaseControlId)    

    def GetLayoutDirection(*args, **kwargs):
        """
        GetLayoutDirection(self) -> int

        Get the layout direction (LTR or RTL) for this window.  Returns
        ``wx.Layout_Default`` if layout direction is not supported.
        """
        return __core.Window_GetLayoutDirection(*args, **kwargs)

    def SetLayoutDirection(*args, **kwargs):
        """
        SetLayoutDirection(self, int dir)

        Set the layout direction (LTR or RTL) for this window.
        """
        return __core.Window_SetLayoutDirection(*args, **kwargs)

    def AdjustForLayoutDirection(*args, **kwargs):
        """
        AdjustForLayoutDirection(self, int x, int width, int widthTotal) -> int

        Mirror coordinates for RTL layout if this window uses it and if the
        mirroring is not done automatically like Win32.
        """
        return __core.Window_AdjustForLayoutDirection(*args, **kwargs)

    def SetSize(*args, **kwargs):
        """
        SetSize(self, Size size)

        Sets the size of the window in pixels.
        """
        return __core.Window_SetSize(*args, **kwargs)

    def SetDimensions(*args, **kwargs):
        """
        SetDimensions(self, int x, int y, int width, int height, int sizeFlags=SIZE_AUTO)

        Sets the position and size of the window in pixels.  The sizeFlags
        parameter indicates the interpretation of the other params if they are
        equal to -1.

            ========================  ======================================
            wx.SIZE_AUTO              A -1 indicates that a class-specific
                                      default should be used.
            wx.SIZE_USE_EXISTING      Existing dimensions should be used if
                                      -1 values are supplied.
            wxSIZE_ALLOW_MINUS_ONE    Allow dimensions of -1 and less to be
                                      interpreted as real dimensions, not
                                      default values.
            ========================  ======================================

        """
        return __core.Window_SetDimensions(*args, **kwargs)

    def SetRect(*args, **kwargs):
        """
        SetRect(self, Rect rect, int sizeFlags=SIZE_AUTO)

        Sets the position and size of the window in pixels using a wx.Rect.
        """
        return __core.Window_SetRect(*args, **kwargs)

    def SetSizeWH(*args, **kwargs):
        """
        SetSizeWH(self, int width, int height)

        Sets the size of the window in pixels.
        """
        return __core.Window_SetSizeWH(*args, **kwargs)

    def Move(*args, **kwargs):
        """
        Move(self, Point pt, int flags=SIZE_USE_EXISTING)

        Moves the window to the given position.
        """
        return __core.Window_Move(*args, **kwargs)

    SetPosition = Move 
    def MoveXY(*args, **kwargs):
        """
        MoveXY(self, int x, int y, int flags=SIZE_USE_EXISTING)

        Moves the window to the given position.
        """
        return __core.Window_MoveXY(*args, **kwargs)

    def SetInitialSize(*args, **kwargs):
        """
        SetInitialSize(self, Size size=DefaultSize)

        A 'Smart' SetSize that will fill in default size components with the
        window's *best size* values.  Also set's the minsize for use with sizers.
        """
        return __core.Window_SetInitialSize(*args, **kwargs)

    SetBestFittingSize = wx.deprecated(SetInitialSize, 'Use `SetInitialSize`') 
    def Raise(*args, **kwargs):
        """
        Raise(self)

        Raises the window to the top of the window hierarchy.  In current
        version of wxWidgets this works both for managed and child windows.
        """
        return __core.Window_Raise(*args, **kwargs)

    def Lower(*args, **kwargs):
        """
        Lower(self)

        Lowers the window to the bottom of the window hierarchy.  In current
        version of wxWidgets this works both for managed and child windows.
        """
        return __core.Window_Lower(*args, **kwargs)

    def SetClientSize(*args, **kwargs):
        """
        SetClientSize(self, Size size)

        This sets the size of the window client area in pixels. Using this
        function to size a window tends to be more device-independent than
        wx.Window.SetSize, since the application need not worry about what
        dimensions the border or title bar have when trying to fit the window
        around panel items, for example.
        """
        return __core.Window_SetClientSize(*args, **kwargs)

    def SetClientSizeWH(*args, **kwargs):
        """
        SetClientSizeWH(self, int width, int height)

        This sets the size of the window client area in pixels. Using this
        function to size a window tends to be more device-independent than
        wx.Window.SetSize, since the application need not worry about what
        dimensions the border or title bar have when trying to fit the window
        around panel items, for example.
        """
        return __core.Window_SetClientSizeWH(*args, **kwargs)

    def SetClientRect(*args, **kwargs):
        """
        SetClientRect(self, Rect rect)

        This sets the size of the window client area in pixels. Using this
        function to size a window tends to be more device-independent than
        wx.Window.SetSize, since the application need not worry about what
        dimensions the border or title bar have when trying to fit the window
        around panel items, for example.
        """
        return __core.Window_SetClientRect(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> Point

        Get the window's position.  Notice that the position is in client
        coordinates for child windows and screen coordinates for the top level
        ones, use `GetScreenPosition` if you need screen coordinates for all
        kinds of windows.
        """
        return __core.Window_GetPosition(*args, **kwargs)

    def GetPositionTuple(*args, **kwargs):
        """
        GetPositionTuple() -> (x,y)

        Get the window's position.  Notice that the position is in client
        coordinates for child windows and screen coordinates for the top level
        ones, use `GetScreenPosition` if you need screen coordinates for all
        kinds of windows.
        """
        return __core.Window_GetPositionTuple(*args, **kwargs)

    def GetScreenPosition(*args, **kwargs):
        """
        GetScreenPosition(self) -> Point

        Get the position of the window in screen coordinantes.
        """
        return __core.Window_GetScreenPosition(*args, **kwargs)

    def GetScreenPositionTuple(*args, **kwargs):
        """
        GetScreenPositionTuple() -> (x,y)

        Get the position of the window in screen coordinantes.
        """
        return __core.Window_GetScreenPositionTuple(*args, **kwargs)

    def GetScreenRect(*args, **kwargs):
        """
        GetScreenRect(self) -> Rect

        Returns the size and position of the window in screen coordinantes as
        a `wx.Rect` object.
        """
        return __core.Window_GetScreenRect(*args, **kwargs)

    def GetSize(*args, **kwargs):
        """
        GetSize(self) -> Size

        Get the window size.
        """
        return __core.Window_GetSize(*args, **kwargs)

    def GetSizeTuple(*args, **kwargs):
        """
        GetSizeTuple() -> (width, height)

        Get the window size.
        """
        return __core.Window_GetSizeTuple(*args, **kwargs)

    def GetRect(*args, **kwargs):
        """
        GetRect(self) -> Rect

        Returns the size and position of the window as a `wx.Rect` object.
        """
        return __core.Window_GetRect(*args, **kwargs)

    def GetClientSize(*args, **kwargs):
        """
        GetClientSize(self) -> Size

        This gets the size of the window's 'client area' in pixels. The client
        area is the area which may be drawn on by the programmer, excluding
        title bar, border, scrollbars, etc.
        """
        return __core.Window_GetClientSize(*args, **kwargs)

    def GetClientSizeTuple(*args, **kwargs):
        """
        GetClientSizeTuple() -> (width, height)

        This gets the size of the window's 'client area' in pixels. The client
        area is the area which may be drawn on by the programmer, excluding
        title bar, border, scrollbars, etc.
        """
        return __core.Window_GetClientSizeTuple(*args, **kwargs)

    def GetClientAreaOrigin(*args, **kwargs):
        """
        GetClientAreaOrigin(self) -> Point

        Get the origin of the client area of the window relative to the
        window's top left corner (the client area may be shifted because of
        the borders, scrollbars, other decorations...)
        """
        return __core.Window_GetClientAreaOrigin(*args, **kwargs)

    def GetClientRect(*args, **kwargs):
        """
        GetClientRect(self) -> Rect

        Get the client area position and size as a `wx.Rect` object.
        """
        return __core.Window_GetClientRect(*args, **kwargs)

    def ClientToWindowSize(*args, **kwargs):
        """
        ClientToWindowSize(self, Size size) -> Size

        Converts client area size ``size to corresponding window size. In
        other words, the returned value is what `GetSize` would return if this
        window had client area of given size.  Components with
        ``wx.DefaultCoord`` (-1) value are left unchanged.

        Note that the conversion is not always exact, it assumes that
        non-client area doesn't change and so doesn't take into account things
        like menu bar (un)wrapping or (dis)appearance of the scrollbars.
        """
        return __core.Window_ClientToWindowSize(*args, **kwargs)

    def WindowToClientSize(*args, **kwargs):
        """
        WindowToClientSize(self, Size size) -> Size

        Converts window size ``size`` to corresponding client area size. In
        other words, the returned value is what `GetClientSize` would return
        if this window had given window size. Components with
        ``wxDefaultCoord`` (-1) value are left unchanged.

        Note that the conversion is not always exact, it assumes that
        non-client area doesn't change and so doesn't take into account things
        like menu bar (un)wrapping or (dis)appearance of the scrollbars.
        """
        return __core.Window_WindowToClientSize(*args, **kwargs)

    def GetBestSize(*args, **kwargs):
        """
        GetBestSize(self) -> Size

        This function returns the best acceptable minimal size for the
        window, if applicable. For example, for a static text control, it will
        be the minimal size such that the control label is not truncated. For
        windows containing subwindows (such as wx.Panel), the size returned by
        this function will be the same as the size the window would have had
        after calling Fit.
        """
        return __core.Window_GetBestSize(*args, **kwargs)

    def GetBestSizeTuple(*args, **kwargs):
        """
        GetBestSizeTuple() -> (width, height)

        This function returns the best acceptable minimal size for the
        window, if applicable. For example, for a static text control, it will
        be the minimal size such that the control label is not truncated. For
        windows containing subwindows (such as wx.Panel), the size returned by
        this function will be the same as the size the window would have had
        after calling Fit.
        """
        return __core.Window_GetBestSizeTuple(*args, **kwargs)

    def InvalidateBestSize(*args, **kwargs):
        """
        InvalidateBestSize(self)

        Reset the cached best size value so it will be recalculated the next
        time it is needed.
        """
        return __core.Window_InvalidateBestSize(*args, **kwargs)

    def CacheBestSize(*args, **kwargs):
        """
        CacheBestSize(self, Size size)

        Cache the best size so it doesn't need to be calculated again, (at least until
        some properties of the window change.)
        """
        return __core.Window_CacheBestSize(*args, **kwargs)

    def GetEffectiveMinSize(*args, **kwargs):
        """
        GetEffectiveMinSize(self) -> Size

        This function will merge the window's best size into the window's
        minimum size, giving priority to the min size components, and returns
        the results.

        """
        return __core.Window_GetEffectiveMinSize(*args, **kwargs)

    GetBestFittingSize = wx.deprecated(GetEffectiveMinSize, 'Use `GetEffectiveMinSize` instead.') 
    def GetAdjustedBestSize(self):
        s = self.GetBestSize()
        return wx.Size(max(s.width,  self.GetMinWidth()),
                       max(s.height, self.GetMinHeight()))
    GetAdjustedBestSize = wx.deprecated(GetAdjustedBestSize, 'Use `GetEffectiveMinSize` instead.')

    def Center(*args, **kwargs):
        """
        Center(self, int direction=BOTH)

        Centers the window.  The parameter specifies the direction for
        centering, and may be wx.HORIZONTAL, wx.VERTICAL or wx.BOTH. It may
        also include wx.CENTER_ON_SCREEN flag if you want to center the window
        on the entire screen and not on its parent window.  If it is a
        top-level window and has no parent then it will always be centered
        relative to the screen.
        """
        return __core.Window_Center(*args, **kwargs)

    Centre = Center 
    def CenterOnParent(*args, **kwargs):
        """
        CenterOnParent(self, int dir=BOTH)

        Center with respect to the the parent window
        """
        return __core.Window_CenterOnParent(*args, **kwargs)

    CentreOnParent = CenterOnParent 
    def Fit(*args, **kwargs):
        """
        Fit(self)

        Sizes the window so that it fits around its subwindows. This function
        won't do anything if there are no subwindows and will only really work
        correctly if sizers are used for the subwindows layout. Also, if the
        window has exactly one subwindow it is better (faster and the result
        is more precise as Fit adds some margin to account for fuzziness of
        its calculations) to call window.SetClientSize(child.GetSize())
        instead of calling Fit.
        """
        return __core.Window_Fit(*args, **kwargs)

    def FitInside(*args, **kwargs):
        """
        FitInside(self)

        Similar to Fit, but sizes the interior (virtual) size of a
        window. Mainly useful with scrolled windows to reset scrollbars after
        sizing changes that do not trigger a size event, and/or scrolled
        windows without an interior sizer. This function similarly won't do
        anything if there are no subwindows.
        """
        return __core.Window_FitInside(*args, **kwargs)

    def SetSizeHints(*args, **kwargs):
        """
        SetSizeHints(self, int minW, int minH, int maxW=-1, int maxH=-1, int incW=-1, 
            int incH=-1)

        Allows specification of minimum and maximum window sizes, and window
        size increments. If a pair of values is not set (or set to -1), the
        default values will be used.  If this function is called, the user
        will not be able to size the window outside the given bounds (if it is
        a top-level window.)  Sizers will also inspect the minimum window size
        and will use that value if set when calculating layout.

        The resizing increments are only significant under Motif or Xt.
        """
        return __core.Window_SetSizeHints(*args, **kwargs)

    def SetSizeHintsSz(*args, **kwargs):
        """
        SetSizeHintsSz(self, Size minSize, Size maxSize=DefaultSize, Size incSize=DefaultSize)

        Allows specification of minimum and maximum window sizes, and window
        size increments. If a pair of values is not set (or set to -1), the
        default values will be used.  If this function is called, the user
        will not be able to size the window outside the given bounds (if it is
        a top-level window.)  Sizers will also inspect the minimum window size
        and will use that value if set when calculating layout.

        The resizing increments are only significant under Motif or Xt.
        """
        return __core.Window_SetSizeHintsSz(*args, **kwargs)

    def SetVirtualSizeHints(*args, **kwargs):
        """SetVirtualSizeHints(self, int minW, int minH, int maxW=-1, int maxH=-1)"""
        return __core.Window_SetVirtualSizeHints(*args, **kwargs)

    def SetVirtualSizeHintsSz(*args, **kwargs):
        """SetVirtualSizeHintsSz(self, Size minSize, Size maxSize=DefaultSize)"""
        return __core.Window_SetVirtualSizeHintsSz(*args, **kwargs)

    SetVirtualSizeHints = wx.deprecated(SetVirtualSizeHints)
    SetVirtualSizeHintsSz = wx.deprecated(SetVirtualSizeHintsSz)

    def GetMaxSize(*args, **kwargs):
        """GetMaxSize(self) -> Size"""
        return __core.Window_GetMaxSize(*args, **kwargs)

    def GetMinSize(*args, **kwargs):
        """GetMinSize(self) -> Size"""
        return __core.Window_GetMinSize(*args, **kwargs)

    def SetMinSize(*args, **kwargs):
        """
        SetMinSize(self, Size minSize)

        A more convenient method than `SetSizeHints` for setting just the
        min size.
        """
        return __core.Window_SetMinSize(*args, **kwargs)

    def SetMaxSize(*args, **kwargs):
        """
        SetMaxSize(self, Size maxSize)

        A more convenient method than `SetSizeHints` for setting just the
        max size.
        """
        return __core.Window_SetMaxSize(*args, **kwargs)

    def GetMinWidth(*args, **kwargs):
        """GetMinWidth(self) -> int"""
        return __core.Window_GetMinWidth(*args, **kwargs)

    def GetMinHeight(*args, **kwargs):
        """GetMinHeight(self) -> int"""
        return __core.Window_GetMinHeight(*args, **kwargs)

    def GetMaxWidth(*args, **kwargs):
        """GetMaxWidth(self) -> int"""
        return __core.Window_GetMaxWidth(*args, **kwargs)

    def GetMaxHeight(*args, **kwargs):
        """GetMaxHeight(self) -> int"""
        return __core.Window_GetMaxHeight(*args, **kwargs)

    def SetMinClientSize(*args, **kwargs):
        """SetMinClientSize(self, Size size)"""
        return __core.Window_SetMinClientSize(*args, **kwargs)

    def SetMaxClientSize(*args, **kwargs):
        """SetMaxClientSize(self, Size size)"""
        return __core.Window_SetMaxClientSize(*args, **kwargs)

    def GetMinClientSize(*args, **kwargs):
        """GetMinClientSize(self) -> Size"""
        return __core.Window_GetMinClientSize(*args, **kwargs)

    def GetMaxClientSize(*args, **kwargs):
        """GetMaxClientSize(self) -> Size"""
        return __core.Window_GetMaxClientSize(*args, **kwargs)

    def SetVirtualSize(*args, **kwargs):
        """
        SetVirtualSize(self, Size size)

        Set the the virtual size of a window in pixels.  For most windows this
        is just the client area of the window, but for some like scrolled
        windows it is more or less independent of the screen window size.
        """
        return __core.Window_SetVirtualSize(*args, **kwargs)

    def SetVirtualSizeWH(*args, **kwargs):
        """
        SetVirtualSizeWH(self, int w, int h)

        Set the the virtual size of a window in pixels.  For most windows this
        is just the client area of the window, but for some like scrolled
        windows it is more or less independent of the screen window size.
        """
        return __core.Window_SetVirtualSizeWH(*args, **kwargs)

    def GetVirtualSize(*args, **kwargs):
        """
        GetVirtualSize(self) -> Size

        Get the the virtual size of the window in pixels.  For most windows
        this is just the client area of the window, but for some like scrolled
        windows it is more or less independent of the screen window size.
        """
        return __core.Window_GetVirtualSize(*args, **kwargs)

    def GetVirtualSizeTuple(*args, **kwargs):
        """
        GetVirtualSizeTuple() -> (width, height)

        Get the the virtual size of the window in pixels.  For most windows
        this is just the client area of the window, but for some like scrolled
        windows it is more or less independent of the screen window size.
        """
        return __core.Window_GetVirtualSizeTuple(*args, **kwargs)

    def GetWindowBorderSize(*args, **kwargs):
        """
        GetWindowBorderSize(self) -> Size

        Return the size of the left/right and top/bottom borders.
        """
        return __core.Window_GetWindowBorderSize(*args, **kwargs)

    def GetBestVirtualSize(*args, **kwargs):
        """
        GetBestVirtualSize(self) -> Size

        Return the largest of ClientSize and BestSize (as determined by a
        sizer, interior children, or other means)
        """
        return __core.Window_GetBestVirtualSize(*args, **kwargs)

    def InformFirstDirection(*args, **kwargs):
        """
        InformFirstDirection(self, int direction, int size, int availableOtherDir) -> bool

        wxSizer and friends use this to give a chance to a component to recalc
        its min size once one of the final size components is known. Override 
        this function when that is useful (such as for wxStaticText which can 
        stretch over several lines). Parameter availableOtherDir
        tells the item how much more space there is available in the opposite 
        direction (-1 if unknown).
        """
        return __core.Window_InformFirstDirection(*args, **kwargs)

    def SendSizeEvent(*args, **kwargs):
        """
        SendSizeEvent(self, int flags=0)

        Sends a size event to the window using its current size -- this has an
        effect of refreshing the window layout.

        By default the event is sent, i.e. processed immediately, but if flags
        value includes wxSEND_EVENT_POST then it's posted, i.e. only schedule
        for later processing.
        """
        return __core.Window_SendSizeEvent(*args, **kwargs)

    def SendSizeEventToParent(*args, **kwargs):
        """
        SendSizeEventToParent(self, int flags=0)

        This is a safe wrapper for GetParent().SendSizeEvent(): it checks that
        we have a parent window and it's not in process of being deleted.
        """
        return __core.Window_SendSizeEventToParent(*args, **kwargs)

    def PostSizeEvent(*args, **kwargs):
        """
        PostSizeEvent(self)

        This is a more readable synonym for SendSizeEvent(wx.SEND_EVENT_POST)
        """
        return __core.Window_PostSizeEvent(*args, **kwargs)

    def PostSizeEventToParent(*args, **kwargs):
        """
        PostSizeEventToParent(self)

        This is the same as SendSizeEventToParent() but using PostSizeEvent()
        """
        return __core.Window_PostSizeEventToParent(*args, **kwargs)

    def Show(*args, **kwargs):
        """
        Show(self, bool show=True) -> bool

        Shows or hides the window. You may need to call Raise for a top level
        window if you want to bring it to top, although this is not needed if
        Show is called immediately after the frame creation.  Returns True if
        the window has been shown or hidden or False if nothing was done
        because it already was in the requested state.
        """
        return __core.Window_Show(*args, **kwargs)

    def Hide(*args, **kwargs):
        """
        Hide(self) -> bool

        Equivalent to calling Show(False).
        """
        return __core.Window_Hide(*args, **kwargs)

    def ShowWithEffect(*args, **kwargs):
        """
        ShowWithEffect(self, int effect, unsigned int timeout=0) -> bool

        Show the window with a special effect, not implemented on most
        platforms (where it is the same as Show())

        Timeout specifies how long the animation should take, in ms, the
        default value of 0 means to use the default (system-dependent) value.

        """
        return __core.Window_ShowWithEffect(*args, **kwargs)

    def HideWithEffect(*args, **kwargs):
        """
        HideWithEffect(self, int effect, unsigned int timeout=0) -> bool

        Hide the window with a special effect, not implemented on most
        platforms (where it is the same as Hide())

        Timeout specifies how long the animation should take, in ms, the
        default value of 0 means to use the default (system-dependent) value.

        """
        return __core.Window_HideWithEffect(*args, **kwargs)

    def Enable(*args, **kwargs):
        """
        Enable(self, bool enable=True) -> bool

        Enable or disable the window for user input. Note that when a parent
        window is disabled, all of its children are disabled as well and they
        are reenabled again when the parent is.  Returns true if the window
        has been enabled or disabled, false if nothing was done, i.e. if the
        window had already been in the specified state.
        """
        return __core.Window_Enable(*args, **kwargs)

    def Disable(*args, **kwargs):
        """
        Disable(self) -> bool

        Disables the window, same as Enable(false).
        """
        return __core.Window_Disable(*args, **kwargs)

    def IsShown(*args, **kwargs):
        """
        IsShown(self) -> bool

        Returns true if the window is shown, false if it has been hidden.
        """
        return __core.Window_IsShown(*args, **kwargs)

    def IsEnabled(*args, **kwargs):
        """
        IsEnabled(self) -> bool

        Returns true if the window is enabled for input, false otherwise.
        This method takes into account the enabled state of parent windows up
        to the top-level window.
        """
        return __core.Window_IsEnabled(*args, **kwargs)

    def IsThisEnabled(*args, **kwargs):
        """
        IsThisEnabled(self) -> bool

        Returns the internal enabled state independent of the parent(s) state,
        i.e. the state in which the window would be if all of its parents are
        enabled.  Use `IsEnabled` to get the effective window state.
        """
        return __core.Window_IsThisEnabled(*args, **kwargs)

    def IsShownOnScreen(*args, **kwargs):
        """
        IsShownOnScreen(self) -> bool

        Returns ``True`` if the window is physically visible on the screen,
        i.e. it is shown and all its parents up to the toplevel window are
        shown as well.
        """
        return __core.Window_IsShownOnScreen(*args, **kwargs)

    def SetWindowStyleFlag(*args, **kwargs):
        """
        SetWindowStyleFlag(self, long style)

        Sets the style of the window. Please note that some styles cannot be
        changed after the window creation and that Refresh() might need to be
        called after changing the others for the change to take place
        immediately.
        """
        return __core.Window_SetWindowStyleFlag(*args, **kwargs)

    def GetWindowStyleFlag(*args, **kwargs):
        """
        GetWindowStyleFlag(self) -> long

        Gets the window style that was passed to the constructor or Create
        method.
        """
        return __core.Window_GetWindowStyleFlag(*args, **kwargs)

    SetWindowStyle = SetWindowStyleFlag; GetWindowStyle = GetWindowStyleFlag 
    def HasFlag(*args, **kwargs):
        """
        HasFlag(self, int flag) -> bool

        Test if the given style is set for this window.
        """
        return __core.Window_HasFlag(*args, **kwargs)

    def IsRetained(*args, **kwargs):
        """
        IsRetained(self) -> bool

        Returns true if the window is retained, false otherwise.  Retained
        windows are only available on X platforms.
        """
        return __core.Window_IsRetained(*args, **kwargs)

    def ToggleWindowStyle(*args, **kwargs):
        """
        ToggleWindowStyle(self, int flag) -> bool

        Turn the flag on if it had been turned off before and vice versa,
        returns True if the flag is turned on by this function call.
        """
        return __core.Window_ToggleWindowStyle(*args, **kwargs)

    def SetExtraStyle(*args, **kwargs):
        """
        SetExtraStyle(self, long exStyle)

        Sets the extra style bits for the window.  Extra styles are the less
        often used style bits which can't be set with the constructor or with
        SetWindowStyleFlag()
        """
        return __core.Window_SetExtraStyle(*args, **kwargs)

    def GetExtraStyle(*args, **kwargs):
        """
        GetExtraStyle(self) -> long

        Returns the extra style bits for the window.
        """
        return __core.Window_GetExtraStyle(*args, **kwargs)

    def HasExtraStyle(*args, **kwargs):
        """
        HasExtraStyle(self, int exFlag) -> bool

        Returns ``True`` if the given extra flag is set.
        """
        return __core.Window_HasExtraStyle(*args, **kwargs)

    def MakeModal(*args, **kwargs):
        """
        MakeModal(self, bool modal=True)

        Disables all other windows in the application so that the user can
        only interact with this window.  Passing False will reverse this
        effect.
        """
        return __core.Window_MakeModal(*args, **kwargs)

    def SetThemeEnabled(*args, **kwargs):
        """
        SetThemeEnabled(self, bool enableTheme)

        This function tells a window if it should use the system's "theme"
         code to draw the windows' background instead if its own background
         drawing code. This will only have an effect on platforms that support
         the notion of themes in user defined windows. One such platform is
         GTK+ where windows can have (very colourful) backgrounds defined by a
         user's selected theme.

        Dialogs, notebook pages and the status bar have this flag set to true
        by default so that the default look and feel is simulated best.
        """
        return __core.Window_SetThemeEnabled(*args, **kwargs)

    def GetThemeEnabled(*args, **kwargs):
        """
        GetThemeEnabled(self) -> bool

        Return the themeEnabled flag.
        """
        return __core.Window_GetThemeEnabled(*args, **kwargs)

    def SetFocus(*args, **kwargs):
        """
        SetFocus(self)

        Set's the focus to this window, allowing it to receive keyboard input.
        """
        return __core.Window_SetFocus(*args, **kwargs)

    def SetFocusFromKbd(*args, **kwargs):
        """
        SetFocusFromKbd(self)

        Set focus to this window as the result of a keyboard action.  Normally
        only called internally.
        """
        return __core.Window_SetFocusFromKbd(*args, **kwargs)

    def FindFocus(*args, **kwargs):
        """
        FindFocus() -> Window

        Returns the window or control that currently has the keyboard focus,
        or None.
        """
        return __core.Window_FindFocus(*args, **kwargs)

    FindFocus = staticmethod(FindFocus)
    def HasFocus(*args, **kwargs):
        """
        HasFocus(self) -> bool

        Returns ``True`` if the window has the keyboard focus.
        """
        return __core.Window_HasFocus(*args, **kwargs)

    def AcceptsFocus(*args, **kwargs):
        """
        AcceptsFocus(self) -> bool

        Can this window have focus?
        """
        return __core.Window_AcceptsFocus(*args, **kwargs)

    def CanAcceptFocus(*args, **kwargs):
        """
        CanAcceptFocus(self) -> bool

        Can this window have focus right now?
        """
        return __core.Window_CanAcceptFocus(*args, **kwargs)

    def AcceptsFocusFromKeyboard(*args, **kwargs):
        """
        AcceptsFocusFromKeyboard(self) -> bool

        Can this window be given focus by keyboard navigation? if not, the
        only way to give it focus (provided it accepts it at all) is to click
        it.
        """
        return __core.Window_AcceptsFocusFromKeyboard(*args, **kwargs)

    def CanAcceptFocusFromKeyboard(*args, **kwargs):
        """
        CanAcceptFocusFromKeyboard(self) -> bool

        Can this window be assigned focus from keyboard right now?
        """
        return __core.Window_CanAcceptFocusFromKeyboard(*args, **kwargs)

    def SetCanFocus(*args, **kwargs):
        """SetCanFocus(self, bool canFocus)"""
        return __core.Window_SetCanFocus(*args, **kwargs)

    def NavigateIn(*args, **kwargs):
        """
        NavigateIn(self, int flags=NavigationKeyEvent.IsForward) -> bool

        Navigates inside this window.
        """
        return __core.Window_NavigateIn(*args, **kwargs)

    def Navigate(*args, **kwargs):
        """
        Navigate(self, int flags=NavigationKeyEvent.IsForward) -> bool

        Does keyboard navigation starting from this window to another.  This is
        equivalient to self.GetParent().NavigateIn().
        """
        return __core.Window_Navigate(*args, **kwargs)

    def HandleAsNavigationKey(*args, **kwargs):
        """
        HandleAsNavigationKey(self, KeyEvent event) -> bool

        This function will generate the appropriate call to `Navigate` if the
        key event is one normally used for keyboard navigation.  Returns
        ``True`` if the key pressed was for navigation and was handled,
        ``False`` otherwise.
        """
        return __core.Window_HandleAsNavigationKey(*args, **kwargs)

    def MoveAfterInTabOrder(*args, **kwargs):
        """
        MoveAfterInTabOrder(self, Window win)

        Moves this window in the tab navigation order after the specified
        sibling window.  This means that when the user presses the TAB key on
        that other window, the focus switches to this window.

        The default tab order is the same as creation order.  This function
        and `MoveBeforeInTabOrder` allow to change it after creating all the
        windows.
        """
        return __core.Window_MoveAfterInTabOrder(*args, **kwargs)

    def MoveBeforeInTabOrder(*args, **kwargs):
        """
        MoveBeforeInTabOrder(self, Window win)

        Same as `MoveAfterInTabOrder` except that it inserts this window just
        before win instead of putting it right after it.
        """
        return __core.Window_MoveBeforeInTabOrder(*args, **kwargs)

    def GetChildren(*args, **kwargs):
        """
        GetChildren(self) -> WindowList

        Returns an object containing a list of the window's children.  The
        object provides a Python sequence-like interface over the internal
        list maintained by the window..
        """
        return __core.Window_GetChildren(*args, **kwargs)

    def GetPrevSibling(*args, **kwargs):
        """GetPrevSibling(self) -> Window"""
        return __core.Window_GetPrevSibling(*args, **kwargs)

    def GetNextSibling(*args, **kwargs):
        """GetNextSibling(self) -> Window"""
        return __core.Window_GetNextSibling(*args, **kwargs)

    def GetParent(*args, **kwargs):
        """
        GetParent(self) -> Window

        Returns the parent window of this window, or None if there isn't one.
        """
        return __core.Window_GetParent(*args, **kwargs)

    def GetGrandParent(*args, **kwargs):
        """
        GetGrandParent(self) -> Window

        Returns the parent of the parent of this window, or None if there
        isn't one.
        """
        return __core.Window_GetGrandParent(*args, **kwargs)

    def GetTopLevelParent(*args, **kwargs):
        """
        GetTopLevelParent(self) -> Window

        Returns the first frame or dialog in this window's parental hierarchy.
        """
        return __core.Window_GetTopLevelParent(*args, **kwargs)

    def IsTopLevel(*args, **kwargs):
        """
        IsTopLevel(self) -> bool

        Returns true if the given window is a top-level one. Currently all
        frames and dialogs are always considered to be top-level windows (even
        if they have a parent window).
        """
        return __core.Window_IsTopLevel(*args, **kwargs)

    def Reparent(*args, **kwargs):
        """
        Reparent(self, Window newParent) -> bool

        Reparents the window, i.e the window will be removed from its current
        parent window (e.g. a non-standard toolbar in a wxFrame) and then
        re-inserted into another. Available on Windows and GTK.  Returns True
        if the parent was changed, False otherwise (error or newParent ==
        oldParent)
        """
        return __core.Window_Reparent(*args, **kwargs)

    def AddChild(*args, **kwargs):
        """
        AddChild(self, Window child)

        Adds a child window. This is called automatically by window creation
        functions so should not be required by the application programmer.
        """
        return __core.Window_AddChild(*args, **kwargs)

    def RemoveChild(*args, **kwargs):
        """
        RemoveChild(self, Window child)

        Removes a child window. This is called automatically by window
        deletion functions so should not be required by the application
        programmer.
        """
        return __core.Window_RemoveChild(*args, **kwargs)

    def FindWindowById(*args, **kwargs):
        """
        FindWindowById(self, long winid) -> Window

        Find a child of this window by window ID
        """
        return __core.Window_FindWindowById(*args, **kwargs)

    def FindWindowByName(*args, **kwargs):
        """
        FindWindowByName(self, String name) -> Window

        Find a child of this window by name
        """
        return __core.Window_FindWindowByName(*args, **kwargs)

    def FindWindowByLabel(*args, **kwargs):
        """
        FindWindowByLabel(self, String label) -> Window

        Find a child of this window by label
        """
        return __core.Window_FindWindowByLabel(*args, **kwargs)

    def GetEventHandler(*args, **kwargs):
        """
        GetEventHandler(self) -> EvtHandler

        Returns the event handler for this window. By default, the window is
        its own event handler.
        """
        return __core.Window_GetEventHandler(*args, **kwargs)

    def SetEventHandler(*args, **kwargs):
        """
        SetEventHandler(self, EvtHandler handler)

        Sets the event handler for this window.  An event handler is an object
        that is capable of processing the events sent to a window.  (In other
        words, is able to dispatch the events to handler function.)  By
        default, the window is its own event handler, but an application may
        wish to substitute another, for example to allow central
        implementation of event-handling for a variety of different window
        classes.

        It is usually better to use `wx.Window.PushEventHandler` since this sets
        up a chain of event handlers, where an event not handled by one event
        handler is handed off to the next one in the chain.
        """
        return __core.Window_SetEventHandler(*args, **kwargs)

    def PushEventHandler(*args, **kwargs):
        """
        PushEventHandler(self, EvtHandler handler)

        Pushes this event handler onto the event handler stack for the window.
        An event handler is an object that is capable of processing the events
        sent to a window.  (In other words, is able to dispatch the events to a
        handler function.)  By default, the window is its own event handler,
        but an application may wish to substitute another, for example to
        allow central implementation of event-handling for a variety of
        different window classes.

        wx.Window.PushEventHandler allows an application to set up a chain of
        event handlers, where an event not handled by one event handler is
        handed to the next one in the chain.  Use `wx.Window.PopEventHandler`
        to remove the event handler.  Ownership of the handler is *not* given
        to the window, so you should be sure to pop the handler before the
        window is destroyed and either let PopEventHandler destroy it, or call
        its Destroy method yourself.
        """
        return __core.Window_PushEventHandler(*args, **kwargs)

    def PopEventHandler(*args, **kwargs):
        """
        PopEventHandler(self, bool deleteHandler=False) -> EvtHandler

        Removes and returns the top-most event handler on the event handler
        stack.  If deleteHandler is True then the wx.EvtHandler object will be
        destroyed after it is popped, and ``None`` will be returned instead.
        """
        return __core.Window_PopEventHandler(*args, **kwargs)

    def RemoveEventHandler(*args, **kwargs):
        """
        RemoveEventHandler(self, EvtHandler handler) -> bool

        Find the given handler in the event handler chain and remove (but not
        delete) it from the event handler chain, returns True if it was found
        and False otherwise (this also results in an assert failure so this
        function should only be called when the handler is supposed to be
        there.)
        """
        return __core.Window_RemoveEventHandler(*args, **kwargs)

    def ProcessWindowEvent(*args, **kwargs):
        """
        ProcessWindowEvent(self, Event event) -> bool

        Process an event by calling GetEventHandler().ProcessEvent(): this
        is a straightforward replacement for ProcessEvent() itself which
        shouldn't be used directly with windows as it doesn't take into
        account any event handlers associated with the window
        """
        return __core.Window_ProcessWindowEvent(*args, **kwargs)

    def HandleWindowEvent(*args, **kwargs):
        """
        HandleWindowEvent(self, Event event) -> bool

        Process an event by calling GetEventHandler()->ProcessEvent() and
        handling any exceptions thrown by event handlers. It's mostly useful
        when processing wx events when called from C code (e.g. in GTK+
        callback) when the exception wouldn't correctly propagate to
        wx.EventLoop.
        """
        return __core.Window_HandleWindowEvent(*args, **kwargs)

    def SetValidator(*args, **kwargs):
        """
        SetValidator(self, Validator validator)

        Deletes the current validator (if any) and sets the window validator,
        having called wx.Validator.Clone to create a new validator of this
        type.
        """
        return __core.Window_SetValidator(*args, **kwargs)

    def GetValidator(*args, **kwargs):
        """
        GetValidator(self) -> Validator

        Returns a pointer to the current validator for the window, or None if
        there is none.
        """
        return __core.Window_GetValidator(*args, **kwargs)

    def Validate(*args, **kwargs):
        """
        Validate(self) -> bool

        Validates the current values of the child controls using their
        validators.  If the window has wx.WS_EX_VALIDATE_RECURSIVELY extra
        style flag set, the method will also call Validate() of all child
        windows.  Returns false if any of the validations failed.
        """
        return __core.Window_Validate(*args, **kwargs)

    def TransferDataToWindow(*args, **kwargs):
        """
        TransferDataToWindow(self) -> bool

        Transfers values to child controls from data areas specified by their
        validators.  If the window has wx.WS_EX_VALIDATE_RECURSIVELY extra
        style flag set, the method will also call TransferDataToWindow() of
        all child windows.
        """
        return __core.Window_TransferDataToWindow(*args, **kwargs)

    def TransferDataFromWindow(*args, **kwargs):
        """
        TransferDataFromWindow(self) -> bool

        Transfers values from child controls to data areas specified by their
        validators. Returns false if a transfer failed.  If the window has
        wx.WS_EX_VALIDATE_RECURSIVELY extra style flag set, the method will
        also call TransferDataFromWindow() of all child windows.
        """
        return __core.Window_TransferDataFromWindow(*args, **kwargs)

    def InitDialog(*args, **kwargs):
        """
        InitDialog(self)

        Sends an EVT_INIT_DIALOG event, whose handler usually transfers data
        to the dialog via validators.
        """
        return __core.Window_InitDialog(*args, **kwargs)

    def SetAcceleratorTable(*args, **kwargs):
        """
        SetAcceleratorTable(self, AcceleratorTable accel)

        Sets the accelerator table for this window.
        """
        return __core.Window_SetAcceleratorTable(*args, **kwargs)

    def GetAcceleratorTable(*args, **kwargs):
        """
        GetAcceleratorTable(self) -> AcceleratorTable

        Gets the accelerator table for this window.
        """
        return __core.Window_GetAcceleratorTable(*args, **kwargs)

    def RegisterHotKey(*args, **kwargs):
        """
        RegisterHotKey(self, int hotkeyId, int modifiers, int keycode) -> bool

        Registers a system wide hotkey. Every time the user presses the hotkey
        registered here, this window will receive a hotkey event. It will
        receive the event even if the application is in the background and
        does not have the input focus because the user is working with some
        other application.  To bind an event handler function to this hotkey
        use EVT_HOTKEY with an id equal to hotkeyId.  Returns True if the
        hotkey was registered successfully.
        """
        return __core.Window_RegisterHotKey(*args, **kwargs)

    def UnregisterHotKey(*args, **kwargs):
        """
        UnregisterHotKey(self, int hotkeyId) -> bool

        Unregisters a system wide hotkey.
        """
        return __core.Window_UnregisterHotKey(*args, **kwargs)

    def ConvertDialogPointToPixels(*args, **kwargs):
        """
        ConvertDialogPointToPixels(self, Point pt) -> Point

        Converts a point or size from dialog units to pixels.  Dialog units
        are used for maintaining a dialog's proportions even if the font
        changes. For the x dimension, the dialog units are multiplied by the
        average character width and then divided by 4. For the y dimension,
        the dialog units are multiplied by the average character height and
        then divided by 8.
        """
        return __core.Window_ConvertDialogPointToPixels(*args, **kwargs)

    def ConvertDialogSizeToPixels(*args, **kwargs):
        """
        ConvertDialogSizeToPixels(self, Size sz) -> Size

        Converts a point or size from dialog units to pixels.  Dialog units
        are used for maintaining a dialog's proportions even if the font
        changes. For the x dimension, the dialog units are multiplied by the
        average character width and then divided by 4. For the y dimension,
        the dialog units are multiplied by the average character height and
        then divided by 8.
        """
        return __core.Window_ConvertDialogSizeToPixels(*args, **kwargs)

    def DLG_PNT(*args, **kwargs):
        """
        DLG_PNT(self, Point pt) -> Point

        Converts a point or size from dialog units to pixels.  Dialog units
        are used for maintaining a dialog's proportions even if the font
        changes. For the x dimension, the dialog units are multiplied by the
        average character width and then divided by 4. For the y dimension,
        the dialog units are multiplied by the average character height and
        then divided by 8.
        """
        return __core.Window_DLG_PNT(*args, **kwargs)

    def DLG_SZE(*args, **kwargs):
        """
        DLG_SZE(self, Size sz) -> Size

        Converts a point or size from dialog units to pixels.  Dialog units
        are used for maintaining a dialog's proportions even if the font
        changes. For the x dimension, the dialog units are multiplied by the
        average character width and then divided by 4. For the y dimension,
        the dialog units are multiplied by the average character height and
        then divided by 8.
        """
        return __core.Window_DLG_SZE(*args, **kwargs)

    def ConvertPixelPointToDialog(*args, **kwargs):
        """ConvertPixelPointToDialog(self, Point pt) -> Point"""
        return __core.Window_ConvertPixelPointToDialog(*args, **kwargs)

    def ConvertPixelSizeToDialog(*args, **kwargs):
        """ConvertPixelSizeToDialog(self, Size sz) -> Size"""
        return __core.Window_ConvertPixelSizeToDialog(*args, **kwargs)

    def WarpPointer(*args, **kwargs):
        """
        WarpPointer(self, int x, int y)

        Moves the pointer to the given position on the window.

        NOTE: This function is not supported under Mac because Apple Human
        Interface Guidelines forbid moving the mouse cursor programmatically.
        """
        return __core.Window_WarpPointer(*args, **kwargs)

    def CaptureMouse(*args, **kwargs):
        """
        CaptureMouse(self)

        Directs all mouse input to this window. Call wx.Window.ReleaseMouse to
        release the capture.

        Note that wxWindows maintains the stack of windows having captured the
        mouse and when the mouse is released the capture returns to the window
        which had had captured it previously and it is only really released if
        there were no previous window. In particular, this means that you must
        release the mouse as many times as you capture it, unless the window
        receives the `wx.MouseCaptureLostEvent` event.
         
        Any application which captures the mouse in the beginning of some
        operation *must* handle `wx.MouseCaptureLostEvent` and cancel this
        operation when it receives the event. The event handler must not
        recapture mouse.
        """
        return __core.Window_CaptureMouse(*args, **kwargs)

    def ReleaseMouse(*args, **kwargs):
        """
        ReleaseMouse(self)

        Releases mouse input captured with wx.Window.CaptureMouse.
        """
        return __core.Window_ReleaseMouse(*args, **kwargs)

    def GetCapture(*args, **kwargs):
        """
        GetCapture() -> Window

        Returns the window which currently captures the mouse or None
        """
        return __core.Window_GetCapture(*args, **kwargs)

    GetCapture = staticmethod(GetCapture)
    def HasCapture(*args, **kwargs):
        """
        HasCapture(self) -> bool

        Returns true if this window has the current mouse capture.
        """
        return __core.Window_HasCapture(*args, **kwargs)

    def Refresh(*args, **kwargs):
        """
        Refresh(self, bool eraseBackground=True, Rect rect=None)

        Mark the specified rectangle (or the whole window) as "dirty" so it
        will be repainted.  Causes an EVT_PAINT event to be generated and sent
        to the window.
        """
        return __core.Window_Refresh(*args, **kwargs)

    def RefreshRect(*args, **kwargs):
        """
        RefreshRect(self, Rect rect, bool eraseBackground=True)

        Redraws the contents of the given rectangle: the area inside it will
        be repainted.  This is the same as Refresh but has a nicer syntax.
        """
        return __core.Window_RefreshRect(*args, **kwargs)

    def Update(*args, **kwargs):
        """
        Update(self)

        Calling this method immediately repaints the invalidated area of the
        window instead of waiting for the EVT_PAINT event to happen, (normally
        this would usually only happen when the flow of control returns to the
        event loop.)  Notice that this function doesn't refresh the window and
        does nothing if the window has been already repainted.  Use `Refresh`
        first if you want to immediately redraw the window (or some portion of
        it) unconditionally.
        """
        return __core.Window_Update(*args, **kwargs)

    def ClearBackground(*args, **kwargs):
        """
        ClearBackground(self)

        Clears the window by filling it with the current background
        colour. Does not cause an erase background event to be generated.
        """
        return __core.Window_ClearBackground(*args, **kwargs)

    def Freeze(*args, **kwargs):
        """
        Freeze(self)

        Freezes the window or, in other words, prevents any updates from
        taking place on screen, the window is not redrawn at all. Thaw must be
        called to reenable window redrawing.  Calls to Freeze/Thaw may be
        nested, with the actual Thaw being delayed until all the nesting has
        been undone.

        This method is useful for visual appearance optimization (for example,
        it is a good idea to use it before inserting large amount of text into
        a wxTextCtrl under wxGTK) but is not implemented on all platforms nor
        for all controls so it is mostly just a hint to wxWindows and not a
        mandatory directive.
        """
        return __core.Window_Freeze(*args, **kwargs)

    def IsFrozen(*args, **kwargs):
        """
        IsFrozen(self) -> bool

        Returns ``True`` if the window has been frozen and not thawed yet.

        :see: `Freeze` and `Thaw`
        """
        return __core.Window_IsFrozen(*args, **kwargs)

    def Thaw(*args, **kwargs):
        """
        Thaw(self)

        Reenables window updating after a previous call to Freeze.  Calls to
        Freeze/Thaw may be nested, so Thaw must be called the same number of
        times that Freeze was before the window will be updated.
        """
        return __core.Window_Thaw(*args, **kwargs)

    def IsDoubleBuffered(*args, **kwargs):
        """
        IsDoubleBuffered(self) -> bool

        Returns ``True`` if the window contents is double-buffered by the
        system, i.e. if any drawing done on the window is really done on a
        temporary backing surface and transferred to the screen all at once
        later.
        """
        return __core.Window_IsDoubleBuffered(*args, **kwargs)

    def SetDoubleBuffered(*args, **kwargs):
        """
        SetDoubleBuffered(self, bool on)

        Put the native window into double buffered or composited mode.
        """
        return __core.Window_SetDoubleBuffered(*args, **kwargs)

    def GetUpdateRegion(*args, **kwargs):
        """
        GetUpdateRegion(self) -> Region

        Returns the region specifying which parts of the window have been
        damaged. Should only be called within an EVT_PAINT handler.
        """
        return __core.Window_GetUpdateRegion(*args, **kwargs)

    def GetUpdateClientRect(*args, **kwargs):
        """
        GetUpdateClientRect(self) -> Rect

        Get the update rectangle region bounding box in client coords.
        """
        return __core.Window_GetUpdateClientRect(*args, **kwargs)

    def IsExposed(*args, **kwargs):
        """
        IsExposed(self, int x, int y, int w=1, int h=1) -> bool

        Returns true if the given point or rectangle area has been exposed
        since the last repaint. Call this in an paint event handler to
        optimize redrawing by only redrawing those areas, which have been
        exposed.
        """
        return __core.Window_IsExposed(*args, **kwargs)

    def IsExposedPoint(*args, **kwargs):
        """
        IsExposedPoint(self, Point pt) -> bool

        Returns true if the given point or rectangle area has been exposed
        since the last repaint. Call this in an paint event handler to
        optimize redrawing by only redrawing those areas, which have been
        exposed.
        """
        return __core.Window_IsExposedPoint(*args, **kwargs)

    def IsExposedRect(*args, **kwargs):
        """
        IsExposedRect(self, Rect rect) -> bool

        Returns true if the given point or rectangle area has been exposed
        since the last repaint. Call this in an paint event handler to
        optimize redrawing by only redrawing those areas, which have been
        exposed.
        """
        return __core.Window_IsExposedRect(*args, **kwargs)

    def GetDefaultAttributes(*args, **kwargs):
        """
        GetDefaultAttributes(self) -> VisualAttributes

        Get the default attributes for an instance of this class.  This is
        useful if you want to use the same font or colour in your own control
        as in a standard control -- which is a much better idea than hard
        coding specific colours or fonts which might look completely out of
        place on the user's system, especially if it uses themes.
        """
        return __core.Window_GetDefaultAttributes(*args, **kwargs)

    def GetClassDefaultAttributes(*args, **kwargs):
        """
        GetClassDefaultAttributes(int variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes

        Get the default attributes for this class.  This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        user's system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignore under other platforms. Under Mac, it will change the size of
        the returned font. See `wx.Window.SetWindowVariant` for more about
        this.
        """
        return __core.Window_GetClassDefaultAttributes(*args, **kwargs)

    GetClassDefaultAttributes = staticmethod(GetClassDefaultAttributes)
    def SetBackgroundColour(*args, **kwargs):
        """
        SetBackgroundColour(self, Colour colour) -> bool

        Sets the background colour of the window.  Returns True if the colour
        was changed.  The background colour is usually painted by the default
        EVT_ERASE_BACKGROUND event handler function under Windows and
        automatically under GTK.  Using `wx.NullColour` will reset the window
        to the default background colour.

        Note that setting the background colour may not cause an immediate
        refresh, so you may wish to call `ClearBackground` or `Refresh` after
        calling this function.

        Using this function will disable attempts to use themes for this
        window, if the system supports them.  Use with care since usually the
        themes represent the appearance chosen by the user to be used for all
        applications on the system.
        """
        return __core.Window_SetBackgroundColour(*args, **kwargs)

    def SetOwnBackgroundColour(*args, **kwargs):
        """SetOwnBackgroundColour(self, Colour colour)"""
        return __core.Window_SetOwnBackgroundColour(*args, **kwargs)

    def SetForegroundColour(*args, **kwargs):
        """
        SetForegroundColour(self, Colour colour) -> bool

        Sets the foreground colour of the window.  Returns True is the colour
        was changed.  The interpretation of foreground colour is dependent on
        the window class; it may be the text colour or other colour, or it may
        not be used at all.
        """
        return __core.Window_SetForegroundColour(*args, **kwargs)

    def SetOwnForegroundColour(*args, **kwargs):
        """SetOwnForegroundColour(self, Colour colour)"""
        return __core.Window_SetOwnForegroundColour(*args, **kwargs)

    def GetBackgroundColour(*args, **kwargs):
        """
        GetBackgroundColour(self) -> Colour

        Returns the background colour of the window.
        """
        return __core.Window_GetBackgroundColour(*args, **kwargs)

    def GetForegroundColour(*args, **kwargs):
        """
        GetForegroundColour(self) -> Colour

        Returns the foreground colour of the window.  The interpretation of
        foreground colour is dependent on the window class; it may be the text
        colour or other colour, or it may not be used at all.
        """
        return __core.Window_GetForegroundColour(*args, **kwargs)

    def InheritsBackgroundColour(*args, **kwargs):
        """InheritsBackgroundColour(self) -> bool"""
        return __core.Window_InheritsBackgroundColour(*args, **kwargs)

    def UseBgCol(*args, **kwargs):
        """UseBgCol(self) -> bool"""
        return __core.Window_UseBgCol(*args, **kwargs)

    def SetBackgroundStyle(*args, **kwargs):
        """
        SetBackgroundStyle(self, int style) -> bool

        Returns the background style of the window. The background style
        indicates how the background of the window is drawn.

            ======================  ========================================
            wx.BG_STYLE_SYSTEM      The background colour or pattern should
                                    be determined by the system
            wx.BG_STYLE_COLOUR      The background should be a solid colour
            wx.BG_STYLE_CUSTOM      The background will be implemented by the
                                    application.
            ======================  ========================================

        On GTK+, use of wx.BG_STYLE_CUSTOM allows the flicker-free drawing of
        a custom background, such as a tiled bitmap. Currently the style has
        no effect on other platforms.

        :see: `GetBackgroundStyle`, `SetBackgroundColour`
        """
        return __core.Window_SetBackgroundStyle(*args, **kwargs)

    def GetBackgroundStyle(*args, **kwargs):
        """
        GetBackgroundStyle(self) -> int

        Returns the background style of the window.

        :see: `SetBackgroundStyle`
        """
        return __core.Window_GetBackgroundStyle(*args, **kwargs)

    def HasTransparentBackground(*args, **kwargs):
        """
        HasTransparentBackground(self) -> bool

        Returns True if this window's background is transparent (as, for
        example, for `wx.StaticText`) and should show the parent window's
        background.

        This method is mostly used internally by the library itself and you
        normally shouldn't have to call it. You may, however, have to override
        it in your custom control classes to ensure that background is painted
        correctly.
        """
        return __core.Window_HasTransparentBackground(*args, **kwargs)

    def SetCursor(*args, **kwargs):
        """
        SetCursor(self, Cursor cursor) -> bool

        Sets the window's cursor. Notice that the window cursor also sets it
        for the children of the window implicitly.

        The cursor may be wx.NullCursor in which case the window cursor will
        be reset back to default.
        """
        return __core.Window_SetCursor(*args, **kwargs)

    def GetCursor(*args, **kwargs):
        """
        GetCursor(self) -> Cursor

        Return the cursor associated with this window.
        """
        return __core.Window_GetCursor(*args, **kwargs)

    def SetFont(*args, **kwargs):
        """
        SetFont(self, Font font) -> bool

        Sets the font for this window.
        """
        return __core.Window_SetFont(*args, **kwargs)

    def SetOwnFont(*args, **kwargs):
        """SetOwnFont(self, Font font)"""
        return __core.Window_SetOwnFont(*args, **kwargs)

    def GetFont(*args, **kwargs):
        """
        GetFont(self) -> Font

        Returns the default font used for this window.
        """
        return __core.Window_GetFont(*args, **kwargs)

    def SetCaret(*args, **kwargs):
        """
        SetCaret(self, Caret caret)

        Sets the caret associated with the window.
        """
        return __core.Window_SetCaret(*args, **kwargs)

    def GetCaret(*args, **kwargs):
        """
        GetCaret(self) -> Caret

        Returns the caret associated with the window.
        """
        return __core.Window_GetCaret(*args, **kwargs)

    def GetCharHeight(*args, **kwargs):
        """
        GetCharHeight(self) -> int

        Get the (average) character size for the current font.
        """
        return __core.Window_GetCharHeight(*args, **kwargs)

    def GetCharWidth(*args, **kwargs):
        """
        GetCharWidth(self) -> int

        Get the (average) character size for the current font.
        """
        return __core.Window_GetCharWidth(*args, **kwargs)

    def GetTextExtent(*args, **kwargs):
        """
        GetTextExtent(String string) -> (width, height)

        Get the width and height of the text using the current font.
        """
        return __core.Window_GetTextExtent(*args, **kwargs)

    def GetFullTextExtent(*args, **kwargs):
        """
        GetFullTextExtent(String string, Font font=None) ->
           (width, height, descent, externalLeading)

        Get the width, height, decent and leading of the text using the
        current or specified font.
        """
        return __core.Window_GetFullTextExtent(*args, **kwargs)

    def ClientToScreenXY(*args, **kwargs):
        """
        ClientToScreenXY(int x, int y) -> (x,y)

        Converts to screen coordinates from coordinates relative to this window.
        """
        return __core.Window_ClientToScreenXY(*args, **kwargs)

    def ScreenToClientXY(*args, **kwargs):
        """
        ScreenToClientXY(int x, int y) -> (x,y)

        Converts from screen to client window coordinates.
        """
        return __core.Window_ScreenToClientXY(*args, **kwargs)

    def ClientToScreen(*args, **kwargs):
        """
        ClientToScreen(self, Point pt) -> Point

        Converts to screen coordinates from coordinates relative to this window.
        """
        return __core.Window_ClientToScreen(*args, **kwargs)

    def ScreenToClient(*args, **kwargs):
        """
        ScreenToClient(self, Point pt) -> Point

        Converts from screen to client window coordinates.
        """
        return __core.Window_ScreenToClient(*args, **kwargs)

    def HitTestXY(*args, **kwargs):
        """
        HitTestXY(self, int x, int y) -> int

        Test where the given (in client coords) point lies
        """
        return __core.Window_HitTestXY(*args, **kwargs)

    def HitTest(*args, **kwargs):
        """
        HitTest(self, Point pt) -> int

        Test where the given (in client coords) point lies
        """
        return __core.Window_HitTest(*args, **kwargs)

    def GetBorder(*args):
        """
        GetBorder(self, long flags) -> int
        GetBorder(self) -> int

        Get border for the flags of this window
        """
        return __core.Window_GetBorder(*args)

    def UpdateWindowUI(*args, **kwargs):
        """
        UpdateWindowUI(self, long flags=UPDATE_UI_NONE)

        This function sends EVT_UPDATE_UI events to the window. The particular
        implementation depends on the window; for example a wx.ToolBar will
        send an update UI event for each toolbar button, and a wx.Frame will
        send an update UI event for each menubar menu item. You can call this
        function from your application to ensure that your UI is up-to-date at
        a particular point in time (as far as your EVT_UPDATE_UI handlers are
        concerned). This may be necessary if you have called
        `wx.UpdateUIEvent.SetMode` or `wx.UpdateUIEvent.SetUpdateInterval` to
        limit the overhead that wxWindows incurs by sending update UI events
        in idle time.
        """
        return __core.Window_UpdateWindowUI(*args, **kwargs)

    def PopupMenuXY(*args, **kwargs):
        """
        PopupMenuXY(self, Menu menu, int x=-1, int y=-1) -> bool

        Pops up the given menu at the specified coordinates, relative to this window,
        and returns control when the user has dismissed the menu. If a menu item is
        selected, the corresponding menu event is generated and will be processed as
        usual.  If the default position is given then the current position of the
        mouse cursor will be used.
        """
        return __core.Window_PopupMenuXY(*args, **kwargs)

    def PopupMenu(*args, **kwargs):
        """
        PopupMenu(self, Menu menu, Point pos=DefaultPosition) -> bool

        Pops up the given menu at the specified coordinates, relative to this window,
        and returns control when the user has dismissed the menu. If a menu item is
        selected, the corresponding menu event is generated and will be processed as
        usual.  If the default position is given then the current position of the
        mouse cursor will be used.
        """
        return __core.Window_PopupMenu(*args, **kwargs)

    def GetPopupMenuSelectionFromUser(*args, **kwargs):
        """
        GetPopupMenuSelectionFromUser(self, Menu menu, Point pos=DefaultPosition) -> int

        Simply return the id of the selected item or wxID_NONE without
        generating any events.
        """
        return __core.Window_GetPopupMenuSelectionFromUser(*args, **kwargs)

    def HasMultiplePages(*args, **kwargs):
        """HasMultiplePages(self) -> bool"""
        return __core.Window_HasMultiplePages(*args, **kwargs)

    def SendIdleEvents(*args, **kwargs):
        """
        SendIdleEvents(self, IdleEvent event) -> bool

        Send idle event to window and all subwindows.  Returns True if more
        idle time is requested.
        """
        return __core.Window_SendIdleEvents(*args, **kwargs)

    def GetHandle(*args, **kwargs):
        """
        GetHandle(self) -> long

        Returns the platform-specific handle (as a long integer) of the
        physical window.  On wxMSW this is the win32 window handle, on wxGTK
        it is the XWindow ID, and on wxMac it is the ControlRef.
        """
        return __core.Window_GetHandle(*args, **kwargs)

    def AssociateHandle(*args, **kwargs):
        """
        AssociateHandle(self, long handle)

        Associate the window with a new native handle
        """
        return __core.Window_AssociateHandle(*args, **kwargs)

    def DissociateHandle(*args, **kwargs):
        """
        DissociateHandle(self)

        Dissociate the current native handle from the window
        """
        return __core.Window_DissociateHandle(*args, **kwargs)

    def GetGtkWidget(*args, **kwargs):
        """
        GetGtkWidget(self) -> long

        On wxGTK returns a pointer to the GtkWidget for this window as a long
        integer.  On the other platforms this method returns zero.
        """
        return __core.Window_GetGtkWidget(*args, **kwargs)

    def CanScroll(*args, **kwargs):
        """
        CanScroll(self, int orient) -> bool

        Can the window have the scrollbar in this orientation?
        """
        return __core.Window_CanScroll(*args, **kwargs)

    def HasScrollbar(*args, **kwargs):
        """
        HasScrollbar(self, int orient) -> bool

        Does the window have the scrollbar for this orientation?
        """
        return __core.Window_HasScrollbar(*args, **kwargs)

    def SetScrollbar(*args, **kwargs):
        """
        SetScrollbar(self, int orientation, int position, int thumbSize, int range, 
            bool refresh=True)

        Sets the scrollbar properties of a built-in scrollbar.
        """
        return __core.Window_SetScrollbar(*args, **kwargs)

    def SetScrollPos(*args, **kwargs):
        """
        SetScrollPos(self, int orientation, int pos, bool refresh=True)

        Sets the position of one of the built-in scrollbars.
        """
        return __core.Window_SetScrollPos(*args, **kwargs)

    def GetScrollPos(*args, **kwargs):
        """
        GetScrollPos(self, int orientation) -> int

        Returns the built-in scrollbar position.
        """
        return __core.Window_GetScrollPos(*args, **kwargs)

    def GetScrollThumb(*args, **kwargs):
        """
        GetScrollThumb(self, int orientation) -> int

        Returns the built-in scrollbar thumb size.
        """
        return __core.Window_GetScrollThumb(*args, **kwargs)

    def GetScrollRange(*args, **kwargs):
        """
        GetScrollRange(self, int orientation) -> int

        Returns the built-in scrollbar range.
        """
        return __core.Window_GetScrollRange(*args, **kwargs)

    def ScrollWindow(*args, **kwargs):
        """
        ScrollWindow(self, int dx, int dy, Rect rect=None)

        Physically scrolls the pixels in the window and move child windows
        accordingly.  Use this function to optimise your scrolling
        implementations, to minimise the area that must be redrawn. Note that
        it is rarely required to call this function from a user program.
        """
        return __core.Window_ScrollWindow(*args, **kwargs)

    def ScrollLines(*args, **kwargs):
        """
        ScrollLines(self, int lines) -> bool

        If the platform and window class supports it, scrolls the window by
        the given number of lines down, if lines is positive, or up if lines
        is negative.  Returns True if the window was scrolled, False if it was
        already on top/bottom and nothing was done.
        """
        return __core.Window_ScrollLines(*args, **kwargs)

    def ScrollPages(*args, **kwargs):
        """
        ScrollPages(self, int pages) -> bool

        If the platform and window class supports it, scrolls the window by
        the given number of pages down, if pages is positive, or up if pages
        is negative.  Returns True if the window was scrolled, False if it was
        already on top/bottom and nothing was done.
        """
        return __core.Window_ScrollPages(*args, **kwargs)

    def LineUp(*args, **kwargs):
        """
        LineUp(self) -> bool

        This is just a wrapper for ScrollLines(-1).
        """
        return __core.Window_LineUp(*args, **kwargs)

    def LineDown(*args, **kwargs):
        """
        LineDown(self) -> bool

        This is just a wrapper for ScrollLines(1).
        """
        return __core.Window_LineDown(*args, **kwargs)

    def PageUp(*args, **kwargs):
        """
        PageUp(self) -> bool

        This is just a wrapper for ScrollPages(-1).
        """
        return __core.Window_PageUp(*args, **kwargs)

    def PageDown(*args, **kwargs):
        """
        PageDown(self) -> bool

        This is just a wrapper for ScrollPages(1).
        """
        return __core.Window_PageDown(*args, **kwargs)

    def AlwaysShowScrollbars(*args, **kwargs):
        """AlwaysShowScrollbars(self, bool horz=True, bool vert=True)"""
        return __core.Window_AlwaysShowScrollbars(*args, **kwargs)

    def IsScrollbarAlwaysShown(*args, **kwargs):
        """IsScrollbarAlwaysShown(self, int orient) -> bool"""
        return __core.Window_IsScrollbarAlwaysShown(*args, **kwargs)

    def SetHelpText(*args, **kwargs):
        """
        SetHelpText(self, String text)

        Sets the help text to be used as context-sensitive help for this
        window.  Note that the text is actually stored by the current
        `wx.HelpProvider` implementation, and not in the window object itself.
        """
        return __core.Window_SetHelpText(*args, **kwargs)

    def SetHelpTextForId(*args, **kwargs):
        """
        SetHelpTextForId(self, String text)

        Associate this help text with all windows with the same id as this
        one.
        """
        return __core.Window_SetHelpTextForId(*args, **kwargs)

    SetHelpTextForId = wx.deprecated(SetHelpTextForId,
                                                       'Use wx.HelpProvider.Get().AddHelp(id, text)') 
    def GetHelpTextAtPoint(*args, **kwargs):
        """
        GetHelpTextAtPoint(self, Point pt, wxHelpEvent::Origin origin) -> String

        Get the help string associated with the given position in this window.

        Notice that pt may be invalid if event origin is keyboard or unknown
        and this method should return the global window help text then

        """
        return __core.Window_GetHelpTextAtPoint(*args, **kwargs)

    def GetHelpText(*args, **kwargs):
        """
        GetHelpText(self) -> String

        Gets the help text to be used as context-sensitive help for this
        window.  Note that the text is actually stored by the current
        `wx.HelpProvider` implementation, and not in the window object itself.
        """
        return __core.Window_GetHelpText(*args, **kwargs)

    def SetToolTipString(*args, **kwargs):
        """
        SetToolTipString(self, String tip)

        Attach a tooltip to the window.
        """
        return __core.Window_SetToolTipString(*args, **kwargs)

    def SetToolTip(*args, **kwargs):
        """
        SetToolTip(self, ToolTip tip)

        Attach a tooltip to the window.
        """
        return __core.Window_SetToolTip(*args, **kwargs)

    def UnsetToolTip(*args, **kwargs):
        """UnsetToolTip(self)"""
        return __core.Window_UnsetToolTip(*args, **kwargs)

    def GetToolTip(*args, **kwargs):
        """
        GetToolTip(self) -> ToolTip

        get the associated tooltip or None if none
        """
        return __core.Window_GetToolTip(*args, **kwargs)

    def GetToolTipString(self):
        tip = self.GetToolTip()
        if tip:
            return tip.GetTip()
        else:
            return None

    ToolTipString = property(GetToolTipString, SetToolTipString)

    def SetDropTarget(*args, **kwargs):
        """
        SetDropTarget(self, DropTarget dropTarget)

        Associates a drop target with this window.  If the window already has
        a drop target, it is deleted.
        """
        return __core.Window_SetDropTarget(*args, **kwargs)

    def GetDropTarget(*args, **kwargs):
        """
        GetDropTarget(self) -> DropTarget

        Returns the associated drop target, which may be None.
        """
        return __core.Window_GetDropTarget(*args, **kwargs)

    def DragAcceptFiles(*args, **kwargs):
        """
        DragAcceptFiles(self, bool accept)

        Enables or disables eligibility for drop file events, EVT_DROP_FILES.
        """
        return __core.Window_DragAcceptFiles(*args, **kwargs)

    def SetConstraints(*args, **kwargs):
        """
        SetConstraints(self, LayoutConstraints constraints)

        Sets the window to have the given layout constraints. If an existing
        layout constraints object is already owned by the window, it will be
        deleted.  Pass None to disassociate and delete the window's current
        constraints.

        You must call SetAutoLayout to tell a window to use the constraints
        automatically in its default EVT_SIZE handler; otherwise, you must
        handle EVT_SIZE yourself and call Layout() explicitly. When setting
        both a wx.LayoutConstraints and a wx.Sizer, only the sizer will have
        effect.
        """
        return __core.Window_SetConstraints(*args, **kwargs)

    def GetConstraints(*args, **kwargs):
        """
        GetConstraints(self) -> LayoutConstraints

        Returns a pointer to the window's layout constraints, or None if there
        are none.
        """
        return __core.Window_GetConstraints(*args, **kwargs)

    def SetAutoLayout(*args, **kwargs):
        """
        SetAutoLayout(self, bool autoLayout)

        Determines whether the Layout function will be called automatically
        when the window is resized.  lease note that this only happens for the
        windows usually used to contain children, namely `wx.Panel` and
        `wx.TopLevelWindow` (and the classes deriving from them).

        This method is called implicitly by `SetSizer` but if you use
        `SetConstraints` you should call it manually or otherwise the window
        layout won't be correctly updated when its size changes.
        """
        return __core.Window_SetAutoLayout(*args, **kwargs)

    def GetAutoLayout(*args, **kwargs):
        """
        GetAutoLayout(self) -> bool

        Returns the current autoLayout setting
        """
        return __core.Window_GetAutoLayout(*args, **kwargs)

    def Layout(*args, **kwargs):
        """
        Layout(self) -> bool

        Invokes the constraint-based layout algorithm or the sizer-based
        algorithm for this window.  See SetAutoLayout: when auto layout is on,
        this function gets called automatically by the default EVT_SIZE
        handler when the window is resized.
        """
        return __core.Window_Layout(*args, **kwargs)

    def SetSizer(*args, **kwargs):
        """
        SetSizer(self, Sizer sizer, bool deleteOld=True)

        Sets the window to have the given layout sizer. The window will then
        own the object, and will take care of its deletion. If an existing
        layout sizer object is already owned by the window, it will be deleted
        if the deleteOld parameter is true. Note that this function will also
        call SetAutoLayout implicitly with a True parameter if the sizer is
        non-None, and False otherwise.
        """
        return __core.Window_SetSizer(*args, **kwargs)

    def SetSizerAndFit(*args, **kwargs):
        """
        SetSizerAndFit(self, Sizer sizer, bool deleteOld=True)

        The same as SetSizer, except it also sets the size hints for the
        window based on the sizer's minimum size.
        """
        return __core.Window_SetSizerAndFit(*args, **kwargs)

    def GetSizer(*args, **kwargs):
        """
        GetSizer(self) -> Sizer

        Return the sizer associated with the window by a previous call to
        SetSizer or None if there isn't one.
        """
        return __core.Window_GetSizer(*args, **kwargs)

    def SetContainingSizer(*args, **kwargs):
        """
        SetContainingSizer(self, Sizer sizer)

        This normally does not need to be called by application code. It is
        called internally when a window is added to a sizer, and is used so
        the window can remove itself from the sizer when it is destroyed.
        """
        return __core.Window_SetContainingSizer(*args, **kwargs)

    def GetContainingSizer(*args, **kwargs):
        """
        GetContainingSizer(self) -> Sizer

        Return the sizer that this window is a member of, if any, otherwise None.
        """
        return __core.Window_GetContainingSizer(*args, **kwargs)

    def InheritAttributes(*args, **kwargs):
        """
        InheritAttributes(self)

        This function is (or should be, in case of custom controls) called
        during window creation to intelligently set up the window visual
        attributes, that is the font and the foreground and background
        colours.

        By 'intelligently' the following is meant: by default, all windows use
        their own default attributes. However if some of the parent's
        attributes are explicitly changed (that is, using SetFont and not
        SetOwnFont) and if the corresponding attribute hadn't been
        explicitly set for this window itself, then this window takes the same
        value as used by the parent. In addition, if the window overrides
        ShouldInheritColours to return false, the colours will not be changed
        no matter what and only the font might.

        This rather complicated logic is necessary in order to accommodate the
        different usage scenarios. The most common one is when all default
        attributes are used and in this case, nothing should be inherited as
        in modern GUIs different controls use different fonts (and colours)
        than their siblings so they can't inherit the same value from the
        parent. However it was also deemed desirable to allow to simply change
        the attributes of all children at once by just changing the font or
        colour of their common parent, hence in this case we do inherit the
        parents attributes.

        """
        return __core.Window_InheritAttributes(*args, **kwargs)

    def ShouldInheritColours(*args, **kwargs):
        """
        ShouldInheritColours(self) -> bool

        Return true from here to allow the colours of this window to be
        changed by InheritAttributes, returning false forbids inheriting them
        from the parent window.

        The base class version returns false, but this method is overridden in
        wxControl where it returns true.
        """
        return __core.Window_ShouldInheritColours(*args, **kwargs)

    def CanBeOutsideClientArea(*args, **kwargs):
        """CanBeOutsideClientArea(self) -> bool"""
        return __core.Window_CanBeOutsideClientArea(*args, **kwargs)

    def CanApplyThemeBorder(*args, **kwargs):
        """CanApplyThemeBorder(self) -> bool"""
        return __core.Window_CanApplyThemeBorder(*args, **kwargs)

    def GetMainWindowOfCompositeControl(*args, **kwargs):
        """GetMainWindowOfCompositeControl(self) -> Window"""
        return __core.Window_GetMainWindowOfCompositeControl(*args, **kwargs)

    def CanSetTransparent(*args, **kwargs):
        """
        CanSetTransparent(self) -> bool

        Returns ``True`` if the platform supports setting the transparency for
        this window.  Note that this method will err on the side of caution,
        so it is possible that this will return ``False`` when it is in fact
        possible to set the transparency.

        NOTE: On X-windows systems the X server must have the composite
        extension loaded, and there must be a composite manager program (such
        as xcompmgr) running.
        """
        return __core.Window_CanSetTransparent(*args, **kwargs)

    def SetTransparent(*args, **kwargs):
        """
        SetTransparent(self, byte alpha) -> bool

        Attempt to set the transparency of this window to the ``alpha`` value,
        returns True on success.  The ``alpha`` value is an integer in the
        range of 0 to 255, where 0 is fully transparent and 255 is fully
        opaque.
        """
        return __core.Window_SetTransparent(*args, **kwargs)

    def PostCreate(self, pre):
        """
        Phase 3 of the 2-phase create <wink!>
        Call this method after precreating the window with the 2-phase create method.
        """
        self.this = pre.this
        self.thisown = pre.thisown
        pre.thisown = 0
        if hasattr(self, '_setOORInfo'):
            try:
                self._setOORInfo(self)
            except TypeError:
                pass
        if hasattr(self, '_setCallbackInfo'):
            try:
                self._setCallbackInfo(self, pre.__class__)
            except TypeError:
                pass

    AcceleratorTable = property(GetAcceleratorTable,SetAcceleratorTable,doc="See `GetAcceleratorTable` and `SetAcceleratorTable`") 
    AutoLayout = property(GetAutoLayout,SetAutoLayout,doc="See `GetAutoLayout` and `SetAutoLayout`") 
    BackgroundColour = property(GetBackgroundColour,SetBackgroundColour,doc="See `GetBackgroundColour` and `SetBackgroundColour`") 
    BackgroundStyle = property(GetBackgroundStyle,SetBackgroundStyle,doc="See `GetBackgroundStyle` and `SetBackgroundStyle`") 
    EffectiveMinSize = property(GetEffectiveMinSize,doc="See `GetEffectiveMinSize`") 
    BestSize = property(GetBestSize,doc="See `GetBestSize`") 
    BestVirtualSize = property(GetBestVirtualSize,doc="See `GetBestVirtualSize`") 
    Border = property(GetBorder,doc="See `GetBorder`") 
    Caret = property(GetCaret,SetCaret,doc="See `GetCaret` and `SetCaret`") 
    CharHeight = property(GetCharHeight,doc="See `GetCharHeight`") 
    CharWidth = property(GetCharWidth,doc="See `GetCharWidth`") 
    Children = property(GetChildren,doc="See `GetChildren`") 
    ClientAreaOrigin = property(GetClientAreaOrigin,doc="See `GetClientAreaOrigin`") 
    ClientRect = property(GetClientRect,SetClientRect,doc="See `GetClientRect` and `SetClientRect`") 
    ClientSize = property(GetClientSize,SetClientSize,doc="See `GetClientSize` and `SetClientSize`") 
    Constraints = property(GetConstraints,SetConstraints,doc="See `GetConstraints` and `SetConstraints`") 
    ContainingSizer = property(GetContainingSizer,SetContainingSizer,doc="See `GetContainingSizer` and `SetContainingSizer`") 
    Cursor = property(GetCursor,SetCursor,doc="See `GetCursor` and `SetCursor`") 
    DefaultAttributes = property(GetDefaultAttributes,doc="See `GetDefaultAttributes`") 
    DropTarget = property(GetDropTarget,SetDropTarget,doc="See `GetDropTarget` and `SetDropTarget`") 
    EventHandler = property(GetEventHandler,SetEventHandler,doc="See `GetEventHandler` and `SetEventHandler`") 
    ExtraStyle = property(GetExtraStyle,SetExtraStyle,doc="See `GetExtraStyle` and `SetExtraStyle`") 
    Font = property(GetFont,SetFont,doc="See `GetFont` and `SetFont`") 
    ForegroundColour = property(GetForegroundColour,SetForegroundColour,doc="See `GetForegroundColour` and `SetForegroundColour`") 
    GrandParent = property(GetGrandParent,doc="See `GetGrandParent`") 
    TopLevelParent = property(GetTopLevelParent,doc="See `GetTopLevelParent`") 
    Handle = property(GetHandle,doc="See `GetHandle`") 
    HelpText = property(GetHelpText,SetHelpText,doc="See `GetHelpText` and `SetHelpText`") 
    Id = property(GetId,SetId,doc="See `GetId` and `SetId`") 
    Label = property(GetLabel,SetLabel,doc="See `GetLabel` and `SetLabel`") 
    LayoutDirection = property(GetLayoutDirection,SetLayoutDirection,doc="See `GetLayoutDirection` and `SetLayoutDirection`") 
    MaxHeight = property(GetMaxHeight,doc="See `GetMaxHeight`") 
    MaxSize = property(GetMaxSize,SetMaxSize,doc="See `GetMaxSize` and `SetMaxSize`") 
    MaxWidth = property(GetMaxWidth,doc="See `GetMaxWidth`") 
    MinHeight = property(GetMinHeight,doc="See `GetMinHeight`") 
    MinSize = property(GetMinSize,SetMinSize,doc="See `GetMinSize` and `SetMinSize`") 
    MinWidth = property(GetMinWidth,doc="See `GetMinWidth`") 
    Name = property(GetName,SetName,doc="See `GetName` and `SetName`") 
    Parent = property(GetParent,doc="See `GetParent`") 
    Position = property(GetPosition,SetPosition,doc="See `GetPosition` and `SetPosition`") 
    Rect = property(GetRect,SetRect,doc="See `GetRect` and `SetRect`") 
    ScreenPosition = property(GetScreenPosition,doc="See `GetScreenPosition`") 
    ScreenRect = property(GetScreenRect,doc="See `GetScreenRect`") 
    Size = property(GetSize,SetSize,doc="See `GetSize` and `SetSize`") 
    Sizer = property(GetSizer,SetSizer,doc="See `GetSizer` and `SetSizer`") 
    ThemeEnabled = property(GetThemeEnabled,SetThemeEnabled,doc="See `GetThemeEnabled` and `SetThemeEnabled`") 
    ToolTip = property(GetToolTip,SetToolTip,doc="See `GetToolTip` and `SetToolTip`") 
    UpdateClientRect = property(GetUpdateClientRect,doc="See `GetUpdateClientRect`") 
    UpdateRegion = property(GetUpdateRegion,doc="See `GetUpdateRegion`") 
    Validator = property(GetValidator,SetValidator,doc="See `GetValidator` and `SetValidator`") 
    VirtualSize = property(GetVirtualSize,SetVirtualSize,doc="See `GetVirtualSize` and `SetVirtualSize`") 
    WindowStyle = property(GetWindowStyle,SetWindowStyle,doc="See `GetWindowStyle` and `SetWindowStyle`") 
    WindowStyleFlag = property(GetWindowStyleFlag,SetWindowStyleFlag,doc="See `GetWindowStyleFlag` and `SetWindowStyleFlag`") 
    WindowVariant = property(GetWindowVariant,SetWindowVariant,doc="See `GetWindowVariant` and `SetWindowVariant`") 
    Shown = property(IsShown,Show,doc="See `IsShown` and `Show`") 
    Enabled = property(IsEnabled,Enable,doc="See `IsEnabled` and `Enable`") 
    TopLevel = property(IsTopLevel,doc="See `IsTopLevel`") 
    GtkWidget = property(GetGtkWidget) 
    MinClientSize = property(GetMinClientSize,SetMinClientSize) 
    MaxClientSize = property(GetMaxClientSize,SetMaxClientSize) 
__core.Window_swigregister(Window)

def PreWindow(*args, **kwargs):
    """
    PreWindow() -> Window

    Precreate a Window for 2-phase creation.
    """
    val = __core.new_PreWindow(*args, **kwargs)
    return val

def Window_NewControlId(*args, **kwargs):
  """
    Window_NewControlId(int count=1) -> int

    Generate a unique id (or count of them consecutively), returns a
    valid id in the auto-id range or wxID_NONE if failed.  If using
    autoid management, it will mark the id as reserved until it is
    used (by assigning it to a wxWindowIDRef) or unreserved.
    """
  return __core.Window_NewControlId(*args, **kwargs)

def Window_UnreserveControlId(*args, **kwargs):
  """
    Window_UnreserveControlId(int id, int count=1)

    If an ID generated from NewControlId is not assigned to a wxWindowIDRef,
    it must be unreserved.
    """
  return __core.Window_UnreserveControlId(*args, **kwargs)

def Window_FindFocus(*args):
  """
    Window_FindFocus() -> Window

    Returns the window or control that currently has the keyboard focus,
    or None.
    """
  return __core.Window_FindFocus(*args)

def Window_GetCapture(*args):
  """
    Window_GetCapture() -> Window

    Returns the window which currently captures the mouse or None
    """
  return __core.Window_GetCapture(*args)

def Window_GetClassDefaultAttributes(*args, **kwargs):
  """
    Window_GetClassDefaultAttributes(int variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes

    Get the default attributes for this class.  This is useful if you want
    to use the same font or colour in your own control as in a standard
    control -- which is a much better idea than hard coding specific
    colours or fonts which might look completely out of place on the
    user's system, especially if it uses themes.

    The variant parameter is only relevant under Mac currently and is
    ignore under other platforms. Under Mac, it will change the size of
    the returned font. See `wx.Window.SetWindowVariant` for more about
    this.
    """
  return __core.Window_GetClassDefaultAttributes(*args, **kwargs)

def DLG_PNT(win, point_or_x, y=None):
    """
    Convenience function for converting a Point or (x,y) in
    dialog units to pixel units.
    """
    if y is None:
        return win.ConvertDialogPointToPixels(point_or_x)
    else:
        return win.ConvertDialogPointToPixels(wx.Point(point_or_x, y))

def DLG_SZE(win, size_width, height=None):
    """
    Convenience function for converting a Size or (w,h) in
    dialog units to pixel units.
    """
    if height is None:
        return win.ConvertDialogSizeToPixels(size_width)
    else:
        return win.ConvertDialogSizeToPixels(wx.Size(size_width, height))


def FindWindowById(*args, **kwargs):
  """
    FindWindowById(long id, Window parent=None) -> Window

    Find the first window in the application with the given id. If parent
    is None, the search will start from all top-level frames and dialog
    boxes; if non-None, the search will be limited to the given window
    hierarchy. The search is recursive in both cases.
    """
  return __core.FindWindowById(*args, **kwargs)

def FindWindowByName(*args, **kwargs):
  """
    FindWindowByName(String name, Window parent=None) -> Window

    Find a window by its name (as given in a window constructor or Create
    function call). If parent is None, the search will start from all
    top-level frames and dialog boxes; if non-None, the search will be
    limited to the given window hierarchy. The search is recursive in both
    cases.

    If no window with such name is found, wx.FindWindowByLabel is called.
    """
  return __core.FindWindowByName(*args, **kwargs)

def FindWindowByLabel(*args, **kwargs):
  """
    FindWindowByLabel(String label, Window parent=None) -> Window

    Find a window by its label. Depending on the type of window, the label
    may be a window title or panel item label. If parent is None, the
    search will start from all top-level frames and dialog boxes; if
    non-None, the search will be limited to the given window
    hierarchy. The search is recursive in both cases.
    """
  return __core.FindWindowByLabel(*args, **kwargs)

def Window_FromHWND(*args, **kwargs):
  """Window_FromHWND(Window parent, unsigned long _hWnd) -> Window"""
  return __core.Window_FromHWND(*args, **kwargs)

def GetTopLevelWindows(*args):
  """
    GetTopLevelWindows() -> WindowList

    Returns a list-like object of the the application's top-level windows, (frames,
    dialogs, etc.)
    """
  return __core.GetTopLevelWindows(*args)
class FrozenWindow(object):
    """
    A context manager to be used with Python 'with' statements
    that will freeze the given window for the duration of the
    with block.
    """
    def __init__(self, window):
        self._win = window
    def __enter__(self):
        self._win.Freeze()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._win.Thaw()

#---------------------------------------------------------------------------

class Validator(EvtHandler):
    """Proxy of C++ Validator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> Validator"""
        this = __core.new_Validator(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def Clone(*args, **kwargs):
        """Clone(self) -> Validator"""
        return __core.Validator_Clone(*args, **kwargs)

    def Validate(*args, **kwargs):
        """Validate(self, Window parent) -> bool"""
        return __core.Validator_Validate(*args, **kwargs)

    def TransferToWindow(*args, **kwargs):
        """TransferToWindow(self) -> bool"""
        return __core.Validator_TransferToWindow(*args, **kwargs)

    def TransferFromWindow(*args, **kwargs):
        """TransferFromWindow(self) -> bool"""
        return __core.Validator_TransferFromWindow(*args, **kwargs)

    def GetWindow(*args, **kwargs):
        """GetWindow(self) -> Window"""
        return __core.Validator_GetWindow(*args, **kwargs)

    def SetWindow(*args, **kwargs):
        """SetWindow(self, Window window)"""
        return __core.Validator_SetWindow(*args, **kwargs)

    def IsSilent(*args, **kwargs):
        """IsSilent() -> bool"""
        return __core.Validator_IsSilent(*args, **kwargs)

    IsSilent = staticmethod(IsSilent)
    def SuppressBellOnError(*args, **kwargs):
        """SuppressBellOnError(bool suppress=True)"""
        return __core.Validator_SuppressBellOnError(*args, **kwargs)

    SuppressBellOnError = staticmethod(SuppressBellOnError)
    def SetBellOnError(*args, **kwargs):
        """SetBellOnError(int doIt=True)"""
        return __core.Validator_SetBellOnError(*args, **kwargs)

    SetBellOnError = staticmethod(SetBellOnError)
    Window = property(GetWindow,SetWindow,doc="See `GetWindow` and `SetWindow`") 
__core.Validator_swigregister(Validator)

def Validator_IsSilent(*args):
  """Validator_IsSilent() -> bool"""
  return __core.Validator_IsSilent(*args)

def Validator_SuppressBellOnError(*args, **kwargs):
  """Validator_SuppressBellOnError(bool suppress=True)"""
  return __core.Validator_SuppressBellOnError(*args, **kwargs)

def Validator_SetBellOnError(*args, **kwargs):
  """Validator_SetBellOnError(int doIt=True)"""
  return __core.Validator_SetBellOnError(*args, **kwargs)

class PyValidator(Validator):
    """Proxy of C++ PyValidator class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> PyValidator"""
        this = __core.new_PyValidator(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self);PyValidator._setCallbackInfo(self, self, PyValidator)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class, int incref=1)"""
        return __core.PyValidator__setCallbackInfo(*args, **kwargs)

__core.PyValidator_swigregister(PyValidator)

#---------------------------------------------------------------------------

class MenuItemList_iterator(object):
    """This class serves as an iterator for a wxMenuItemList object."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_MenuItemList_iterator
    __del__ = lambda self : None;
    def next(*args, **kwargs):
        """next(self) -> MenuItem"""
        return __core.MenuItemList_iterator_next(*args, **kwargs)

__core.MenuItemList_iterator_swigregister(MenuItemList_iterator)
DefaultValidator = cvar.DefaultValidator

class MenuItemList(object):
    """
    This class wraps a wxList-based class and gives it a Python
    sequence-like interface.  Sequence operations supported are length,
    index access and iteration.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_MenuItemList
    __del__ = lambda self : None;
    def __len__(*args, **kwargs):
        """__len__(self) -> size_t"""
        return __core.MenuItemList___len__(*args, **kwargs)

    def __getitem__(*args, **kwargs):
        """__getitem__(self, size_t index) -> MenuItem"""
        return __core.MenuItemList___getitem__(*args, **kwargs)

    def __contains__(*args, **kwargs):
        """__contains__(self, MenuItem obj) -> bool"""
        return __core.MenuItemList___contains__(*args, **kwargs)

    def __iter__(*args, **kwargs):
        """__iter__(self) -> MenuItemList_iterator"""
        return __core.MenuItemList___iter__(*args, **kwargs)

    def index(*args, **kwargs):
        """index(self, MenuItem obj) -> int"""
        return __core.MenuItemList_index(*args, **kwargs)

    def __repr__(self):
        return "wxMenuItemList: " + repr(list(self))

__core.MenuItemList_swigregister(MenuItemList)

class Menu(EvtHandler):
    """Proxy of C++ Menu class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, String title=EmptyString, long style=0) -> Menu"""
        this = __core.new_Menu(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def Append(*args, **kwargs):
        """
        Append(self, int id, String text=EmptyString, String help=EmptyString, 
            int kind=ITEM_NORMAL) -> MenuItem
        """
        return __core.Menu_Append(*args, **kwargs)

    def AppendSeparator(*args, **kwargs):
        """AppendSeparator(self) -> MenuItem"""
        return __core.Menu_AppendSeparator(*args, **kwargs)

    def AppendCheckItem(*args, **kwargs):
        """AppendCheckItem(self, int id, String text, String help=EmptyString) -> MenuItem"""
        return __core.Menu_AppendCheckItem(*args, **kwargs)

    def AppendRadioItem(*args, **kwargs):
        """AppendRadioItem(self, int id, String text, String help=EmptyString) -> MenuItem"""
        return __core.Menu_AppendRadioItem(*args, **kwargs)

    def AppendMenu(*args, **kwargs):
        """AppendMenu(self, int id, String text, Menu submenu, String help=EmptyString) -> MenuItem"""
        return __core.Menu_AppendMenu(*args, **kwargs)

    def AppendSubMenu(*args, **kwargs):
        """AppendSubMenu(self, Menu submenu, String text, String help=EmptyString) -> MenuItem"""
        return __core.Menu_AppendSubMenu(*args, **kwargs)

    def AppendItem(*args, **kwargs):
        """AppendItem(self, MenuItem item) -> MenuItem"""
        return __core.Menu_AppendItem(*args, **kwargs)

    def InsertItem(*args, **kwargs):
        """InsertItem(self, size_t pos, MenuItem item) -> MenuItem"""
        return __core.Menu_InsertItem(*args, **kwargs)

    def PrependItem(*args, **kwargs):
        """PrependItem(self, MenuItem item) -> MenuItem"""
        return __core.Menu_PrependItem(*args, **kwargs)

    def Break(*args, **kwargs):
        """Break(self)"""
        return __core.Menu_Break(*args, **kwargs)

    def Insert(*args, **kwargs):
        """
        Insert(self, size_t pos, int id, String text=EmptyString, String help=EmptyString, 
            int kind=ITEM_NORMAL) -> MenuItem
        """
        return __core.Menu_Insert(*args, **kwargs)

    def InsertSeparator(*args, **kwargs):
        """InsertSeparator(self, size_t pos) -> MenuItem"""
        return __core.Menu_InsertSeparator(*args, **kwargs)

    def InsertCheckItem(*args, **kwargs):
        """InsertCheckItem(self, size_t pos, int id, String text, String help=EmptyString) -> MenuItem"""
        return __core.Menu_InsertCheckItem(*args, **kwargs)

    def InsertRadioItem(*args, **kwargs):
        """InsertRadioItem(self, size_t pos, int id, String text, String help=EmptyString) -> MenuItem"""
        return __core.Menu_InsertRadioItem(*args, **kwargs)

    def InsertMenu(*args, **kwargs):
        """InsertMenu(self, size_t pos, int id, String text, Menu submenu, String help=EmptyString) -> MenuItem"""
        return __core.Menu_InsertMenu(*args, **kwargs)

    def Prepend(*args, **kwargs):
        """
        Prepend(self, int id, String text=EmptyString, String help=EmptyString, 
            int kind=ITEM_NORMAL) -> MenuItem
        """
        return __core.Menu_Prepend(*args, **kwargs)

    def PrependSeparator(*args, **kwargs):
        """PrependSeparator(self) -> MenuItem"""
        return __core.Menu_PrependSeparator(*args, **kwargs)

    def PrependCheckItem(*args, **kwargs):
        """PrependCheckItem(self, int id, String text, String help=EmptyString) -> MenuItem"""
        return __core.Menu_PrependCheckItem(*args, **kwargs)

    def PrependRadioItem(*args, **kwargs):
        """PrependRadioItem(self, int id, String text, String help=EmptyString) -> MenuItem"""
        return __core.Menu_PrependRadioItem(*args, **kwargs)

    def PrependMenu(*args, **kwargs):
        """PrependMenu(self, int id, String text, Menu submenu, String help=EmptyString) -> MenuItem"""
        return __core.Menu_PrependMenu(*args, **kwargs)

    def Remove(*args, **kwargs):
        """Remove(self, int id) -> MenuItem"""
        return __core.Menu_Remove(*args, **kwargs)

    def RemoveItem(self, item):
        """RemoveItem(self, MenuItem item) -> MenuItem"""
        #// The return object is always the parameter, so return that 
        #// proxy instead of the new one
        val = _core_.Menu_RemoveItem(self, item)
        item.this.own(val.this.own())
        val.this.disown()
        return item


    def Delete(*args, **kwargs):
        """Delete(self, int id) -> bool"""
        return __core.Menu_Delete(*args, **kwargs)

    def DeleteItem(*args, **kwargs):
        """DeleteItem(self, MenuItem item) -> bool"""
        return __core.Menu_DeleteItem(*args, **kwargs)

    def Destroy(*args, **kwargs):
        """
        Destroy(self)

        Deletes the C++ object this Python object is a proxy for.
        """
        args[0].this.own(False)
        return __core.Menu_Destroy(*args, **kwargs)

    def DestroyId(*args, **kwargs):
        """DestroyId(self, int id) -> bool"""
        return __core.Menu_DestroyId(*args, **kwargs)

    def DestroyItem(*args, **kwargs):
        """DestroyItem(self, MenuItem item) -> bool"""
        return __core.Menu_DestroyItem(*args, **kwargs)

    def GetMenuItemCount(*args, **kwargs):
        """GetMenuItemCount(self) -> size_t"""
        return __core.Menu_GetMenuItemCount(*args, **kwargs)

    def GetMenuItems(*args, **kwargs):
        """GetMenuItems(self) -> MenuItemList"""
        return __core.Menu_GetMenuItems(*args, **kwargs)

    def FindItem(*args, **kwargs):
        """FindItem(self, String item) -> int"""
        return __core.Menu_FindItem(*args, **kwargs)

    def FindItemById(*args, **kwargs):
        """FindItemById(self, int id) -> MenuItem"""
        return __core.Menu_FindItemById(*args, **kwargs)

    def FindItemByPosition(*args, **kwargs):
        """FindItemByPosition(self, size_t position) -> MenuItem"""
        return __core.Menu_FindItemByPosition(*args, **kwargs)

    def Enable(*args, **kwargs):
        """Enable(self, int id, bool enable)"""
        return __core.Menu_Enable(*args, **kwargs)

    def IsEnabled(*args, **kwargs):
        """IsEnabled(self, int id) -> bool"""
        return __core.Menu_IsEnabled(*args, **kwargs)

    def Check(*args, **kwargs):
        """Check(self, int id, bool check)"""
        return __core.Menu_Check(*args, **kwargs)

    def IsChecked(*args, **kwargs):
        """IsChecked(self, int id) -> bool"""
        return __core.Menu_IsChecked(*args, **kwargs)

    def SetLabel(*args, **kwargs):
        """SetLabel(self, int id, String label)"""
        return __core.Menu_SetLabel(*args, **kwargs)

    def GetLabel(*args, **kwargs):
        """GetLabel(self, int id) -> String"""
        return __core.Menu_GetLabel(*args, **kwargs)

    def GetLabelText(*args, **kwargs):
        """GetLabelText(self, int itemid) -> String"""
        return __core.Menu_GetLabelText(*args, **kwargs)

    def SetHelpString(*args, **kwargs):
        """SetHelpString(self, int id, String helpString)"""
        return __core.Menu_SetHelpString(*args, **kwargs)

    def GetHelpString(*args, **kwargs):
        """GetHelpString(self, int id) -> String"""
        return __core.Menu_GetHelpString(*args, **kwargs)

    def SetTitle(*args, **kwargs):
        """SetTitle(self, String title)"""
        return __core.Menu_SetTitle(*args, **kwargs)

    def GetTitle(*args, **kwargs):
        """GetTitle(self) -> String"""
        return __core.Menu_GetTitle(*args, **kwargs)

    def SetEventHandler(*args, **kwargs):
        """SetEventHandler(self, EvtHandler handler)"""
        return __core.Menu_SetEventHandler(*args, **kwargs)

    def GetEventHandler(*args, **kwargs):
        """GetEventHandler(self) -> EvtHandler"""
        return __core.Menu_GetEventHandler(*args, **kwargs)

    def SetInvokingWindow(*args, **kwargs):
        """SetInvokingWindow(self, Window win)"""
        return __core.Menu_SetInvokingWindow(*args, **kwargs)

    def GetInvokingWindow(*args, **kwargs):
        """GetInvokingWindow(self) -> Window"""
        return __core.Menu_GetInvokingWindow(*args, **kwargs)

    def GetWindow(*args, **kwargs):
        """GetWindow(self) -> Window"""
        return __core.Menu_GetWindow(*args, **kwargs)

    def GetStyle(*args, **kwargs):
        """GetStyle(self) -> long"""
        return __core.Menu_GetStyle(*args, **kwargs)

    def UpdateUI(*args, **kwargs):
        """UpdateUI(self, EvtHandler source=None)"""
        return __core.Menu_UpdateUI(*args, **kwargs)

    def GetMenuBar(*args, **kwargs):
        """GetMenuBar(self) -> MenuBar"""
        return __core.Menu_GetMenuBar(*args, **kwargs)

    def Attach(*args, **kwargs):
        """Attach(self, wxMenuBarBase menubar)"""
        return __core.Menu_Attach(*args, **kwargs)

    def Detach(*args, **kwargs):
        """Detach(self)"""
        return __core.Menu_Detach(*args, **kwargs)

    def IsAttached(*args, **kwargs):
        """IsAttached(self) -> bool"""
        return __core.Menu_IsAttached(*args, **kwargs)

    def SetParent(*args, **kwargs):
        """SetParent(self, Menu parent)"""
        return __core.Menu_SetParent(*args, **kwargs)

    def GetParent(*args, **kwargs):
        """GetParent(self) -> Menu"""
        return __core.Menu_GetParent(*args, **kwargs)

    EventHandler = property(GetEventHandler,SetEventHandler,doc="See `GetEventHandler` and `SetEventHandler`") 
    HelpString = property(GetHelpString,SetHelpString,doc="See `GetHelpString` and `SetHelpString`") 
    InvokingWindow = property(GetInvokingWindow,SetInvokingWindow,doc="See `GetInvokingWindow` and `SetInvokingWindow`") 
    MenuBar = property(GetMenuBar,doc="See `GetMenuBar`") 
    MenuItemCount = property(GetMenuItemCount,doc="See `GetMenuItemCount`") 
    MenuItems = property(GetMenuItems,doc="See `GetMenuItems`") 
    Parent = property(GetParent,SetParent,doc="See `GetParent` and `SetParent`") 
    Style = property(GetStyle,doc="See `GetStyle`") 
    Title = property(GetTitle,SetTitle,doc="See `GetTitle` and `SetTitle`") 
__core.Menu_swigregister(Menu)

#---------------------------------------------------------------------------

class MenuBar(Window):
    """Proxy of C++ MenuBar class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self, long style=0) -> MenuBar"""
        this = __core.new_MenuBar(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def Append(*args, **kwargs):
        """Append(self, Menu menu, String title) -> bool"""
        return __core.MenuBar_Append(*args, **kwargs)

    def Insert(*args, **kwargs):
        """Insert(self, size_t pos, Menu menu, String title) -> bool"""
        return __core.MenuBar_Insert(*args, **kwargs)

    def GetMenuCount(*args, **kwargs):
        """GetMenuCount(self) -> size_t"""
        return __core.MenuBar_GetMenuCount(*args, **kwargs)

    def GetMenu(*args, **kwargs):
        """GetMenu(self, size_t pos) -> Menu"""
        return __core.MenuBar_GetMenu(*args, **kwargs)

    def Replace(*args, **kwargs):
        """Replace(self, size_t pos, Menu menu, String title) -> Menu"""
        return __core.MenuBar_Replace(*args, **kwargs)

    def Remove(*args, **kwargs):
        """Remove(self, size_t pos) -> Menu"""
        return __core.MenuBar_Remove(*args, **kwargs)

    def EnableTop(*args, **kwargs):
        """EnableTop(self, size_t pos, bool enable)"""
        return __core.MenuBar_EnableTop(*args, **kwargs)

    def IsEnabledTop(*args, **kwargs):
        """IsEnabledTop(self, size_t pos) -> bool"""
        return __core.MenuBar_IsEnabledTop(*args, **kwargs)

    def SetMenuLabel(*args, **kwargs):
        """SetMenuLabel(self, size_t pos, String label)"""
        return __core.MenuBar_SetMenuLabel(*args, **kwargs)

    def GetMenuLabel(*args, **kwargs):
        """GetMenuLabel(self, size_t pos) -> String"""
        return __core.MenuBar_GetMenuLabel(*args, **kwargs)

    SetLabelTop = SetMenuLabel
    GetLabelTop = GetMenuLabel    

    def GetMenuLabelText(*args, **kwargs):
        """GetMenuLabelText(self, size_t pos) -> String"""
        return __core.MenuBar_GetMenuLabelText(*args, **kwargs)

    def FindMenuItem(*args, **kwargs):
        """FindMenuItem(self, String menu, String item) -> int"""
        return __core.MenuBar_FindMenuItem(*args, **kwargs)

    def FindItemById(*args, **kwargs):
        """FindItemById(self, int id) -> MenuItem"""
        return __core.MenuBar_FindItemById(*args, **kwargs)

    def FindMenu(*args, **kwargs):
        """FindMenu(self, String title) -> int"""
        return __core.MenuBar_FindMenu(*args, **kwargs)

    def Enable(*args, **kwargs):
        """Enable(self, int id, bool enable)"""
        return __core.MenuBar_Enable(*args, **kwargs)

    def Check(*args, **kwargs):
        """Check(self, int id, bool check)"""
        return __core.MenuBar_Check(*args, **kwargs)

    def IsChecked(*args, **kwargs):
        """IsChecked(self, int id) -> bool"""
        return __core.MenuBar_IsChecked(*args, **kwargs)

    def IsEnabled(*args, **kwargs):
        """IsEnabled(self, int id) -> bool"""
        return __core.MenuBar_IsEnabled(*args, **kwargs)

    def SetLabel(*args, **kwargs):
        """SetLabel(self, int id, String label)"""
        return __core.MenuBar_SetLabel(*args, **kwargs)

    def GetLabel(*args, **kwargs):
        """GetLabel(self, int id) -> String"""
        return __core.MenuBar_GetLabel(*args, **kwargs)

    def SetHelpString(*args, **kwargs):
        """SetHelpString(self, int id, String helpString)"""
        return __core.MenuBar_SetHelpString(*args, **kwargs)

    def GetHelpString(*args, **kwargs):
        """GetHelpString(self, int id) -> String"""
        return __core.MenuBar_GetHelpString(*args, **kwargs)

    def GetFrame(*args, **kwargs):
        """GetFrame(self) -> wxFrame"""
        return __core.MenuBar_GetFrame(*args, **kwargs)

    def IsAttached(*args, **kwargs):
        """IsAttached(self) -> bool"""
        return __core.MenuBar_IsAttached(*args, **kwargs)

    def Attach(*args, **kwargs):
        """Attach(self, wxFrame frame)"""
        return __core.MenuBar_Attach(*args, **kwargs)

    def Detach(*args, **kwargs):
        """Detach(self)"""
        return __core.MenuBar_Detach(*args, **kwargs)

    def UpdateMenus(*args, **kwargs):
        """UpdateMenus(self)"""
        return __core.MenuBar_UpdateMenus(*args, **kwargs)

    def SetAutoWindowMenu(*args, **kwargs):
        """SetAutoWindowMenu(bool enable)"""
        return __core.MenuBar_SetAutoWindowMenu(*args, **kwargs)

    SetAutoWindowMenu = staticmethod(SetAutoWindowMenu)
    def GetAutoWindowMenu(*args, **kwargs):
        """GetAutoWindowMenu() -> bool"""
        return __core.MenuBar_GetAutoWindowMenu(*args, **kwargs)

    GetAutoWindowMenu = staticmethod(GetAutoWindowMenu)
    def MacSetCommonMenuBar(*args, **kwargs):
        """MacSetCommonMenuBar(MenuBar menubar)"""
        return __core.MenuBar_MacSetCommonMenuBar(*args, **kwargs)

    MacSetCommonMenuBar = staticmethod(MacSetCommonMenuBar)
    def GetMenus(self):
        """Return a list of (menu, label) items for the menus in the MenuBar. """
        return [(self.GetMenu(i), self.GetLabelTop(i)) 
                for i in range(self.GetMenuCount())]
        
    def SetMenus(self, items):
        """Clear and add new menus to the MenuBar from a list of (menu, label) items. """
        for i in range(self.GetMenuCount()-1, -1, -1):
            self.Remove(i)
        for m, l in items:
            self.Append(m, l)

    Frame = property(GetFrame,doc="See `GetFrame`") 
    MenuCount = property(GetMenuCount,doc="See `GetMenuCount`") 
    Menus = property(GetMenus,SetMenus,doc="See `GetMenus` and `SetMenus`") 
__core.MenuBar_swigregister(MenuBar)

def MenuBar_SetAutoWindowMenu(*args, **kwargs):
  """MenuBar_SetAutoWindowMenu(bool enable)"""
  return __core.MenuBar_SetAutoWindowMenu(*args, **kwargs)

def MenuBar_GetAutoWindowMenu(*args):
  """MenuBar_GetAutoWindowMenu() -> bool"""
  return __core.MenuBar_GetAutoWindowMenu(*args)

def MenuBar_MacSetCommonMenuBar(*args, **kwargs):
  """MenuBar_MacSetCommonMenuBar(MenuBar menubar)"""
  return __core.MenuBar_MacSetCommonMenuBar(*args, **kwargs)

#---------------------------------------------------------------------------

class MenuItem(Object):
    """Proxy of C++ MenuItem class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Menu parentMenu=None, int id=ID_SEPARATOR, String text=EmptyString, 
            String help=EmptyString, int kind=ITEM_NORMAL, 
            Menu subMenu=None) -> MenuItem
        """
        this = __core.new_MenuItem(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_MenuItem
    __del__ = lambda self : None;
    def Destroy(self): pass 
    def GetMenu(*args, **kwargs):
        """GetMenu(self) -> Menu"""
        return __core.MenuItem_GetMenu(*args, **kwargs)

    def SetMenu(*args, **kwargs):
        """SetMenu(self, Menu menu)"""
        return __core.MenuItem_SetMenu(*args, **kwargs)

    def SetId(*args, **kwargs):
        """SetId(self, int id)"""
        return __core.MenuItem_SetId(*args, **kwargs)

    def GetId(*args, **kwargs):
        """GetId(self) -> int"""
        return __core.MenuItem_GetId(*args, **kwargs)

    def IsSeparator(*args, **kwargs):
        """IsSeparator(self) -> bool"""
        return __core.MenuItem_IsSeparator(*args, **kwargs)

    def SetItemLabel(*args, **kwargs):
        """SetItemLabel(self, String str)"""
        return __core.MenuItem_SetItemLabel(*args, **kwargs)

    def GetItemLabel(*args, **kwargs):
        """GetItemLabel(self) -> String"""
        return __core.MenuItem_GetItemLabel(*args, **kwargs)

    def GetItemLabelText(*args, **kwargs):
        """GetItemLabelText(self) -> String"""
        return __core.MenuItem_GetItemLabelText(*args, **kwargs)

    def GetLabelText(*args, **kwargs):
        """GetLabelText(String label) -> String"""
        return __core.MenuItem_GetLabelText(*args, **kwargs)

    GetLabelText = staticmethod(GetLabelText)
    GetLabel = GetItemLabelText
    GetText = GetItemLabel
    SetText = SetItemLabel
    GetLabelFromText = GetLabelText

    def GetKind(*args, **kwargs):
        """GetKind(self) -> int"""
        return __core.MenuItem_GetKind(*args, **kwargs)

    def SetKind(*args, **kwargs):
        """SetKind(self, int kind)"""
        return __core.MenuItem_SetKind(*args, **kwargs)

    def SetCheckable(*args, **kwargs):
        """SetCheckable(self, bool checkable)"""
        return __core.MenuItem_SetCheckable(*args, **kwargs)

    def IsCheckable(*args, **kwargs):
        """IsCheckable(self) -> bool"""
        return __core.MenuItem_IsCheckable(*args, **kwargs)

    def IsSubMenu(*args, **kwargs):
        """IsSubMenu(self) -> bool"""
        return __core.MenuItem_IsSubMenu(*args, **kwargs)

    def SetSubMenu(*args, **kwargs):
        """SetSubMenu(self, Menu menu)"""
        return __core.MenuItem_SetSubMenu(*args, **kwargs)

    def GetSubMenu(*args, **kwargs):
        """GetSubMenu(self) -> Menu"""
        return __core.MenuItem_GetSubMenu(*args, **kwargs)

    def Enable(*args, **kwargs):
        """Enable(self, bool enable=True)"""
        return __core.MenuItem_Enable(*args, **kwargs)

    def IsEnabled(*args, **kwargs):
        """IsEnabled(self) -> bool"""
        return __core.MenuItem_IsEnabled(*args, **kwargs)

    def Check(*args, **kwargs):
        """Check(self, bool check=True)"""
        return __core.MenuItem_Check(*args, **kwargs)

    def IsChecked(*args, **kwargs):
        """IsChecked(self) -> bool"""
        return __core.MenuItem_IsChecked(*args, **kwargs)

    def Toggle(*args, **kwargs):
        """Toggle(self)"""
        return __core.MenuItem_Toggle(*args, **kwargs)

    def SetHelp(*args, **kwargs):
        """SetHelp(self, String str)"""
        return __core.MenuItem_SetHelp(*args, **kwargs)

    def GetHelp(*args, **kwargs):
        """GetHelp(self) -> String"""
        return __core.MenuItem_GetHelp(*args, **kwargs)

    def GetAccel(*args, **kwargs):
        """GetAccel(self) -> AcceleratorEntry"""
        return __core.MenuItem_GetAccel(*args, **kwargs)

    def SetAccel(*args, **kwargs):
        """SetAccel(self, AcceleratorEntry accel)"""
        return __core.MenuItem_SetAccel(*args, **kwargs)

    def SetBitmap(*args, **kwargs):
        """SetBitmap(self, Bitmap bitmap)"""
        return __core.MenuItem_SetBitmap(*args, **kwargs)

    def GetBitmap(*args, **kwargs):
        """GetBitmap(self) -> Bitmap"""
        return __core.MenuItem_GetBitmap(*args, **kwargs)

    def SetFont(*args, **kwargs):
        """SetFont(self, Font font)"""
        return __core.MenuItem_SetFont(*args, **kwargs)

    def GetFont(*args, **kwargs):
        """GetFont(self) -> Font"""
        return __core.MenuItem_GetFont(*args, **kwargs)

    def SetTextColour(*args, **kwargs):
        """SetTextColour(self, Colour colText)"""
        return __core.MenuItem_SetTextColour(*args, **kwargs)

    def GetTextColour(*args, **kwargs):
        """GetTextColour(self) -> Colour"""
        return __core.MenuItem_GetTextColour(*args, **kwargs)

    def SetBackgroundColour(*args, **kwargs):
        """SetBackgroundColour(self, Colour colBack)"""
        return __core.MenuItem_SetBackgroundColour(*args, **kwargs)

    def GetBackgroundColour(*args, **kwargs):
        """GetBackgroundColour(self) -> Colour"""
        return __core.MenuItem_GetBackgroundColour(*args, **kwargs)

    def SetBitmaps(*args, **kwargs):
        """SetBitmaps(self, Bitmap bmpChecked, Bitmap bmpUnchecked=wxNullBitmap)"""
        return __core.MenuItem_SetBitmaps(*args, **kwargs)

    def SetDisabledBitmap(*args, **kwargs):
        """SetDisabledBitmap(self, Bitmap bmpDisabled)"""
        return __core.MenuItem_SetDisabledBitmap(*args, **kwargs)

    def GetDisabledBitmap(*args, **kwargs):
        """GetDisabledBitmap(self) -> Bitmap"""
        return __core.MenuItem_GetDisabledBitmap(*args, **kwargs)

    def SetMarginWidth(*args, **kwargs):
        """SetMarginWidth(self, int nWidth)"""
        return __core.MenuItem_SetMarginWidth(*args, **kwargs)

    def GetMarginWidth(*args, **kwargs):
        """GetMarginWidth(self) -> int"""
        return __core.MenuItem_GetMarginWidth(*args, **kwargs)

    def GetDefaultMarginWidth(*args, **kwargs):
        """GetDefaultMarginWidth() -> int"""
        return __core.MenuItem_GetDefaultMarginWidth(*args, **kwargs)

    GetDefaultMarginWidth = staticmethod(GetDefaultMarginWidth)
    def IsOwnerDrawn(*args, **kwargs):
        """IsOwnerDrawn(self) -> bool"""
        return __core.MenuItem_IsOwnerDrawn(*args, **kwargs)

    def SetOwnerDrawn(*args, **kwargs):
        """SetOwnerDrawn(self, bool ownerDrawn=True)"""
        return __core.MenuItem_SetOwnerDrawn(*args, **kwargs)

    Accel = property(GetAccel,SetAccel,doc="See `GetAccel` and `SetAccel`") 
    BackgroundColour = property(GetBackgroundColour,SetBackgroundColour,doc="See `GetBackgroundColour` and `SetBackgroundColour`") 
    Bitmap = property(GetBitmap,SetBitmap,doc="See `GetBitmap` and `SetBitmap`") 
    DisabledBitmap = property(GetDisabledBitmap,SetDisabledBitmap,doc="See `GetDisabledBitmap` and `SetDisabledBitmap`") 
    Font = property(GetFont,SetFont,doc="See `GetFont` and `SetFont`") 
    Help = property(GetHelp,SetHelp,doc="See `GetHelp` and `SetHelp`") 
    Id = property(GetId,SetId,doc="See `GetId` and `SetId`") 
    Kind = property(GetKind,SetKind,doc="See `GetKind` and `SetKind`") 
    Label = property(GetLabel,doc="See `GetLabel`") 
    MarginWidth = property(GetMarginWidth,SetMarginWidth,doc="See `GetMarginWidth` and `SetMarginWidth`") 
    Menu = property(GetMenu,SetMenu,doc="See `GetMenu` and `SetMenu`") 
    SubMenu = property(GetSubMenu,SetSubMenu,doc="See `GetSubMenu` and `SetSubMenu`") 
    Text = property(GetText,SetText,doc="See `GetText` and `SetText`") 
    TextColour = property(GetTextColour,SetTextColour,doc="See `GetTextColour` and `SetTextColour`") 
    ItemLabel = property(GetItemLabel,SetItemLabel) 
    ItemLabelText = property(GetItemLabelText) 
__core.MenuItem_swigregister(MenuItem)

def MenuItem_GetLabelText(*args, **kwargs):
  """MenuItem_GetLabelText(String label) -> String"""
  return __core.MenuItem_GetLabelText(*args, **kwargs)

def MenuItem_GetDefaultMarginWidth(*args):
  """MenuItem_GetDefaultMarginWidth() -> int"""
  return __core.MenuItem_GetDefaultMarginWidth(*args)

#---------------------------------------------------------------------------

ELLIPSIZE_FLAGS_NONE = __core.ELLIPSIZE_FLAGS_NONE
ELLIPSIZE_FLAGS_PROCESS_MNEMONICS = __core.ELLIPSIZE_FLAGS_PROCESS_MNEMONICS
ELLIPSIZE_FLAGS_EXPAND_TABS = __core.ELLIPSIZE_FLAGS_EXPAND_TABS
ELLIPSIZE_FLAGS_DEFAULT = __core.ELLIPSIZE_FLAGS_DEFAULT
ELLIPSIZE_NONE = __core.ELLIPSIZE_NONE
ELLIPSIZE_START = __core.ELLIPSIZE_START
ELLIPSIZE_MIDDLE = __core.ELLIPSIZE_MIDDLE
ELLIPSIZE_END = __core.ELLIPSIZE_END
class Control(Window):
    """
    This is the base class for a control or 'widget'.

    A control is generally a small window which processes user input
    and/or displays one or more item of data.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=0, Validator validator=DefaultValidator, 
            String name=ControlNameStr) -> Control

        Create a Control.  Normally you should only call this from a subclass'
        __init__ as a plain old wx.Control is not very useful.
        """
        this = __core.new_Control(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def Create(*args, **kwargs):
        """
        Create(self, Window parent, int id=-1, Point pos=DefaultPosition, 
            Size size=DefaultSize, long style=0, Validator validator=DefaultValidator, 
            String name=ControlNameStr) -> bool

        Do the 2nd phase and create the GUI control.
        """
        return __core.Control_Create(*args, **kwargs)

    def GetAlignment(*args, **kwargs):
        """
        GetAlignment(self) -> int

        Get the control alignment (left/right/centre, top/bottom/centre)
        """
        return __core.Control_GetAlignment(*args, **kwargs)

    def GetLabelText(*args, **kwargs):
        """
        GetLabelText(self) -> String

        Get just the text of the label, without mnemonic characters ('&')
        """
        return __core.Control_GetLabelText(*args, **kwargs)

    def SetLabelText(*args, **kwargs):
        """SetLabelText(self, String text)"""
        return __core.Control_SetLabelText(*args, **kwargs)

    def SetLabelMarkup(*args, **kwargs):
        """SetLabelMarkup(self, String markup) -> bool"""
        return __core.Control_SetLabelMarkup(*args, **kwargs)

    def Command(*args, **kwargs):
        """
        Command(self, CommandEvent event)

        Simulates the effect of the user issuing a command to the item.

        :see: `wx.CommandEvent`

        """
        return __core.Control_Command(*args, **kwargs)

    def RemoveMnemonics(*args, **kwargs):
        """
        RemoveMnemonics(String str) -> String

        removes the mnemonics characters
        """
        return __core.Control_RemoveMnemonics(*args, **kwargs)

    RemoveMnemonics = staticmethod(RemoveMnemonics)
    def EscapeMnemonics(*args, **kwargs):
        """
        EscapeMnemonics(String str) -> String

        escapes (by doubling them) the mnemonics
        """
        return __core.Control_EscapeMnemonics(*args, **kwargs)

    EscapeMnemonics = staticmethod(EscapeMnemonics)
    def FindAccelIndex(*args, **kwargs):
        """
        FindAccelIndex(String label) -> int

        Return the accel index in the string or -1 if none.
        """
        return __core.Control_FindAccelIndex(*args, **kwargs)

    FindAccelIndex = staticmethod(FindAccelIndex)
    def Ellipsize(*args, **kwargs):
        """Ellipsize(String label, DC dc, int mode, int maxWidth, int flags=ELLIPSIZE_FLAGS_DEFAULT) -> String"""
        return __core.Control_Ellipsize(*args, **kwargs)

    Ellipsize = staticmethod(Ellipsize)
    def GetCompositeControlsDefaultAttributes(*args, **kwargs):
        """GetCompositeControlsDefaultAttributes(int variant) -> VisualAttributes"""
        return __core.Control_GetCompositeControlsDefaultAttributes(*args, **kwargs)

    GetCompositeControlsDefaultAttributes = staticmethod(GetCompositeControlsDefaultAttributes)
    def GetClassDefaultAttributes(*args, **kwargs):
        """
        GetClassDefaultAttributes(int variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes

        Get the default attributes for this class.  This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        user's system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignore under other platforms. Under Mac, it will change the size of
        the returned font. See `wx.Window.SetWindowVariant` for more about
        this.
        """
        return __core.Control_GetClassDefaultAttributes(*args, **kwargs)

    GetClassDefaultAttributes = staticmethod(GetClassDefaultAttributes)
    Alignment = property(GetAlignment,doc="See `GetAlignment`") 
    LabelText = property(GetLabelText,SetLabelText,doc="See `GetLabelText`") 
__core.Control_swigregister(Control)
ControlNameStr = cvar.ControlNameStr

def PreControl(*args, **kwargs):
    """
    PreControl() -> Control

    Precreate a Control control for 2-phase creation
    """
    val = __core.new_PreControl(*args, **kwargs)
    return val

def Control_RemoveMnemonics(*args, **kwargs):
  """
    Control_RemoveMnemonics(String str) -> String

    removes the mnemonics characters
    """
  return __core.Control_RemoveMnemonics(*args, **kwargs)

def Control_EscapeMnemonics(*args, **kwargs):
  """
    Control_EscapeMnemonics(String str) -> String

    escapes (by doubling them) the mnemonics
    """
  return __core.Control_EscapeMnemonics(*args, **kwargs)

def Control_FindAccelIndex(*args, **kwargs):
  """
    Control_FindAccelIndex(String label) -> int

    Return the accel index in the string or -1 if none.
    """
  return __core.Control_FindAccelIndex(*args, **kwargs)

def Control_Ellipsize(*args, **kwargs):
  """Control_Ellipsize(String label, DC dc, int mode, int maxWidth, int flags=ELLIPSIZE_FLAGS_DEFAULT) -> String"""
  return __core.Control_Ellipsize(*args, **kwargs)

def Control_GetCompositeControlsDefaultAttributes(*args, **kwargs):
  """Control_GetCompositeControlsDefaultAttributes(int variant) -> VisualAttributes"""
  return __core.Control_GetCompositeControlsDefaultAttributes(*args, **kwargs)

def Control_GetClassDefaultAttributes(*args, **kwargs):
  """
    Control_GetClassDefaultAttributes(int variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes

    Get the default attributes for this class.  This is useful if you want
    to use the same font or colour in your own control as in a standard
    control -- which is a much better idea than hard coding specific
    colours or fonts which might look completely out of place on the
    user's system, especially if it uses themes.

    The variant parameter is only relevant under Mac currently and is
    ignore under other platforms. Under Mac, it will change the size of
    the returned font. See `wx.Window.SetWindowVariant` for more about
    this.
    """
  return __core.Control_GetClassDefaultAttributes(*args, **kwargs)

#---------------------------------------------------------------------------

class ItemContainer(object):
    """
    The wx.ItemContainer class defines an interface which is implemented
    by all controls which have string subitems, each of which may be
    selected, such as `wx.ListBox`, `wx.CheckListBox`, `wx.Choice` as well
    as `wx.ComboBox` which implements an extended interface deriving from
    this one.

    It defines the methods for accessing the control's items and although
    each of the derived classes implements them differently, they still
    all conform to the same interface.

    The items in a wx.ItemContainer have (non empty) string labels and,
    optionally, client data associated with them.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def Append(*args, **kwargs):
        """
        Append(self, String item, PyObject clientData=None) -> int

        Adds the item to the control, associating the given data with the item
        if not None.  The return value is the index of the newly added item
        which may be different from the last one if the control is sorted (e.g.
        has wx.LB_SORT or wx.CB_SORT style).
        """
        return __core.ItemContainer_Append(*args, **kwargs)

    def AppendItems(*args, **kwargs):
        """
        AppendItems(self, List strings)

        Apend several items at once to the control.  Notice that calling this
        method may be much faster than appending the items one by one if you
        need to add a lot of items.
        """
        return __core.ItemContainer_AppendItems(*args, **kwargs)

    def Insert(*args, **kwargs):
        """
        Insert(self, String item, int pos, PyObject clientData=None) -> int

        Insert an item into the control before the item at the ``pos`` index,
        optionally associating some data object with the item.
        """
        return __core.ItemContainer_Insert(*args, **kwargs)

    def InsertItems(*args, **kwargs):
        """
        InsertItems(self, List strings, int pos) --> int

        Inserts several items at once into the control.  Returns the index of
        the last item inserted.
        """
        return __core.ItemContainer_InsertItems(*args, **kwargs)

    def Set(*args, **kwargs):
        """
        Set(self, List strings)

        Replace all the items in the control
        """
        return __core.ItemContainer_Set(*args, **kwargs)

    def Clear(*args, **kwargs):
        """
        Clear(self)

        Removes all items from the control.
        """
        return __core.ItemContainer_Clear(*args, **kwargs)

    def Delete(*args, **kwargs):
        """
        Delete(self, int n)

        Deletes the item at the zero-based index 'n' from the control. Note
        that it is an error (signalled by a `wx.PyAssertionError` exception if
        enabled) to remove an item with the index negative or greater or equal
        than the number of items in the control.
        """
        return __core.ItemContainer_Delete(*args, **kwargs)

    def GetClientData(*args, **kwargs):
        """
        GetClientData(self, int n) -> PyObject

        Returns the client data associated with the given item, (if any.)
        """
        return __core.ItemContainer_GetClientData(*args, **kwargs)

    def SetClientData(*args, **kwargs):
        """
        SetClientData(self, int n, PyObject clientData)

        Associate the given client data with the item at position n.
        """
        return __core.ItemContainer_SetClientData(*args, **kwargs)

    def HasClientData(*args, **kwargs):
        """HasClientData(self) -> bool"""
        return __core.ItemContainer_HasClientData(*args, **kwargs)

    def GetCount(*args, **kwargs):
        """
        GetCount(self) -> int

        Returns the number of items in the control.
        """
        return __core.ItemContainer_GetCount(*args, **kwargs)

    def IsEmpty(*args, **kwargs):
        """
        IsEmpty(self) -> bool

        Returns True if the control is empty or False if it has some items.
        """
        return __core.ItemContainer_IsEmpty(*args, **kwargs)

    def GetString(*args, **kwargs):
        """
        GetString(self, int n) -> String

        Returns the label of the item with the given index.
        """
        return __core.ItemContainer_GetString(*args, **kwargs)

    def GetStrings(*args, **kwargs):
        """GetStrings(self) -> wxArrayString"""
        return __core.ItemContainer_GetStrings(*args, **kwargs)

    def IsSorted(*args, **kwargs):
        """IsSorted(self) -> bool"""
        return __core.ItemContainer_IsSorted(*args, **kwargs)

    def SetString(*args, **kwargs):
        """
        SetString(self, int n, String s)

        Sets the label for the given item.
        """
        return __core.ItemContainer_SetString(*args, **kwargs)

    def FindString(*args, **kwargs):
        """
        FindString(self, String s) -> int

        Finds an item whose label matches the given string.  Returns the
        zero-based position of the item, or ``wx.NOT_FOUND`` if the string was not
        found.
        """
        return __core.ItemContainer_FindString(*args, **kwargs)

    def SetSelection(*args, **kwargs):
        """
        SetSelection(self, int n)

        Sets the item at index 'n' to be the selected item.
        """
        return __core.ItemContainer_SetSelection(*args, **kwargs)

    def GetSelection(*args, **kwargs):
        """
        GetSelection(self) -> int

        Returns the index of the selected item or ``wx.NOT_FOUND`` if no item
        is selected.
        """
        return __core.ItemContainer_GetSelection(*args, **kwargs)

    def SetStringSelection(*args, **kwargs):
        """SetStringSelection(self, String s) -> bool"""
        return __core.ItemContainer_SetStringSelection(*args, **kwargs)

    def GetStringSelection(*args, **kwargs):
        """
        GetStringSelection(self) -> String

        Returns the label of the selected item or an empty string if no item
        is selected.
        """
        return __core.ItemContainer_GetStringSelection(*args, **kwargs)

    def Select(*args, **kwargs):
        """
        Select(self, int n)

        This is the same as `SetSelection` and exists only because it is
        slightly more natural for controls which support multiple selection.
        """
        return __core.ItemContainer_Select(*args, **kwargs)

    def GetItems(self):
        """Return a list of the strings in the control"""
        return [self.GetString(i) for i in xrange(self.GetCount())]
        
    def SetItems(self, items):
        """Clear and set the strings in the control from a list"""
        self.Clear()
        self.AppendItems(items)

    Count = property(GetCount,doc="See `GetCount`") 
    Items = property(GetItems,SetItems,doc="See `GetItems` and `SetItems`") 
    Selection = property(GetSelection,SetSelection,doc="See `GetSelection` and `SetSelection`") 
    StringSelection = property(GetStringSelection,SetStringSelection,doc="See `GetStringSelection` and `SetStringSelection`") 
    Strings = property(GetStrings,doc="See `GetStrings`") 
__core.ItemContainer_swigregister(ItemContainer)

#---------------------------------------------------------------------------

class ControlWithItems(Control,ItemContainer):
    """
    wx.ControlWithItems combines the ``wx.ItemContainer`` class with the
    wx.Control class, and is used for the base class of various controls
    that have items.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
__core.ControlWithItems_swigregister(ControlWithItems)

#---------------------------------------------------------------------------

TE_HT_UNKNOWN = __core.TE_HT_UNKNOWN
TE_HT_BEFORE = __core.TE_HT_BEFORE
TE_HT_ON_TEXT = __core.TE_HT_ON_TEXT
TE_HT_BELOW = __core.TE_HT_BELOW
TE_HT_BEYOND = __core.TE_HT_BEYOND
class TextEntryBase(object):
    """Proxy of C++ TextEntryBase class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_TextEntryBase
    __del__ = lambda self : None;
    def SetValue(*args, **kwargs):
        """
        SetValue(self, String value)

        Set the value in the text entry field.  Generates a text change event.
        """
        return __core.TextEntryBase_SetValue(*args, **kwargs)

    def ChangeValue(*args, **kwargs):
        """
        ChangeValue(self, String value)

        Set the value in the text entry field.  Does not generate a text change event.
        """
        return __core.TextEntryBase_ChangeValue(*args, **kwargs)

    def WriteText(*args, **kwargs):
        """
        WriteText(self, String text)

        Insert text at the current insertion point in the text field,
        replacing any text that is currently selected.
        """
        return __core.TextEntryBase_WriteText(*args, **kwargs)

    def AppendText(*args, **kwargs):
        """
        AppendText(self, String text)

        Add text to the end of the text field, without removing any existing
        text.  Will reset the selection if any.
        """
        return __core.TextEntryBase_AppendText(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """
        GetValue(self) -> String

        Returns the current value in the text field.
        """
        return __core.TextEntryBase_GetValue(*args, **kwargs)

    def GetRange(*args, **kwargs):
        """
        GetRange(self, long from, long to) -> String

        Returns a subset of the value in the text field.
        """
        return __core.TextEntryBase_GetRange(*args, **kwargs)

    GetString = wx.deprecated(GetRange, "Use `GetRange` instead.") 
    def IsEmpty(*args, **kwargs):
        """
        IsEmpty(self) -> bool

        Returns True if the value in the text field is empty.
        """
        return __core.TextEntryBase_IsEmpty(*args, **kwargs)

    def Replace(*args, **kwargs):
        """
        Replace(self, long from, long to, String value)

        Replaces the text between two positions with the given text.
        """
        return __core.TextEntryBase_Replace(*args, **kwargs)

    def Remove(*args, **kwargs):
        """
        Remove(self, long from, long to)

        Removes the text between two positions in the text field
        """
        return __core.TextEntryBase_Remove(*args, **kwargs)

    def Clear(*args, **kwargs):
        """
        Clear(self)

        Clear all text from the text field
        """
        return __core.TextEntryBase_Clear(*args, **kwargs)

    def RemoveSelection(*args, **kwargs):
        """RemoveSelection(self)"""
        return __core.TextEntryBase_RemoveSelection(*args, **kwargs)

    def Copy(*args, **kwargs):
        """
        Copy(self)

        Copies the selected text to the clipboard.
        """
        return __core.TextEntryBase_Copy(*args, **kwargs)

    def Cut(*args, **kwargs):
        """
        Cut(self)

        Copies the selected text to the clipboard and removes the selection.
        """
        return __core.TextEntryBase_Cut(*args, **kwargs)

    def Paste(*args, **kwargs):
        """
        Paste(self)

        Pastes text from the clipboard to the text field.
        """
        return __core.TextEntryBase_Paste(*args, **kwargs)

    def CanCopy(*args, **kwargs):
        """
        CanCopy(self) -> bool

        Returns True if the text field has a text selection to copy to the
        clipboard.
        """
        return __core.TextEntryBase_CanCopy(*args, **kwargs)

    def CanCut(*args, **kwargs):
        """
        CanCut(self) -> bool

        Returns True if the text field is editable and there is a text
        selection to copy to the clipboard.
        """
        return __core.TextEntryBase_CanCut(*args, **kwargs)

    def CanPaste(*args, **kwargs):
        """
        CanPaste(self) -> bool

        Returns True if the text field is editable and there is text on the
        clipboard that can be pasted into the text field.
        """
        return __core.TextEntryBase_CanPaste(*args, **kwargs)

    def Undo(*args, **kwargs):
        """
        Undo(self)

        Undoes the last edit in the text field
        """
        return __core.TextEntryBase_Undo(*args, **kwargs)

    def Redo(*args, **kwargs):
        """
        Redo(self)

        Redoes the last undo in the text field
        """
        return __core.TextEntryBase_Redo(*args, **kwargs)

    def CanUndo(*args, **kwargs):
        """
        CanUndo(self) -> bool

        Returns True if the text field is editable and the last edit can be
        undone.
        """
        return __core.TextEntryBase_CanUndo(*args, **kwargs)

    def CanRedo(*args, **kwargs):
        """
        CanRedo(self) -> bool

        Returns True if the text field is editable and the last undo can be
        redone.
        """
        return __core.TextEntryBase_CanRedo(*args, **kwargs)

    def SetInsertionPoint(*args, **kwargs):
        """
        SetInsertionPoint(self, long pos)

        Sets the insertion point in the combobox text field.
        """
        return __core.TextEntryBase_SetInsertionPoint(*args, **kwargs)

    def GetInsertionPoint(*args, **kwargs):
        """
        GetInsertionPoint(self) -> long

        Returns the insertion point for the combobox's text field.
        """
        return __core.TextEntryBase_GetInsertionPoint(*args, **kwargs)

    def SetInsertionPointEnd(*args, **kwargs):
        """
        SetInsertionPointEnd(self)

        Move the insertion point to the end of the current value.
        """
        return __core.TextEntryBase_SetInsertionPointEnd(*args, **kwargs)

    def GetLastPosition(*args, **kwargs):
        """
        GetLastPosition(self) -> long

        Returns the last position in the combobox text field.
        """
        return __core.TextEntryBase_GetLastPosition(*args, **kwargs)

    def SetSelection(*args, **kwargs):
        """
        SetSelection(self, long from, long to)

        Selects the text starting at the first position up to (but not
        including) the character at the last position.  If both parameters are
        -1 then all text in the control is selected.
        """
        return __core.TextEntryBase_SetSelection(*args, **kwargs)

    def SelectAll(*args, **kwargs):
        """
        SelectAll(self)

        Select all text in the text field.
        """
        return __core.TextEntryBase_SelectAll(*args, **kwargs)

    def HasSelection(*args, **kwargs):
        """
        HasSelection(self) -> bool

        Returns True if there is a non-empty selection in the text field.
        """
        return __core.TextEntryBase_HasSelection(*args, **kwargs)

    def GetStringSelection(*args, **kwargs):
        """
        GetStringSelection(self) -> String

        Returns the selected text.
        """
        return __core.TextEntryBase_GetStringSelection(*args, **kwargs)

    def GetSelection(*args, **kwargs):
        """
        GetSelection() -> (from, to)

        If the return values from and to are the same, there is no selection.
        """
        return __core.TextEntryBase_GetSelection(*args, **kwargs)

    Selection = property(GetSelection) 
    def AutoComplete(*args, **kwargs):
        """AutoComplete(self, wxArrayString choices) -> bool"""
        return __core.TextEntryBase_AutoComplete(*args, **kwargs)

    def AutoCompleteFileNames(*args, **kwargs):
        """AutoCompleteFileNames(self) -> bool"""
        return __core.TextEntryBase_AutoCompleteFileNames(*args, **kwargs)

    def AutoCompleteDirectories(*args, **kwargs):
        """AutoCompleteDirectories(self) -> bool"""
        return __core.TextEntryBase_AutoCompleteDirectories(*args, **kwargs)

    def IsEditable(*args, **kwargs):
        """IsEditable(self) -> bool"""
        return __core.TextEntryBase_IsEditable(*args, **kwargs)

    def SetEditable(*args, **kwargs):
        """SetEditable(self, bool editable)"""
        return __core.TextEntryBase_SetEditable(*args, **kwargs)

    def SetMaxLength(*args, **kwargs):
        """
        SetMaxLength(self, long len)

        Set the max number of characters which may be entered in a single line
        text control.
        """
        return __core.TextEntryBase_SetMaxLength(*args, **kwargs)

    def SetHint(*args, **kwargs):
        """SetHint(self, String hint) -> bool"""
        return __core.TextEntryBase_SetHint(*args, **kwargs)

    def GetHint(*args, **kwargs):
        """GetHint(self) -> String"""
        return __core.TextEntryBase_GetHint(*args, **kwargs)

    def SetMargins(*args, **kwargs):
        """SetMargins(self, Point pt) -> bool"""
        return __core.TextEntryBase_SetMargins(*args, **kwargs)

    def GetMargins(*args, **kwargs):
        """GetMargins(self) -> Point"""
        return __core.TextEntryBase_GetMargins(*args, **kwargs)

    InsertionPoint = property(GetInsertionPoint,SetInsertionPoint) 
    LastPosition = property(GetLastPosition) 
    Value = property(GetValue,SetValue) 
__core.TextEntryBase_swigregister(TextEntryBase)

class TextEntry(TextEntryBase):
    """Proxy of C++ TextEntry class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
__core.TextEntry_swigregister(TextEntry)

class TextAreaBase(object):
    """multiline text control specific methods"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_TextAreaBase
    __del__ = lambda self : None;
    def GetLineLength(*args, **kwargs):
        """GetLineLength(self, long lineNo) -> int"""
        return __core.TextAreaBase_GetLineLength(*args, **kwargs)

    def GetLineText(*args, **kwargs):
        """GetLineText(self, long lineNo) -> String"""
        return __core.TextAreaBase_GetLineText(*args, **kwargs)

    def GetNumberOfLines(*args, **kwargs):
        """GetNumberOfLines(self) -> int"""
        return __core.TextAreaBase_GetNumberOfLines(*args, **kwargs)

    def LoadFile(*args, **kwargs):
        """LoadFile(self, String file, int fileType=wxTEXT_TYPE_ANY) -> bool"""
        return __core.TextAreaBase_LoadFile(*args, **kwargs)

    def SaveFile(*args, **kwargs):
        """SaveFile(self, String file=wxEmptyString, int fileType=wxTEXT_TYPE_ANY) -> bool"""
        return __core.TextAreaBase_SaveFile(*args, **kwargs)

    def IsModified(*args, **kwargs):
        """IsModified(self) -> bool"""
        return __core.TextAreaBase_IsModified(*args, **kwargs)

    def MarkDirty(*args, **kwargs):
        """MarkDirty(self)"""
        return __core.TextAreaBase_MarkDirty(*args, **kwargs)

    def DiscardEdits(*args, **kwargs):
        """DiscardEdits(self)"""
        return __core.TextAreaBase_DiscardEdits(*args, **kwargs)

    def SetModified(*args, **kwargs):
        """SetModified(self, bool modified)"""
        return __core.TextAreaBase_SetModified(*args, **kwargs)

    def SetStyle(*args, **kwargs):
        """SetStyle(self, long start, long end, wxTextAttr style) -> bool"""
        return __core.TextAreaBase_SetStyle(*args, **kwargs)

    def GetStyle(*args, **kwargs):
        """GetStyle(self, long position, wxTextAttr style) -> bool"""
        return __core.TextAreaBase_GetStyle(*args, **kwargs)

    def SetDefaultStyle(*args, **kwargs):
        """SetDefaultStyle(self, wxTextAttr style) -> bool"""
        return __core.TextAreaBase_SetDefaultStyle(*args, **kwargs)

    def GetDefaultStyle(*args, **kwargs):
        """GetDefaultStyle(self) -> wxTextAttr"""
        return __core.TextAreaBase_GetDefaultStyle(*args, **kwargs)

    def XYToPosition(*args, **kwargs):
        """XYToPosition(self, long x, long y) -> long"""
        return __core.TextAreaBase_XYToPosition(*args, **kwargs)

    def PositionToXY(*args, **kwargs):
        """PositionToXY(long pos) -> (x, y)"""
        return __core.TextAreaBase_PositionToXY(*args, **kwargs)

    def PositionToCoords(*args, **kwargs):
        """PositionToCoords(self, long pos) -> Point"""
        return __core.TextAreaBase_PositionToCoords(*args, **kwargs)

    def ShowPosition(*args, **kwargs):
        """ShowPosition(self, long pos)"""
        return __core.TextAreaBase_ShowPosition(*args, **kwargs)

    def HitTest(*args, **kwargs):
        """
        HitTest(Point pt) -> (result, col, row)

        Find the row, col coresponding to the character at the point given in
        pixels. NB: pt is in device coords but is not adjusted for the client
        area origin nor scrolling.
        """
        return __core.TextAreaBase_HitTest(*args, **kwargs)

    def HitTestPos(*args, **kwargs):
        """
        HitTestPos(Point pt) -> (result, position)

        Find the character position in the text coresponding to the point
        given in pixels. NB: pt is in device coords but is not adjusted for
        the client area origin nor scrolling. 
        """
        return __core.TextAreaBase_HitTestPos(*args, **kwargs)

    DefaultStyle = property(GetDefaultStyle,SetDefaultStyle) 
    NumberOfLines = property(GetNumberOfLines) 
__core.TextAreaBase_swigregister(TextAreaBase)

class TextCtrlIface(TextAreaBase,TextEntryBase):
    """This class defines the wx.TextCtrl interface"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
__core.TextCtrlIface_swigregister(TextCtrlIface)

class TextCtrlBase(Control,TextAreaBase,TextEntry):
    """An abstract base class for wx.TextCtrl."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
__core.TextCtrlBase_swigregister(TextCtrlBase)

#---------------------------------------------------------------------------

class WithImages(object):
    """Proxy of C++ WithImages class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    NO_IMAGE = __core.WithImages_NO_IMAGE
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> WithImages"""
        this = __core.new_WithImages(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_WithImages
    __del__ = lambda self : None;
    def SetImageList(*args, **kwargs):
        """SetImageList(self, ImageList imageList)"""
        return __core.WithImages_SetImageList(*args, **kwargs)

    def AssignImageList(*args, **kwargs):
        """AssignImageList(self, ImageList imageList)"""
        return __core.WithImages_AssignImageList(*args, **kwargs)

    def GetImageList(*args, **kwargs):
        """GetImageList(self) -> ImageList"""
        return __core.WithImages_GetImageList(*args, **kwargs)

    ImageList = property(GetImageList,SetImageList,doc="See `GetImageList` and `SetImageList`") 
__core.WithImages_swigregister(WithImages)

#---------------------------------------------------------------------------

BK_DEFAULT = __core.BK_DEFAULT
BK_TOP = __core.BK_TOP
BK_BOTTOM = __core.BK_BOTTOM
BK_LEFT = __core.BK_LEFT
BK_RIGHT = __core.BK_RIGHT
BK_ALIGN_MASK = __core.BK_ALIGN_MASK
BK_BUTTONBAR = __core.BK_BUTTONBAR
TBK_BUTTONBAR = __core.TBK_BUTTONBAR
TBK_HORZ_LAYOUT = __core.TBK_HORZ_LAYOUT
BK_HITTEST_NOWHERE = __core.BK_HITTEST_NOWHERE
BK_HITTEST_ONICON = __core.BK_HITTEST_ONICON
BK_HITTEST_ONLABEL = __core.BK_HITTEST_ONLABEL
BK_HITTEST_ONITEM = __core.BK_HITTEST_ONITEM
BK_HITTEST_ONPAGE = __core.BK_HITTEST_ONPAGE
class BookCtrlBase(Control,WithImages):
    """Proxy of C++ BookCtrlBase class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def GetPageCount(*args, **kwargs):
        """GetPageCount(self) -> size_t"""
        return __core.BookCtrlBase_GetPageCount(*args, **kwargs)

    def GetPage(*args, **kwargs):
        """GetPage(self, size_t n) -> Window"""
        return __core.BookCtrlBase_GetPage(*args, **kwargs)

    def GetCurrentPage(*args, **kwargs):
        """GetCurrentPage(self) -> Window"""
        return __core.BookCtrlBase_GetCurrentPage(*args, **kwargs)

    def GetSelection(*args, **kwargs):
        """GetSelection(self) -> int"""
        return __core.BookCtrlBase_GetSelection(*args, **kwargs)

    def SetPageText(*args, **kwargs):
        """SetPageText(self, size_t n, String strText) -> bool"""
        return __core.BookCtrlBase_SetPageText(*args, **kwargs)

    def GetPageText(*args, **kwargs):
        """GetPageText(self, size_t n) -> String"""
        return __core.BookCtrlBase_GetPageText(*args, **kwargs)

    def GetPageImage(*args, **kwargs):
        """GetPageImage(self, size_t n) -> int"""
        return __core.BookCtrlBase_GetPageImage(*args, **kwargs)

    def SetPageImage(*args, **kwargs):
        """SetPageImage(self, size_t n, int imageId) -> bool"""
        return __core.BookCtrlBase_SetPageImage(*args, **kwargs)

    def SetPageSize(*args, **kwargs):
        """SetPageSize(self, Size size)"""
        return __core.BookCtrlBase_SetPageSize(*args, **kwargs)

    def CalcSizeFromPage(*args, **kwargs):
        """CalcSizeFromPage(self, Size sizePage) -> Size"""
        return __core.BookCtrlBase_CalcSizeFromPage(*args, **kwargs)

    def GetInternalBorder(*args, **kwargs):
        """GetInternalBorder(self) -> unsigned int"""
        return __core.BookCtrlBase_GetInternalBorder(*args, **kwargs)

    def SetInternalBorder(*args, **kwargs):
        """SetInternalBorder(self, unsigned int internalBorder)"""
        return __core.BookCtrlBase_SetInternalBorder(*args, **kwargs)

    def IsVertical(*args, **kwargs):
        """IsVertical(self) -> bool"""
        return __core.BookCtrlBase_IsVertical(*args, **kwargs)

    def SetControlMargin(*args, **kwargs):
        """SetControlMargin(self, int margin)"""
        return __core.BookCtrlBase_SetControlMargin(*args, **kwargs)

    def GetControlMargin(*args, **kwargs):
        """GetControlMargin(self) -> int"""
        return __core.BookCtrlBase_GetControlMargin(*args, **kwargs)

    def SetFitToCurrentPage(*args, **kwargs):
        """SetFitToCurrentPage(self, bool fit)"""
        return __core.BookCtrlBase_SetFitToCurrentPage(*args, **kwargs)

    def GetFitToCurrentPage(*args, **kwargs):
        """GetFitToCurrentPage(self) -> bool"""
        return __core.BookCtrlBase_GetFitToCurrentPage(*args, **kwargs)

    def GetControlSizer(*args, **kwargs):
        """GetControlSizer(self) -> Sizer"""
        return __core.BookCtrlBase_GetControlSizer(*args, **kwargs)

    def DeletePage(*args, **kwargs):
        """DeletePage(self, size_t n) -> bool"""
        return __core.BookCtrlBase_DeletePage(*args, **kwargs)

    def RemovePage(*args, **kwargs):
        """RemovePage(self, size_t n) -> bool"""
        return __core.BookCtrlBase_RemovePage(*args, **kwargs)

    def DeleteAllPages(*args, **kwargs):
        """DeleteAllPages(self) -> bool"""
        return __core.BookCtrlBase_DeleteAllPages(*args, **kwargs)

    def AddPage(*args, **kwargs):
        """AddPage(self, Window page, String text, bool select=False, int imageId=-1) -> bool"""
        return __core.BookCtrlBase_AddPage(*args, **kwargs)

    def InsertPage(*args, **kwargs):
        """
        InsertPage(self, size_t n, Window page, String text, bool select=False, 
            int imageId=-1) -> bool
        """
        return __core.BookCtrlBase_InsertPage(*args, **kwargs)

    def SetSelection(*args, **kwargs):
        """SetSelection(self, size_t n) -> int"""
        return __core.BookCtrlBase_SetSelection(*args, **kwargs)

    def ChangeSelection(*args, **kwargs):
        """ChangeSelection(self, size_t n) -> int"""
        return __core.BookCtrlBase_ChangeSelection(*args, **kwargs)

    def AdvanceSelection(*args, **kwargs):
        """AdvanceSelection(self, bool forward=True)"""
        return __core.BookCtrlBase_AdvanceSelection(*args, **kwargs)

    def HitTest(*args, **kwargs):
        """
        HitTest(Point pt) -> (tab, where)

        Returns the page/tab which is hit, and flags indicating where using
        wx.NB_HITTEST flags.
        """
        return __core.BookCtrlBase_HitTest(*args, **kwargs)

    def GetClassDefaultAttributes(*args, **kwargs):
        """
        GetClassDefaultAttributes(int variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes

        Get the default attributes for this class.  This is useful if you want
        to use the same font or colour in your own control as in a standard
        control -- which is a much better idea than hard coding specific
        colours or fonts which might look completely out of place on the
        user's system, especially if it uses themes.

        The variant parameter is only relevant under Mac currently and is
        ignore under other platforms. Under Mac, it will change the size of
        the returned font. See `wx.Window.SetWindowVariant` for more about
        this.
        """
        return __core.BookCtrlBase_GetClassDefaultAttributes(*args, **kwargs)

    GetClassDefaultAttributes = staticmethod(GetClassDefaultAttributes)
    ControlMargin = property(GetControlMargin,SetControlMargin,doc="See `GetControlMargin` and `SetControlMargin`") 
    ControlSizer = property(GetControlSizer,doc="See `GetControlSizer`") 
    CurrentPage = property(GetCurrentPage,doc="See `GetCurrentPage`") 
    FitToCurrentPage = property(GetFitToCurrentPage,SetFitToCurrentPage,doc="See `GetFitToCurrentPage` and `SetFitToCurrentPage`") 
    InternalBorder = property(GetInternalBorder,SetInternalBorder,doc="See `GetInternalBorder` and `SetInternalBorder`") 
    PageCount = property(GetPageCount,doc="See `GetPageCount`") 
    PageImage = property(GetPageImage,SetPageImage,doc="See `GetPageImage` and `SetPageImage`") 
    PageText = property(GetPageText,SetPageText,doc="See `GetPageText` and `SetPageText`") 
    Selection = property(GetSelection,SetSelection,doc="See `GetSelection` and `SetSelection`") 
__core.BookCtrlBase_swigregister(BookCtrlBase)

def BookCtrlBase_GetClassDefaultAttributes(*args, **kwargs):
  """
    BookCtrlBase_GetClassDefaultAttributes(int variant=WINDOW_VARIANT_NORMAL) -> VisualAttributes

    Get the default attributes for this class.  This is useful if you want
    to use the same font or colour in your own control as in a standard
    control -- which is a much better idea than hard coding specific
    colours or fonts which might look completely out of place on the
    user's system, especially if it uses themes.

    The variant parameter is only relevant under Mac currently and is
    ignore under other platforms. Under Mac, it will change the size of
    the returned font. See `wx.Window.SetWindowVariant` for more about
    this.
    """
  return __core.BookCtrlBase_GetClassDefaultAttributes(*args, **kwargs)

class BookCtrlEvent(NotifyEvent):
    """Proxy of C++ BookCtrlEvent class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, EventType commandType=wxEVT_NULL, int id=0, int nSel=-1, 
            int nOldSel=-1) -> BookCtrlEvent
        """
        this = __core.new_BookCtrlEvent(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetSelection(*args, **kwargs):
        """
        GetSelection(self) -> int

        Returns item index for a listbox or choice selection event (not valid
        for a deselection).
        """
        return __core.BookCtrlEvent_GetSelection(*args, **kwargs)

    def SetSelection(*args, **kwargs):
        """SetSelection(self, int nSel)"""
        return __core.BookCtrlEvent_SetSelection(*args, **kwargs)

    def GetOldSelection(*args, **kwargs):
        """GetOldSelection(self) -> int"""
        return __core.BookCtrlEvent_GetOldSelection(*args, **kwargs)

    def SetOldSelection(*args, **kwargs):
        """SetOldSelection(self, int nOldSel)"""
        return __core.BookCtrlEvent_SetOldSelection(*args, **kwargs)

    OldSelection = property(GetOldSelection,SetOldSelection,doc="See `GetOldSelection` and `SetOldSelection`") 
    Selection = property(GetSelection,SetSelection,doc="See `GetSelection` and `SetSelection`") 
__core.BookCtrlEvent_swigregister(BookCtrlEvent)

#---------------------------------------------------------------------------

class SizerFlags(object):
    """
    Normally, when you add an item to a sizer via `wx.Sizer.Add`, you have
    to specify a lot of flags and parameters which can be unwieldy. This
    is where wx.SizerFlags comes in: it allows you to specify all
    parameters using the named methods instead. For example, instead of::

        sizer.Add(ctrl, 0, wx.EXPAND | wx.ALL, 10)

    you can now write::

        sizer.AddF(ctrl, wx.SizerFlags().Expand().Border(wx.ALL, 10))

    This is more readable and also allows you to create wx.SizerFlags
    objects which can be reused for several sizer items.::

        flagsExpand = wx.SizerFlags(1)
        flagsExpand.Expand().Border(wx.ALL, 10)
        sizer.AddF(ctrl1, flagsExpand)
        sizer.AddF(ctrl2, flagsExpand)

    Note that by specification, all methods of wx.SizerFlags return the
    wx.SizerFlags object itself allowing chaining multiple method calls
    like in the examples above.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int proportion=0) -> SizerFlags

        Constructs the flags object with the specified proportion.
        """
        this = __core.new_SizerFlags(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_SizerFlags
    __del__ = lambda self : None;
    def Proportion(*args, **kwargs):
        """
        Proportion(self, int proportion) -> SizerFlags

        Sets the item's proportion value.
        """
        return __core.SizerFlags_Proportion(*args, **kwargs)

    def Align(*args, **kwargs):
        """
        Align(self, int alignment) -> SizerFlags

        Sets the item's alignment
        """
        return __core.SizerFlags_Align(*args, **kwargs)

    def Expand(*args, **kwargs):
        """
        Expand(self) -> SizerFlags

        Sets the wx.EXPAND flag, which will cause the item to be expanded to
        fill as much space as it is given by the sizer.
        """
        return __core.SizerFlags_Expand(*args, **kwargs)

    def Centre(*args, **kwargs):
        """
        Centre(self) -> SizerFlags

        Same as `Center` for those with an alternate dialect of English.
        """
        return __core.SizerFlags_Centre(*args, **kwargs)

    def Center(*args, **kwargs):
        """
        Center(self) -> SizerFlags

        Sets the centering alignment flags.
        """
        return __core.SizerFlags_Center(*args, **kwargs)

    def Left(*args, **kwargs):
        """
        Left(self) -> SizerFlags

        Aligns the object to the left, a shortcut for calling
        Align(wx.ALIGN_LEFT)
        """
        return __core.SizerFlags_Left(*args, **kwargs)

    def Right(*args, **kwargs):
        """
        Right(self) -> SizerFlags

        Aligns the object to the right, a shortcut for calling
        Align(wx.ALIGN_RIGHT)
        """
        return __core.SizerFlags_Right(*args, **kwargs)

    def Top(*args, **kwargs):
        """
        Top(self) -> SizerFlags

        Aligns the object to the top of the available space, a shortcut for
        calling Align(wx.ALIGN_TOP)
        """
        return __core.SizerFlags_Top(*args, **kwargs)

    def Bottom(*args, **kwargs):
        """
        Bottom(self) -> SizerFlags

        Aligns the object to the bottom of the available space, a shortcut for
        calling Align(wx.ALIGN_BOTTOM)
        """
        return __core.SizerFlags_Bottom(*args, **kwargs)

    def Shaped(*args, **kwargs):
        """
        Shaped(self) -> SizerFlags

        Sets the wx.SHAPED flag.
        """
        return __core.SizerFlags_Shaped(*args, **kwargs)

    def FixedMinSize(*args, **kwargs):
        """
        FixedMinSize(self) -> SizerFlags

        Sets the wx.FIXED_MINSIZE flag.
        """
        return __core.SizerFlags_FixedMinSize(*args, **kwargs)

    def ReserveSpaceEvenIfHidden(*args, **kwargs):
        """
        ReserveSpaceEvenIfHidden(self) -> SizerFlags

        Makes the item ignore window's visibility status
        """
        return __core.SizerFlags_ReserveSpaceEvenIfHidden(*args, **kwargs)

    def Border(*args, **kwargs):
        """
        Border(self, int direction=ALL, int borderInPixels=-1) -> SizerFlags

        Sets the border of the item in the direction(s) or sides given by the
        direction parameter.  If the borderInPixels value is not given then
        the default border size (see `GetDefaultBorder`) will be used.
        """
        return __core.SizerFlags_Border(*args, **kwargs)

    def DoubleBorder(*args, **kwargs):
        """
        DoubleBorder(self, int direction=ALL) -> SizerFlags

        Sets the border in the given direction to twice the default border
        size.
        """
        return __core.SizerFlags_DoubleBorder(*args, **kwargs)

    def TripleBorder(*args, **kwargs):
        """
        TripleBorder(self, int direction=ALL) -> SizerFlags

        Sets the border in the given direction to three times the default
        border size.
        """
        return __core.SizerFlags_TripleBorder(*args, **kwargs)

    def HorzBorder(*args, **kwargs):
        """
        HorzBorder(self) -> SizerFlags

        Sets the left and right borders to the default border size.
        """
        return __core.SizerFlags_HorzBorder(*args, **kwargs)

    def DoubleHorzBorder(*args, **kwargs):
        """
        DoubleHorzBorder(self) -> SizerFlags

        Sets the left and right borders to twice the default border size.
        """
        return __core.SizerFlags_DoubleHorzBorder(*args, **kwargs)

    def GetDefaultBorder(*args, **kwargs):
        """
        GetDefaultBorder() -> int

        Returns the default border size used by the other border methods
        """
        return __core.SizerFlags_GetDefaultBorder(*args, **kwargs)

    GetDefaultBorder = staticmethod(GetDefaultBorder)
    def GetProportion(*args, **kwargs):
        """
        GetProportion(self) -> int

        Returns the proportion value to be used in the sizer item.
        """
        return __core.SizerFlags_GetProportion(*args, **kwargs)

    def GetFlags(*args, **kwargs):
        """
        GetFlags(self) -> int

        Returns the flags value to be used in the sizer item.
        """
        return __core.SizerFlags_GetFlags(*args, **kwargs)

    def GetBorderInPixels(*args, **kwargs):
        """
        GetBorderInPixels(self) -> int

        Returns the border value in pixels to be used in the sizer item.
        """
        return __core.SizerFlags_GetBorderInPixels(*args, **kwargs)

__core.SizerFlags_swigregister(SizerFlags)

def SizerFlags_GetDefaultBorder(*args):
  """
    SizerFlags_GetDefaultBorder() -> int

    Returns the default border size used by the other border methods
    """
  return __core.SizerFlags_GetDefaultBorder(*args)

#---------------------------------------------------------------------------

class SizerItemList_iterator(object):
    """This class serves as an iterator for a wxSizerItemList object."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_SizerItemList_iterator
    __del__ = lambda self : None;
    def next(*args, **kwargs):
        """next(self) -> SizerItem"""
        return __core.SizerItemList_iterator_next(*args, **kwargs)

__core.SizerItemList_iterator_swigregister(SizerItemList_iterator)

class SizerItemList(object):
    """
    This class wraps a wxList-based class and gives it a Python
    sequence-like interface.  Sequence operations supported are length,
    index access and iteration.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_SizerItemList
    __del__ = lambda self : None;
    def __len__(*args, **kwargs):
        """__len__(self) -> size_t"""
        return __core.SizerItemList___len__(*args, **kwargs)

    def __getitem__(*args, **kwargs):
        """__getitem__(self, size_t index) -> SizerItem"""
        return __core.SizerItemList___getitem__(*args, **kwargs)

    def __contains__(*args, **kwargs):
        """__contains__(self, SizerItem obj) -> bool"""
        return __core.SizerItemList___contains__(*args, **kwargs)

    def __iter__(*args, **kwargs):
        """__iter__(self) -> SizerItemList_iterator"""
        return __core.SizerItemList___iter__(*args, **kwargs)

    def index(*args, **kwargs):
        """index(self, SizerItem obj) -> int"""
        return __core.SizerItemList_index(*args, **kwargs)

    def __repr__(self):
        return "wxSizerItemList: " + repr(list(self))

__core.SizerItemList_swigregister(SizerItemList)

class SizerItem(Object):
    """
    The wx.SizerItem class is used to track the position, size and other
    attributes of each item managed by a `wx.Sizer`. It is not usually
    necessary to use this class because the sizer elements can also be
    identified by their positions or window or sizer references but
    sometimes it may be more convenient to use wx.SizerItem directly.
    Also, custom classes derived from `wx.PySizer` will probably need to
    use the collection of wx.SizerItems held by wx.Sizer when calculating
    layout.

    :see: `wx.Sizer`, `wx.GBSizerItem`
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> SizerItem

        Constructs an empty wx.SizerItem.  Either a window, sizer or spacer
        size will need to be set before this item can be used in a Sizer.

        You will probably never need to create a wx.SizerItem directly as they
        are created automatically when the sizer's Add, Insert or Prepend
        methods are called.

        :see: `wx.SizerItemSpacer`, `wx.SizerItemWindow`, `wx.SizerItemSizer`
        """
        this = __core.new_SizerItem(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_SizerItem
    __del__ = lambda self : None;
    def DeleteWindows(*args, **kwargs):
        """
        DeleteWindows(self)

        Destroy the window or the windows in a subsizer, depending on the type
        of item.
        """
        return __core.SizerItem_DeleteWindows(*args, **kwargs)

    def DetachSizer(*args, **kwargs):
        """
        DetachSizer(self)

        Enable deleting the SizerItem without destroying the contained sizer.
        """
        return __core.SizerItem_DetachSizer(*args, **kwargs)

    def GetSize(*args, **kwargs):
        """
        GetSize(self) -> Size

        Get the current size of the item, as set in the last Layout.
        """
        return __core.SizerItem_GetSize(*args, **kwargs)

    def CalcMin(*args, **kwargs):
        """
        CalcMin(self) -> Size

        Calculates the minimum desired size for the item, including any space
        needed by borders.
        """
        return __core.SizerItem_CalcMin(*args, **kwargs)

    def SetDimension(*args, **kwargs):
        """
        SetDimension(self, Point pos, Size size)

        Set the position and size of the space allocated for this item by the
        sizer, and adjust the position and size of the item (window or
        subsizer) to be within that space taking alignment and borders into
        account.
        """
        return __core.SizerItem_SetDimension(*args, **kwargs)

    def GetMinSize(*args, **kwargs):
        """
        GetMinSize(self) -> Size

        Get the minimum size needed for the item.
        """
        return __core.SizerItem_GetMinSize(*args, **kwargs)

    def SetMinSize(*args, **kwargs):
        """
        SetMinSize(self, Size size)

        Set the min size needed for the item
        """
        return __core.SizerItem_SetMinSize(*args, **kwargs)

    def GetMinSizeWithBorder(*args, **kwargs):
        """
        GetMinSizeWithBorder(self) -> Size

        Get the minimum size needed for the item with space for the borders
        added, if needed.
        """
        return __core.SizerItem_GetMinSizeWithBorder(*args, **kwargs)

    def SetInitSize(*args, **kwargs):
        """SetInitSize(self, int x, int y)"""
        return __core.SizerItem_SetInitSize(*args, **kwargs)

    def SetRatioWH(*args, **kwargs):
        """
        SetRatioWH(self, int width, int height)

        Set the ratio item attribute.
        """
        return __core.SizerItem_SetRatioWH(*args, **kwargs)

    def SetRatioSize(*args, **kwargs):
        """
        SetRatioSize(self, Size size)

        Set the ratio item attribute.
        """
        return __core.SizerItem_SetRatioSize(*args, **kwargs)

    def SetRatio(*args, **kwargs):
        """
        SetRatio(self, float ratio)

        Set the ratio item attribute.
        """
        return __core.SizerItem_SetRatio(*args, **kwargs)

    def GetRatio(*args, **kwargs):
        """
        GetRatio(self) -> float

        Set the ratio item attribute.
        """
        return __core.SizerItem_GetRatio(*args, **kwargs)

    def GetRect(*args, **kwargs):
        """
        GetRect(self) -> Rect

        Returns the rectangle that the sizer item should occupy
        """
        return __core.SizerItem_GetRect(*args, **kwargs)

    def SetId(*args, **kwargs):
        """SetId(self, int id)"""
        return __core.SizerItem_SetId(*args, **kwargs)

    def GetId(*args, **kwargs):
        """GetId(self) -> int"""
        return __core.SizerItem_GetId(*args, **kwargs)

    def IsWindow(*args, **kwargs):
        """
        IsWindow(self) -> bool

        Is this sizer item a window?
        """
        return __core.SizerItem_IsWindow(*args, **kwargs)

    def IsSizer(*args, **kwargs):
        """
        IsSizer(self) -> bool

        Is this sizer item a subsizer?
        """
        return __core.SizerItem_IsSizer(*args, **kwargs)

    def IsSpacer(*args, **kwargs):
        """
        IsSpacer(self) -> bool

        Is this sizer item a spacer?
        """
        return __core.SizerItem_IsSpacer(*args, **kwargs)

    def SetProportion(*args, **kwargs):
        """
        SetProportion(self, int proportion)

        Set the proportion value for this item.
        """
        return __core.SizerItem_SetProportion(*args, **kwargs)

    def GetProportion(*args, **kwargs):
        """
        GetProportion(self) -> int

        Get the proportion value for this item.
        """
        return __core.SizerItem_GetProportion(*args, **kwargs)

    SetOption = wx.deprecated(SetProportion, "Please use `SetProportion` instead.") 
    GetOption = wx.deprecated(GetProportion, "Please use `GetProportion` instead.") 
    def SetFlag(*args, **kwargs):
        """
        SetFlag(self, int flag)

        Set the flag value for this item.
        """
        return __core.SizerItem_SetFlag(*args, **kwargs)

    def GetFlag(*args, **kwargs):
        """
        GetFlag(self) -> int

        Get the flag value for this item.
        """
        return __core.SizerItem_GetFlag(*args, **kwargs)

    def SetBorder(*args, **kwargs):
        """
        SetBorder(self, int border)

        Set the border value for this item.
        """
        return __core.SizerItem_SetBorder(*args, **kwargs)

    def GetBorder(*args, **kwargs):
        """
        GetBorder(self) -> int

        Get the border value for this item.
        """
        return __core.SizerItem_GetBorder(*args, **kwargs)

    def GetWindow(*args, **kwargs):
        """
        GetWindow(self) -> Window

        Get the window (if any) that is managed by this sizer item.
        """
        return __core.SizerItem_GetWindow(*args, **kwargs)

    def GetSizer(*args, **kwargs):
        """
        GetSizer(self) -> Sizer

        Get the subsizer (if any) that is managed by this sizer item.
        """
        return __core.SizerItem_GetSizer(*args, **kwargs)

    def GetSpacer(*args, **kwargs):
        """
        GetSpacer(self) -> Size

        Get the size of the spacer managed by this sizer item.
        """
        return __core.SizerItem_GetSpacer(*args, **kwargs)

    def SetWindow(*args, **kwargs):
        """
        SetWindow(self, Window window)

        Set the window to be managed by this sizer item.
        """
        return __core.SizerItem_SetWindow(*args, **kwargs)

    def SetSizer(*args, **kwargs):
        """
        SetSizer(self, Sizer sizer)

        Set the subsizer to be managed by this sizer item.
        """
        return __core.SizerItem_SetSizer(*args, **kwargs)

    def SetSpacer(*args, **kwargs):
        """
        SetSpacer(self, Size size)

        Set the size of the spacer to be managed by this sizer item.
        """
        return __core.SizerItem_SetSpacer(*args, **kwargs)

    SetWindow = wx.deprecated(SetWindow, "Use `AssignWindow` instead.")
    SetSizer = wx.deprecated(SetSizer,   "Use `AssignSizer` instead.")
    SetSpacer = wx.deprecated(SetSpacer, "Use `AssignSpacer` instead.")

    def AssignWindow(*args, **kwargs):
        """
        AssignWindow(self, Window window)

        Set the window to be managed by this sizer item.
        """
        return __core.SizerItem_AssignWindow(*args, **kwargs)

    def AssignSizer(*args, **kwargs):
        """
        AssignSizer(self, Sizer sizer)

        Set the subsizer to be managed by this sizer item.
        """
        return __core.SizerItem_AssignSizer(*args, **kwargs)

    def AssignSpacer(*args, **kwargs):
        """
        AssignSpacer(self, Size size)

        Set the size of the spacer to be managed by this sizer item.
        """
        return __core.SizerItem_AssignSpacer(*args, **kwargs)

    def Show(*args, **kwargs):
        """
        Show(self, bool show)

        Set the show item attribute, which sizers use to determine if the item
        is to be made part of the layout or not. If the item is tracking a
        window then it is shown or hidden as needed.
        """
        return __core.SizerItem_Show(*args, **kwargs)

    def IsShown(*args, **kwargs):
        """
        IsShown(self) -> bool

        Is the item to be shown in the layout?
        """
        return __core.SizerItem_IsShown(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> Point

        Returns the current position of the item, as set in the last Layout.
        """
        return __core.SizerItem_GetPosition(*args, **kwargs)

    def InformFirstDirection(*args, **kwargs):
        """
        InformFirstDirection(self, int direction, int size, int availableOtherDir=-1) -> bool

        Called once the first component of an item has been decided. This is
        used in algorithms that depend on knowing the size in one direction
        before the min size in the other direction can be known.  Returns true
        if it made use of the information (and min size was changed).
        """
        return __core.SizerItem_InformFirstDirection(*args, **kwargs)

    def GetUserData(*args, **kwargs):
        """
        GetUserData(self) -> PyObject

        Returns the userData associated with this sizer item, or None if there
        isn't any.
        """
        return __core.SizerItem_GetUserData(*args, **kwargs)

    def SetUserData(*args, **kwargs):
        """
        SetUserData(self, PyObject userData)

        Associate a Python object with this sizer item.
        """
        return __core.SizerItem_SetUserData(*args, **kwargs)

    Border = property(GetBorder,SetBorder,doc="See `GetBorder` and `SetBorder`") 
    Flag = property(GetFlag,SetFlag,doc="See `GetFlag` and `SetFlag`") 
    MinSize = property(GetMinSize,doc="See `GetMinSize`") 
    MinSizeWithBorder = property(GetMinSizeWithBorder,doc="See `GetMinSizeWithBorder`") 
    Position = property(GetPosition,doc="See `GetPosition`") 
    Proportion = property(GetProportion,SetProportion,doc="See `GetProportion` and `SetProportion`") 
    Ratio = property(GetRatio,SetRatio,doc="See `GetRatio` and `SetRatio`") 
    Rect = property(GetRect,doc="See `GetRect`") 
    Size = property(GetSize,doc="See `GetSize`") 
    Sizer = property(GetSizer,AssignSizer,doc="See `GetSizer` and `AssignSizer`") 
    Spacer = property(GetSpacer,AssignSpacer,doc="See `GetSpacer` and `AssignSpacer`") 
    UserData = property(GetUserData,SetUserData,doc="See `GetUserData` and `SetUserData`") 
    Window = property(GetWindow,AssignWindow,doc="See `GetWindow` and `AssignWindow`") 
    Id = property(GetId,SetId) 
__core.SizerItem_swigregister(SizerItem)

def SizerItemWindow(*args, **kwargs):
    """
    SizerItemWindow(Window window, int proportion=0, int flag=0, int border=0, 
        PyObject userData=None) -> SizerItem

    Constructs a `wx.SizerItem` for tracking a window.
    """
    val = __core.new_SizerItemWindow(*args, **kwargs)
    return val

def SizerItemSpacer(*args, **kwargs):
    """
    SizerItemSpacer(int width, int height, int proportion=0, int flag=0, 
        int border=0, PyObject userData=None) -> SizerItem

    Constructs a `wx.SizerItem` for tracking a spacer.
    """
    val = __core.new_SizerItemSpacer(*args, **kwargs)
    return val

def SizerItemSizer(*args, **kwargs):
    """
    SizerItemSizer(Sizer sizer, int proportion=0, int flag=0, int border=0, 
        PyObject userData=None) -> SizerItem

    Constructs a `wx.SizerItem` for tracking a subsizer
    """
    val = __core.new_SizerItemSizer(*args, **kwargs)
    return val

class Sizer(Object):
    """
    wx.Sizer is the abstract base class used for laying out subwindows in
    a window.  You cannot use wx.Sizer directly; instead, you will have to
    use one of the sizer classes derived from it such as `wx.BoxSizer`,
    `wx.StaticBoxSizer`, `wx.GridSizer`, `wx.FlexGridSizer` and
    `wx.GridBagSizer`.

    The concept implemented by sizers in wxWidgets is closely related to
    layout tools in other GUI toolkits, such as Java's AWT, the GTK
    toolkit or the Qt toolkit. It is based upon the idea of the individual
    subwindows reporting their minimal required size and their ability to
    get stretched if the size of the parent window has changed. This will
    most often mean that the programmer does not set the original size of
    a dialog in the beginning, rather the dialog will assigned a sizer and
    this sizer will be queried about the recommended size. The sizer in
    turn will query its children, which can be normal windows or contorls,
    empty space or other sizers, so that a hierarchy of sizers can be
    constructed. Note that wxSizer does not derive from wxWindow and thus
    do not interfere with tab ordering and requires very little resources
    compared to a real window on screen.

    What makes sizers so well fitted for use in wxWidgets is the fact that
    every control reports its own minimal size and the algorithm can
    handle differences in font sizes or different window (dialog item)
    sizes on different platforms without problems. If for example the
    standard font as well as the overall design of Mac widgets requires
    more space than on Windows, then the initial size of a dialog using a
    sizer will automatically be bigger on Mac than on Windows.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_Sizer
    __del__ = lambda self : None;
    def _setOORInfo(*args, **kwargs):
        """_setOORInfo(self, PyObject _self)"""
        return __core.Sizer__setOORInfo(*args, **kwargs)

    def Add(*args, **kwargs):
        """
        Add(self, item, int proportion=0, int flag=0, int border=0,
            PyObject userData=None) -> wx.SizerItem

        Appends a child item to the sizer.
        """
        return __core.Sizer_Add(*args, **kwargs)

    def AddF(*args, **kwargs):
        """
        AddF(self, item, wx.SizerFlags flags) -> wx.SizerItem

        Similar to `Add` but uses the `wx.SizerFlags` convenience class for
        setting the various flags, options and borders.
        """
        return __core.Sizer_AddF(*args, **kwargs)

    def Insert(*args, **kwargs):
        """
        Insert(self, int before, item, int proportion=0, int flag=0, int border=0,
            PyObject userData=None) -> wx.SizerItem

        Inserts a new item into the list of items managed by this sizer before
        the item at index *before*.  See `Add` for a description of the parameters.
        """
        return __core.Sizer_Insert(*args, **kwargs)

    def InsertF(*args, **kwargs):
        """
        InsertF(self, int before, item, wx.SizerFlags flags) -> wx.SizerItem

        Similar to `Insert`, but uses the `wx.SizerFlags` convenience class
        for setting the various flags, options and borders.
        """
        return __core.Sizer_InsertF(*args, **kwargs)

    def Prepend(*args, **kwargs):
        """
        Prepend(self, item, int proportion=0, int flag=0, int border=0,
            PyObject userData=None) -> wx.SizerItem

        Adds a new item to the begining of the list of sizer items managed by
        this sizer.  See `Add` for a description of the parameters.
        """
        return __core.Sizer_Prepend(*args, **kwargs)

    def PrependF(*args, **kwargs):
        """
        PrependF(self, item, wx.SizerFlags flags) -> wx.SizerItem

        Similar to `Prepend` but uses the `wx.SizerFlags` convenience class
        for setting the various flags, options and borders.
        """
        return __core.Sizer_PrependF(*args, **kwargs)

    def Remove(*args, **kwargs):
        """
        Remove(self, item) -> bool

        Removes an item from the sizer and destroys it.  This method does not
        cause any layout or resizing to take place, call `Layout` to update
        the layout on screen after removing a child from the sizer.  The
        *item* parameter can be either a window, a sizer, or the zero-based
        index of an item to remove.  Returns True if the child item was found
        and removed.
        """
        return __core.Sizer_Remove(*args, **kwargs)

    def Detach(*args, **kwargs):
        """
        Detach(self, item) -> bool

        Detaches an item from the sizer without destroying it.  This method
        does not cause any layout or resizing to take place, call `Layout` to
        do so.  The *item* parameter can be either a window, a sizer, or the
        zero-based index of the item to be detached.  Returns True if the child item
        was found and detached.
        """
        return __core.Sizer_Detach(*args, **kwargs)

    def GetItem(*args, **kwargs):
        """
        GetItem(self, item, recursive=False) -> wx.SizerItem

        Returns the `wx.SizerItem` which holds the *item* given.  The *item*
        parameter can be either a window, a sizer, or the zero-based index of
        the item to be found.
        """
        return __core.Sizer_GetItem(*args, **kwargs)

    def _SetItemMinSize(*args, **kwargs):
        """_SetItemMinSize(self, PyObject item, Size size)"""
        return __core.Sizer__SetItemMinSize(*args, **kwargs)

    def GetItemIndex(self, item):
        """
        Returns the index of the given *item* within the sizer. Does not
        search recursively.  The *item* parameter can be either a window
        or a sizer.  An assertion is raised if the item is not found in
        the sizer.
        """
        sItem = self.GetItem(item)
        assert sItem is not None, "Item not found in the sizer."
        allItems = self.Children
        idx = 0
        for i in allItems:
            if i.this == sItem.this:
                break
            idx += 1
        return idx

    def GetItemById(*args, **kwargs):
        """GetItemById(self, int id, bool recursive=False) -> SizerItem"""
        return __core.Sizer_GetItemById(*args, **kwargs)

    def _ReplaceWin(*args, **kwargs):
        """_ReplaceWin(self, Window oldwin, Window newwin, bool recursive=False) -> bool"""
        return __core.Sizer__ReplaceWin(*args, **kwargs)

    def _ReplaceSizer(*args, **kwargs):
        """_ReplaceSizer(self, Sizer oldsz, Sizer newsz, bool recursive=False) -> bool"""
        return __core.Sizer__ReplaceSizer(*args, **kwargs)

    def _ReplaceItem(*args, **kwargs):
        """_ReplaceItem(self, size_t index, SizerItem newitem) -> bool"""
        return __core.Sizer__ReplaceItem(*args, **kwargs)

    def Replace(self, olditem, item, recursive=False):
        """
        Detaches the given ``olditem`` from the sizer and replaces it with
        ``item`` which can be a window, sizer, or `wx.SizerItem`.  The
        detached child is destroyed only if it is not a window, (because
        windows are owned by their parent, not the sizer.)  The
        ``recursive`` parameter can be used to search for the given
        element recursivly in subsizers.

        This method does not cause any layout or resizing to take place,
        call `Layout` to do so.

        Returns ``True`` if the child item was found and removed.
        """
        if isinstance(olditem, wx.Window):
            return self._ReplaceWin(olditem, item, recursive)
        elif isinstance(olditem, wx.Sizer):
            return self._ReplaceSizer(olditem, item, recursive)
        elif isinstance(olditem, int):
            return self._ReplaceItem(olditem, item)
        else:
            raise TypeError("Expected Window, Sizer, or integer for first parameter.")

    def SetContainingWindow(*args, **kwargs):
        """
        SetContainingWindow(self, Window window)

        Set (or unset) the window this sizer is used in.
        """
        return __core.Sizer_SetContainingWindow(*args, **kwargs)

    def GetContainingWindow(*args, **kwargs):
        """
        GetContainingWindow(self) -> Window

        Get the window this sizer is used in.
        """
        return __core.Sizer_GetContainingWindow(*args, **kwargs)

    def SetItemMinSize(self, item, *args):
        """
        SetItemMinSize(self, item, Size size)

        Sets the minimum size that will be allocated for an item in the sizer.
        The *item* parameter can be either a window, a sizer, or the
        zero-based index of the item.  If a window or sizer is given then it
        will be searched for recursivly in subsizers if neccessary.
        """
        if len(args) == 2:
            # for backward compatibility accept separate width,height args too
            return self._SetItemMinSize(item, args)
        else:
            return self._SetItemMinSize(item, args[0])

    def AddItem(*args, **kwargs):
        """
        AddItem(self, SizerItem item)

        Adds a `wx.SizerItem` to the sizer.
        """
        return __core.Sizer_AddItem(*args, **kwargs)

    def InsertItem(*args, **kwargs):
        """
        InsertItem(self, int index, SizerItem item)

        Inserts a `wx.SizerItem` to the sizer at the position given by *index*.
        """
        return __core.Sizer_InsertItem(*args, **kwargs)

    def PrependItem(*args, **kwargs):
        """
        PrependItem(self, SizerItem item)

        Prepends a `wx.SizerItem` to the sizer.
        """
        return __core.Sizer_PrependItem(*args, **kwargs)

    def AddMany(self, items):
        """
        AddMany is a convenience method for adding several items
        to a sizer at one time.  Simply pass it a list of tuples,
        where each tuple consists of the parameters that you
        would normally pass to the `Add` method.
        """
        for item in items:
            if type(item) != type(()) or (len(item) == 2 and type(item[0]) == type(1)):
                item = (item, )
            self.Add(*item)

    def AddSpacer(self, *args, **kw):
        """AddSpacer(int size) --> SizerItem

        Add a spacer that is (size,size) pixels.
        """
        if args and type(args[0]) == int:
            return self.Add( (args[0],args[0] ), 0)
        else: # otherwise stay compatible with old AddSpacer
            return self.Add(*args, **kw)
    def PrependSpacer(self, *args, **kw):
        """PrependSpacer(int size) --> SizerItem

        Prepend a spacer that is (size, size) pixels."""
        if args and type(args[0]) == int:
            return self.Prepend( (args[0],args[0] ), 0)
        else: # otherwise stay compatible with old PrependSpacer
            return self.Prepend(*args, **kw)
    def InsertSpacer(self, index, *args, **kw):
        """InsertSpacer(int index, int size) --> SizerItem

        Insert a spacer at position index that is (size, size) pixels."""
        if args and type(args[0]) == int:
            return self.Insert( index, (args[0],args[0] ), 0)
        else: # otherwise stay compatible with old InsertSpacer
            return self.Insert(index, *args, **kw)

                   
    def AddStretchSpacer(self, prop=1):
        """AddStretchSpacer(int prop=1) --> SizerItem

        Add a stretchable spacer."""
        return self.Add((0,0), prop)
    def PrependStretchSpacer(self, prop=1):
        """PrependStretchSpacer(int prop=1) --> SizerItem

        Prepend a stretchable spacer."""
        return self.Prepend((0,0), prop)
    def InsertStretchSpacer(self, index, prop=1):
        """InsertStretchSpacer(int index, int prop=1) --> SizerItem

        Insert a stretchable spacer."""
        return self.Insert(index, (0,0), prop)

            
    # for backwards compatibility only, please do not use in new code
    def AddWindow(self, *args, **kw):
        """Compatibility alias for `Add`."""
        return self.Add(*args, **kw)
    def AddSizer(self, *args, **kw):
        """Compatibility alias for `Add`."""
        return self.Add(*args, **kw)

    def PrependWindow(self, *args, **kw):
        """Compatibility alias for `Prepend`."""
        return self.Prepend(*args, **kw)
    def PrependSizer(self, *args, **kw):
        """Compatibility alias for `Prepend`."""
        return self.Prepend(*args, **kw)

    def InsertWindow(self, *args, **kw):
        """Compatibility alias for `Insert`."""
        return self.Insert(*args, **kw)
    def InsertSizer(self, *args, **kw):
        """Compatibility alias for `Insert`."""
        return self.Insert(*args, **kw)

    def RemoveWindow(self, *args, **kw):
        """Compatibility alias for `Remove`."""
        return self.Remove(*args, **kw)
    def RemoveSizer(self, *args, **kw):
        """Compatibility alias for `Remove`."""
        return self.Remove(*args, **kw)
    def RemovePos(self, *args, **kw):
        """Compatibility alias for `Remove`."""
        return self.Remove(*args, **kw)


    def SetDimension(*args):
        """
        SetDimension(self, int x, int y, int width, int height)
        SetDimension(self, Point pos, Size size)
        """
        return __core.Sizer_SetDimension(*args)

    def GetItemCount(*args, **kwargs):
        """GetItemCount(self) -> size_t"""
        return __core.Sizer_GetItemCount(*args, **kwargs)

    def IsEmpty(*args, **kwargs):
        """IsEmpty(self) -> bool"""
        return __core.Sizer_IsEmpty(*args, **kwargs)

    def SetMinSize(*args, **kwargs):
        """
        SetMinSize(self, Size size)

        Call this to give the sizer a minimal size. Normally, the sizer will
        calculate its minimal size based purely on how much space its children
        need. After calling this method `GetMinSize` will return either the
        minimal size as requested by its children or the minimal size set
        here, depending on which is bigger.
        """
        return __core.Sizer_SetMinSize(*args, **kwargs)

    def GetSize(*args, **kwargs):
        """
        GetSize(self) -> Size

        Returns the current size of the space managed by the sizer.
        """
        return __core.Sizer_GetSize(*args, **kwargs)

    def GetPosition(*args, **kwargs):
        """
        GetPosition(self) -> Point

        Returns the current position of the sizer's managed space.
        """
        return __core.Sizer_GetPosition(*args, **kwargs)

    def GetMinSize(*args, **kwargs):
        """
        GetMinSize(self) -> Size

        Returns the minimal size of the sizer. This is either the combined
        minimal size of all the children and their borders or the minimal size
        set by `SetMinSize`, depending on which is bigger.

        Note that the returned value is *client* size, not window size.  In
        particular, if you use the value to set toplevel window's minimal or
        actual size, use `wx.Window.SetMinClientSize` or
        `wx.Window.SetClientSize`, *not* `wx.Window.SetMinSize` or
        `wx.Window.SetSize`.
        """
        return __core.Sizer_GetMinSize(*args, **kwargs)

    def GetSizeTuple(self):
        return self.GetSize().Get()
    def GetPositionTuple(self):
        return self.GetPosition().Get()
    def GetMinSizeTuple(self):
        return self.GetMinSize().Get()

    def RecalcSizes(*args, **kwargs):
        """
        RecalcSizes(self)

        Using the sizes calculated by `CalcMin` reposition and resize all the
        items managed by this sizer.  You should not need to call this directly as
        it is called by `Layout`.
        """
        return __core.Sizer_RecalcSizes(*args, **kwargs)

    def CalcMin(*args, **kwargs):
        """
        CalcMin(self) -> Size

        This method is where the sizer will do the actual calculation of its
        children's minimal sizes.  You should not need to call this directly as
        it is called by `Layout`.
        """
        return __core.Sizer_CalcMin(*args, **kwargs)

    def Layout(*args, **kwargs):
        """
        Layout(self)

        This method will force the recalculation and layout of the items
        controlled by the sizer using the current space allocated to the
        sizer.  Normally this is called automatically from the owning window's
        EVT_SIZE handler, but it is also useful to call it from user code when
        one of the items in a sizer change size, or items are added or
        removed.
        """
        return __core.Sizer_Layout(*args, **kwargs)

    def ComputeFittingClientSize(*args, **kwargs):
        """
        ComputeFittingClientSize(self, Window window) -> Size

        Computes client area size for ``window`` so that it matches the
        sizer's minimal size. Unlike `GetMinSize`, this method accounts for
        other constraints imposed on ``window``, namely display's size
        (returned size will never be too large for the display) and maximum
        window size if previously set by `wx.Window.SetMaxSize`.

        The returned value is suitable for passing to
        `wx.Window.SetClientSize` or `wx`Window.SetMinClientSize`.
        """
        return __core.Sizer_ComputeFittingClientSize(*args, **kwargs)

    def ComputeFittingWindowSize(*args, **kwargs):
        """
        ComputeFittingWindowSize(self, Window window) -> Size

        Like `ComputeFittingClientSize`, but converts the result into *window*
        size.

        The returned value is suitable for passing to `wx.Window.SetSize` or
        `wx.Window.SetMinSize`.

        """
        return __core.Sizer_ComputeFittingWindowSize(*args, **kwargs)

    def Fit(*args, **kwargs):
        """
        Fit(self, Window window) -> Size

        Tell the sizer to resize the *window* to match the sizer's minimal
        size. This is commonly done in the constructor of the window itself in
        order to set its initial size to match the needs of the children as
        determined by the sizer.  Returns the new size.

        For a top level window this is the total window size, not the client size.
        """
        return __core.Sizer_Fit(*args, **kwargs)

    def FitInside(*args, **kwargs):
        """
        FitInside(self, Window window)

        Tell the sizer to resize the *virtual size* of the *window* to match the
        sizer's minimal size. This will not alter the on screen size of the
        window, but may cause the addition/removal/alteration of scrollbars
        required to view the virtual area in windows which manage it.

        :see: `wx.ScrolledWindow.SetScrollbars`

        """
        return __core.Sizer_FitInside(*args, **kwargs)

    def SetSizeHints(*args, **kwargs):
        """
        SetSizeHints(self, Window window)

        Tell the sizer to set (and `Fit`) the minimal size of the *window* to
        match the sizer's minimal size. This is commonly done in the
        constructor of the window itself if the window is resizable (as are
        many dialogs under Unix and frames on probably all platforms) in order
        to prevent the window from being sized smaller than the minimal size
        required by the sizer.
        """
        return __core.Sizer_SetSizeHints(*args, **kwargs)

    def SetVirtualSizeHints(*args, **kwargs):
        """
        SetVirtualSizeHints(self, Window window)

        Tell the sizer to set the minimal size of the window virtual area to
        match the sizer's minimal size. For windows with managed scrollbars
        this will set them appropriately.

        :see: `wx.ScrolledWindow.SetScrollbars`

        """
        return __core.Sizer_SetVirtualSizeHints(*args, **kwargs)

    SetVirtualSizeHints = wx.deprecated(SetVirtualSizeHints) 
    def Clear(*args, **kwargs):
        """
        Clear(self, bool deleteWindows=False)

        Clear all items from the sizer, optionally destroying the window items
        as well.
        """
        return __core.Sizer_Clear(*args, **kwargs)

    def DeleteWindows(*args, **kwargs):
        """
        DeleteWindows(self)

        Destroy all windows managed by the sizer.
        """
        return __core.Sizer_DeleteWindows(*args, **kwargs)

    def InformFirstDirection(*args, **kwargs):
        """
        InformFirstDirection(self, int direction, int size, int availableOtherDir) -> bool

        Inform sizer about the first direction that has been decided (by
        parent item).  Returns true if it made use of the informtion (and
        recalculated min size).
        """
        return __core.Sizer_InformFirstDirection(*args, **kwargs)

    def GetChildren(*args, **kwargs):
        """
        GetChildren(self) -> SizerItemList

        Returns all of the `wx.SizerItem` objects managed by the sizer in a
        list-like object.
        """
        return __core.Sizer_GetChildren(*args, **kwargs)

    def Show(*args, **kwargs):
        """
        Show(self, item, bool show=True, bool recursive=false) -> bool

        Shows or hides an item managed by the sizer.  To make a sizer item
        disappear or reappear, use Show followed by `Layout`.  The *item*
        parameter can be either a window, a sizer, or the zero-based index of
        the item.  Use the recursive parameter to show or hide an item in a
        subsizer.  Returns True if the item was found.
        """
        return __core.Sizer_Show(*args, **kwargs)

    def IsShown(*args, **kwargs):
        """
        IsShown(self, item)

        Determines if the item is currently shown. To make a sizer
        item disappear or reappear, use Show followed by `Layout`.  The *item*
        parameter can be either a window, a sizer, or the zero-based index of
        the item.
        """
        return __core.Sizer_IsShown(*args, **kwargs)

    def Hide(self, item, recursive=False):
        """
        A convenience method for `Show` (item, False, recursive).
        """
        return self.Show(item, False, recursive)

    def ShowItems(*args, **kwargs):
        """
        ShowItems(self, bool show)

        Recursively call `wx.SizerItem.Show` on all sizer items.
        """
        return __core.Sizer_ShowItems(*args, **kwargs)

    Children = property(GetChildren,doc="See `GetChildren`") 
    ContainingWindow = property(GetContainingWindow,SetContainingWindow,doc="See `GetContainingWindow` and `SetContainingWindow`") 
    MinSize = property(GetMinSize,SetMinSize,doc="See `GetMinSize` and `SetMinSize`") 
    Position = property(GetPosition,doc="See `GetPosition`") 
    Size = property(GetSize,doc="See `GetSize`") 
__core.Sizer_swigregister(Sizer)

class PySizer(Sizer):
    """
    wx.PySizer is a special version of `wx.Sizer` that has been
    instrumented to allow the C++ virtual methods to be overloaded in
    Python derived classes.  You would derive from this class if you are
    wanting to implement a custom sizer in Python code.  Simply implement
    `CalcMin` and `RecalcSizes` in the derived class and you're all set.
    For example::

        class MySizer(wx.PySizer):
             def __init__(self):
                 wx.PySizer.__init__(self)

             def CalcMin(self):
                 for item in self.GetChildren():
                      # calculate the total minimum width and height needed
                      # by all items in the sizer according to this sizer's
                      # layout algorithm.
                      ...
                 return wx.Size(width, height)

              def RecalcSizes(self):
                  # find the space allotted to this sizer
                  pos = self.GetPosition()
                  size = self.GetSize()
                  for item in self.GetChildren():
                      # Recalculate (if necessary) the position and size of
                      # each item and then call item.SetDimension to do the
                      # actual positioning and sizing of the items within the
                      # space alloted to this sizer.
                      ...
                      item.SetDimension(itemPos, itemSize)


    When `Layout` is called it first calls `CalcMin` followed by
    `RecalcSizes` so you can optimize a bit by saving the results of
    `CalcMin` and reusing them in `RecalcSizes`.

    :see: `wx.SizerItem`, `wx.Sizer.GetChildren`


    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> PySizer

        Creates a wx.PySizer.  Must be called from the __init__ in the derived
        class.
        """
        this = __core.new_PySizer(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self);PySizer._setCallbackInfo(self, self, PySizer)

    def _setCallbackInfo(*args, **kwargs):
        """_setCallbackInfo(self, PyObject self, PyObject _class)"""
        return __core.PySizer__setCallbackInfo(*args, **kwargs)

__core.PySizer_swigregister(PySizer)

#---------------------------------------------------------------------------

class BoxSizer(Sizer):
    """
    The basic idea behind a box sizer is that windows will most often be
    laid out in rather simple basic geometry, typically in a row or a
    column or nested hierarchies of either.  A wx.BoxSizer will lay out
    its items in a simple row or column, depending on the orientation
    parameter passed to the constructor.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int orient=HORIZONTAL) -> BoxSizer

        Constructor for a wx.BoxSizer. *orient* may be one of ``wx.VERTICAL``
        or ``wx.HORIZONTAL`` for creating either a column sizer or a row
        sizer.
        """
        this = __core.new_BoxSizer(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def GetOrientation(*args, **kwargs):
        """
        GetOrientation(self) -> int

        Returns the current orientation of the sizer.
        """
        return __core.BoxSizer_GetOrientation(*args, **kwargs)

    def SetOrientation(*args, **kwargs):
        """
        SetOrientation(self, int orient)

        Resets the orientation of the sizer.
        """
        return __core.BoxSizer_SetOrientation(*args, **kwargs)

    def IsVertical(*args, **kwargs):
        """IsVertical(self) -> bool"""
        return __core.BoxSizer_IsVertical(*args, **kwargs)

    Orientation = property(GetOrientation,SetOrientation,doc="See `GetOrientation` and `SetOrientation`") 
__core.BoxSizer_swigregister(BoxSizer)

#---------------------------------------------------------------------------

EXTEND_LAST_ON_EACH_LINE = __core.EXTEND_LAST_ON_EACH_LINE
class WrapSizer(BoxSizer):
    """
    A box sizer that can wrap items on several lines when widths exceed
    available width.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int orient=HORIZONTAL, int flags=EXTEND_LAST_ON_EACH_LINE) -> WrapSizer

        A box sizer that can wrap items on several lines when widths exceed
        available width.
        """
        this = __core.new_WrapSizer(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.WrapSizer_swigregister(WrapSizer)

#---------------------------------------------------------------------------

class StaticBoxSizer(BoxSizer):
    """
    wx.StaticBoxSizer derives from and functions identically to the
    `wx.BoxSizer` and adds a `wx.StaticBox` around the items that the sizer
    manages.  Note that this static box must be created separately and
    passed to the sizer constructor.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, StaticBox box, int orient=HORIZONTAL) -> StaticBoxSizer

        Constructor. It takes an associated static box and the orientation
        *orient* as parameters - orient can be either of ``wx.VERTICAL`` or
        ``wx.HORIZONTAL``.
        """
        this = __core.new_StaticBoxSizer(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def GetStaticBox(*args, **kwargs):
        """
        GetStaticBox(self) -> StaticBox

        Returns the static box associated with this sizer.
        """
        return __core.StaticBoxSizer_GetStaticBox(*args, **kwargs)

    StaticBox = property(GetStaticBox,doc="See `GetStaticBox`") 
__core.StaticBoxSizer_swigregister(StaticBoxSizer)

#---------------------------------------------------------------------------

class GridSizer(Sizer):
    """
    A grid sizer is a sizer which lays out its children in a
    two-dimensional table with all cells having the same size.  In other
    words, the width of each cell within the grid is the width of the
    widest item added to the sizer and the height of each grid cell is the
    height of the tallest item.  An optional vertical and/or horizontal
    gap between items can also be specified (in pixels.)

    Items are placed in the cells of the grid in the order they are added,
    in row-major order.  In other words, the first row is filled first,
    then the second, and so on until all items have been added. (If
    neccessary, additional rows will be added as items are added.)  If you
    need to have greater control over the cells that items are placed in
    then use the `wx.GridBagSizer`.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int rows=0, int cols=0, int vgap=0, int hgap=0) -> GridSizer

        Constructor for a wx.GridSizer. *rows* and *cols* determine the number
        of columns and rows in the sizer - if either of the parameters is
        zero, it will be calculated to from the total number of children in
        the sizer, thus making the sizer grow dynamically. *vgap* and *hgap*
        define extra space between all children.
        """
        this = __core.new_GridSizer(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)
        if self.Rows == 0 and self.Cols == 0:
            self.Rows = 1

    def SetCols(*args, **kwargs):
        """
        SetCols(self, int cols)

        Sets the number of columns in the sizer.
        """
        return __core.GridSizer_SetCols(*args, **kwargs)

    def SetRows(*args, **kwargs):
        """
        SetRows(self, int rows)

        Sets the number of rows in the sizer.
        """
        return __core.GridSizer_SetRows(*args, **kwargs)

    def SetVGap(*args, **kwargs):
        """
        SetVGap(self, int gap)

        Sets the vertical gap (in pixels) between the cells in the sizer.
        """
        return __core.GridSizer_SetVGap(*args, **kwargs)

    def SetHGap(*args, **kwargs):
        """
        SetHGap(self, int gap)

        Sets the horizontal gap (in pixels) between cells in the sizer
        """
        return __core.GridSizer_SetHGap(*args, **kwargs)

    def GetCols(*args, **kwargs):
        """
        GetCols(self) -> int

        Returns the number of columns in the sizer.
        """
        return __core.GridSizer_GetCols(*args, **kwargs)

    def GetRows(*args, **kwargs):
        """
        GetRows(self) -> int

        Returns the number of rows in the sizer.
        """
        return __core.GridSizer_GetRows(*args, **kwargs)

    def GetVGap(*args, **kwargs):
        """
        GetVGap(self) -> int

        Returns the vertical gap (in pixels) between the cells in the sizer.
        """
        return __core.GridSizer_GetVGap(*args, **kwargs)

    def GetHGap(*args, **kwargs):
        """
        GetHGap(self) -> int

        Returns the horizontal gap (in pixels) between cells in the sizer.
        """
        return __core.GridSizer_GetHGap(*args, **kwargs)

    def GetEffectiveColsCount(*args, **kwargs):
        """GetEffectiveColsCount(self) -> int"""
        return __core.GridSizer_GetEffectiveColsCount(*args, **kwargs)

    def GetEffectiveRowsCount(*args, **kwargs):
        """GetEffectiveRowsCount(self) -> int"""
        return __core.GridSizer_GetEffectiveRowsCount(*args, **kwargs)

    def CalcRowsCols(self):
        """
        CalcRowsCols() -> (rows, cols)

        Calculates how many rows and columns will be in the sizer based
        on the current number of items and also the rows, cols specified
        in the constructor.
        """
        nitems = len(self.GetChildren())
        rows = self.GetRows()
        cols = self.GetCols()
        assert rows != 0 or cols != 0, "Grid sizer must have either rows or columns fixed"
        if cols != 0:
            rows = (nitems + cols - 1) / cols
        elif rows != 0:
            cols = (nitems + rows - 1) / rows
        return (rows, cols)

    Cols = property(GetCols,SetCols,doc="See `GetCols` and `SetCols`") 
    HGap = property(GetHGap,SetHGap,doc="See `GetHGap` and `SetHGap`") 
    Rows = property(GetRows,SetRows,doc="See `GetRows` and `SetRows`") 
    VGap = property(GetVGap,SetVGap,doc="See `GetVGap` and `SetVGap`") 
__core.GridSizer_swigregister(GridSizer)

#---------------------------------------------------------------------------

FLEX_GROWMODE_NONE = __core.FLEX_GROWMODE_NONE
FLEX_GROWMODE_SPECIFIED = __core.FLEX_GROWMODE_SPECIFIED
FLEX_GROWMODE_ALL = __core.FLEX_GROWMODE_ALL
class FlexGridSizer(GridSizer):
    """
    A flex grid sizer is a sizer which lays out its children in a
    two-dimensional table with all table cells in one row having the same
    height and all cells in one column having the same width, but all
    rows or all columns are not necessarily the same height or width as in
    the `wx.GridSizer`.

    wx.FlexGridSizer can also size items equally in one direction but
    unequally ("flexibly") in the other. If the sizer is only flexible
    in one direction (this can be changed using `SetFlexibleDirection`), it
    needs to be decided how the sizer should grow in the other ("non
    flexible") direction in order to fill the available space. The
    `SetNonFlexibleGrowMode` method serves this purpose.


    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int rows=0, int cols=0, int vgap=0, int hgap=0) -> FlexGridSizer

        Constructor for a wx.FlexGridSizer. *rows* and *cols* determine the
        number of columns and rows in the sizer - if either of the parameters
        is zero, it will be calculated to from the total number of children in
        the sizer, thus making the sizer grow dynamically. *vgap* and *hgap*
        define extra space between all children.
        """
        this = __core.new_FlexGridSizer(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)
        if self.Rows == 0 and self.Cols == 0:
            self.Rows = 1

    def AddGrowableRow(*args, **kwargs):
        """
        AddGrowableRow(self, size_t idx, int proportion=0)

        Specifies that row *idx* (starting from zero) should be grown if there
        is extra space available to the sizer.

        The *proportion* parameter has the same meaning as the stretch factor
        for the box sizers except that if all proportions are 0, then all
        columns are resized equally (instead of not being resized at all).
        """
        return __core.FlexGridSizer_AddGrowableRow(*args, **kwargs)

    def RemoveGrowableRow(*args, **kwargs):
        """
        RemoveGrowableRow(self, size_t idx)

        Specifies that row *idx* is no longer growable.
        """
        return __core.FlexGridSizer_RemoveGrowableRow(*args, **kwargs)

    def AddGrowableCol(*args, **kwargs):
        """
        AddGrowableCol(self, size_t idx, int proportion=0)

        Specifies that column *idx* (starting from zero) should be grown if
        there is extra space available to the sizer.

        The *proportion* parameter has the same meaning as the stretch factor
        for the box sizers except that if all proportions are 0, then all
        columns are resized equally (instead of not being resized at all).
        """
        return __core.FlexGridSizer_AddGrowableCol(*args, **kwargs)

    def RemoveGrowableCol(*args, **kwargs):
        """
        RemoveGrowableCol(self, size_t idx)

        Specifies that column *idx* is no longer growable.
        """
        return __core.FlexGridSizer_RemoveGrowableCol(*args, **kwargs)

    def IsRowGrowable(*args, **kwargs):
        """IsRowGrowable(self, size_t idx) -> bool"""
        return __core.FlexGridSizer_IsRowGrowable(*args, **kwargs)

    def IsColGrowable(*args, **kwargs):
        """IsColGrowable(self, size_t idx) -> bool"""
        return __core.FlexGridSizer_IsColGrowable(*args, **kwargs)

    def SetFlexibleDirection(*args, **kwargs):
        """
        SetFlexibleDirection(self, int direction)

        Specifies whether the sizer should flexibly resize its columns, rows,
        or both. Argument *direction* can be one of the following values.  Any
        other value is ignored.

            ==============    =======================================
            wx.VERTICAL       Rows are flexibly sized.
            wx.HORIZONTAL     Columns are flexibly sized.
            wx.BOTH           Both rows and columns are flexibly sized
                              (this is the default value).
            ==============    =======================================

        Note that this method does not trigger relayout.

        """
        return __core.FlexGridSizer_SetFlexibleDirection(*args, **kwargs)

    def GetFlexibleDirection(*args, **kwargs):
        """
        GetFlexibleDirection(self) -> int

        Returns a value that specifies whether the sizer
        flexibly resizes its columns, rows, or both (default).

        :see: `SetFlexibleDirection`
        """
        return __core.FlexGridSizer_GetFlexibleDirection(*args, **kwargs)

    def SetNonFlexibleGrowMode(*args, **kwargs):
        """
        SetNonFlexibleGrowMode(self, int mode)

        Specifies how the sizer should grow in the non-flexible direction if
        there is one (so `SetFlexibleDirection` must have been called
        previously). Argument *mode* can be one of the following values:

            ==========================  =================================================
            wx.FLEX_GROWMODE_NONE       Sizer doesn't grow in the non flexible direction.
            wx.FLEX_GROWMODE_SPECIFIED  Sizer honors growable columns/rows set with
                                        `AddGrowableCol` and `AddGrowableRow`. In this
                                        case equal sizing applies to minimum sizes of
                                        columns or rows (this is the default value).
            wx.FLEX_GROWMODE_ALL        Sizer equally stretches all columns or rows in
                                        the non flexible direction, whether they are
                                        growable or not in the flexbile direction.
            ==========================  =================================================

        Note that this method does not trigger relayout.
        """
        return __core.FlexGridSizer_SetNonFlexibleGrowMode(*args, **kwargs)

    def GetNonFlexibleGrowMode(*args, **kwargs):
        """
        GetNonFlexibleGrowMode(self) -> int

        Returns the value that specifies how the sizer grows in the
        non-flexible direction if there is one.

        :see: `SetNonFlexibleGrowMode`
        """
        return __core.FlexGridSizer_GetNonFlexibleGrowMode(*args, **kwargs)

    def GetRowHeights(*args, **kwargs):
        """
        GetRowHeights(self) -> list

        Returns a list of integers representing the heights of each of the
        rows in the sizer.
        """
        return __core.FlexGridSizer_GetRowHeights(*args, **kwargs)

    def GetColWidths(*args, **kwargs):
        """
        GetColWidths(self) -> list

        Returns a list of integers representing the widths of each of the
        columns in the sizer.
        """
        return __core.FlexGridSizer_GetColWidths(*args, **kwargs)

    ColWidths = property(GetColWidths,doc="See `GetColWidths`") 
    FlexibleDirection = property(GetFlexibleDirection,SetFlexibleDirection,doc="See `GetFlexibleDirection` and `SetFlexibleDirection`") 
    NonFlexibleGrowMode = property(GetNonFlexibleGrowMode,SetNonFlexibleGrowMode,doc="See `GetNonFlexibleGrowMode` and `SetNonFlexibleGrowMode`") 
    RowHeights = property(GetRowHeights,doc="See `GetRowHeights`") 
__core.FlexGridSizer_swigregister(FlexGridSizer)

class StdDialogButtonSizer(BoxSizer):
    """
    A special sizer that knows how to order and position standard buttons
    in order to conform to the current platform's standards.  You simply
    need to add each `wx.Button` to the sizer, and be sure to create the
    buttons using the standard ID's.  Then call `Realize` and the sizer
    will take care of the rest.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> StdDialogButtonSizer"""
        this = __core.new_StdDialogButtonSizer(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def AddButton(*args, **kwargs):
        """
        AddButton(self, wxButton button)

        Use this to add the buttons to this sizer.  Do not use the `Add`
        method in the base class.
        """
        return __core.StdDialogButtonSizer_AddButton(*args, **kwargs)

    def Realize(*args, **kwargs):
        """
        Realize(self)

        This funciton needs to be called after all the buttons have been added
        to the sizer.  It will reorder them and position them in a platform
        specifc manner.
        """
        return __core.StdDialogButtonSizer_Realize(*args, **kwargs)

    def SetAffirmativeButton(*args, **kwargs):
        """SetAffirmativeButton(self, wxButton button)"""
        return __core.StdDialogButtonSizer_SetAffirmativeButton(*args, **kwargs)

    def SetNegativeButton(*args, **kwargs):
        """SetNegativeButton(self, wxButton button)"""
        return __core.StdDialogButtonSizer_SetNegativeButton(*args, **kwargs)

    def SetCancelButton(*args, **kwargs):
        """SetCancelButton(self, wxButton button)"""
        return __core.StdDialogButtonSizer_SetCancelButton(*args, **kwargs)

    def GetAffirmativeButton(*args, **kwargs):
        """GetAffirmativeButton(self) -> wxButton"""
        return __core.StdDialogButtonSizer_GetAffirmativeButton(*args, **kwargs)

    def GetApplyButton(*args, **kwargs):
        """GetApplyButton(self) -> wxButton"""
        return __core.StdDialogButtonSizer_GetApplyButton(*args, **kwargs)

    def GetNegativeButton(*args, **kwargs):
        """GetNegativeButton(self) -> wxButton"""
        return __core.StdDialogButtonSizer_GetNegativeButton(*args, **kwargs)

    def GetCancelButton(*args, **kwargs):
        """GetCancelButton(self) -> wxButton"""
        return __core.StdDialogButtonSizer_GetCancelButton(*args, **kwargs)

    def GetHelpButton(*args, **kwargs):
        """GetHelpButton(self) -> wxButton"""
        return __core.StdDialogButtonSizer_GetHelpButton(*args, **kwargs)

    AffirmativeButton = property(GetAffirmativeButton,SetAffirmativeButton,doc="See `GetAffirmativeButton` and `SetAffirmativeButton`") 
    ApplyButton = property(GetApplyButton,doc="See `GetApplyButton`") 
    CancelButton = property(GetCancelButton,SetCancelButton,doc="See `GetCancelButton` and `SetCancelButton`") 
    HelpButton = property(GetHelpButton,doc="See `GetHelpButton`") 
    NegativeButton = property(GetNegativeButton,SetNegativeButton,doc="See `GetNegativeButton` and `SetNegativeButton`") 
__core.StdDialogButtonSizer_swigregister(StdDialogButtonSizer)

#---------------------------------------------------------------------------

class GBPosition(object):
    """
    This class represents the position of an item in a virtual grid of
    rows and columns managed by a `wx.GridBagSizer`.  wxPython has
    typemaps that will automatically convert from a 2-element sequence of
    integers to a wx.GBPosition, so you can use the more pythonic
    representation of the position nearly transparently in Python code.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int row=0, int col=0) -> GBPosition

        This class represents the position of an item in a virtual grid of
        rows and columns managed by a `wx.GridBagSizer`.  wxPython has
        typemaps that will automatically convert from a 2-element sequence of
        integers to a wx.GBPosition, so you can use the more pythonic
        representation of the position nearly transparently in Python code.
        """
        this = __core.new_GBPosition(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_GBPosition
    __del__ = lambda self : None;
    def GetRow(*args, **kwargs):
        """GetRow(self) -> int"""
        return __core.GBPosition_GetRow(*args, **kwargs)

    def GetCol(*args, **kwargs):
        """GetCol(self) -> int"""
        return __core.GBPosition_GetCol(*args, **kwargs)

    def SetRow(*args, **kwargs):
        """SetRow(self, int row)"""
        return __core.GBPosition_SetRow(*args, **kwargs)

    def SetCol(*args, **kwargs):
        """SetCol(self, int col)"""
        return __core.GBPosition_SetCol(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Compare GBPosition for equality.
        """
        return __core.GBPosition___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Compare GBPosition for inequality.
        """
        return __core.GBPosition___ne__(*args, **kwargs)

    def Set(*args, **kwargs):
        """Set(self, int row=0, int col=0)"""
        return __core.GBPosition_Set(*args, **kwargs)

    def Get(*args, **kwargs):
        """Get(self) -> PyObject"""
        return __core.GBPosition_Get(*args, **kwargs)

    asTuple = wx.deprecated(Get, "asTuple is deprecated, use `Get` instead")
    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'wx.GBPosition'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.SetRow(val)
        elif index == 1: self.SetCol(val)
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0,0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (wx.GBPosition, self.Get())

    row = property(GetRow, SetRow)
    col = property(GetCol, SetCol)

__core.GBPosition_swigregister(GBPosition)

class GBSpan(object):
    """
    This class is used to hold the row and column spanning attributes of
    items in a `wx.GridBagSizer`.  wxPython has typemaps that will
    automatically convert from a 2-element sequence of integers to a
    wx.GBSpan, so you can use the more pythonic representation of the span
    nearly transparently in Python code.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int rowspan=1, int colspan=1) -> GBSpan

        Construct a new wxGBSpan, optionally setting the rowspan and
        colspan. The default is (1,1). (Meaning that the item occupies one
        cell in each direction.
        """
        this = __core.new_GBSpan(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_GBSpan
    __del__ = lambda self : None;
    def GetRowspan(*args, **kwargs):
        """GetRowspan(self) -> int"""
        return __core.GBSpan_GetRowspan(*args, **kwargs)

    def GetColspan(*args, **kwargs):
        """GetColspan(self) -> int"""
        return __core.GBSpan_GetColspan(*args, **kwargs)

    def SetRowspan(*args, **kwargs):
        """SetRowspan(self, int rowspan)"""
        return __core.GBSpan_SetRowspan(*args, **kwargs)

    def SetColspan(*args, **kwargs):
        """SetColspan(self, int colspan)"""
        return __core.GBSpan_SetColspan(*args, **kwargs)

    def __eq__(*args, **kwargs):
        """
        __eq__(self, PyObject other) -> bool

        Compare wxGBSpan for equality.
        """
        return __core.GBSpan___eq__(*args, **kwargs)

    def __ne__(*args, **kwargs):
        """
        __ne__(self, PyObject other) -> bool

        Compare GBSpan for inequality.
        """
        return __core.GBSpan___ne__(*args, **kwargs)

    def Set(*args, **kwargs):
        """Set(self, int rowspan=1, int colspan=1)"""
        return __core.GBSpan_Set(*args, **kwargs)

    def Get(*args, **kwargs):
        """Get(self) -> PyObject"""
        return __core.GBSpan_Get(*args, **kwargs)

    asTuple = wx.deprecated(Get, "asTuple is deprecated, use `Get` instead")
    def __str__(self):                   return str(self.Get())
    def __repr__(self):                  return 'wx.GBSpan'+str(self.Get())
    def __len__(self):                   return len(self.Get())
    def __getitem__(self, index):        return self.Get()[index]
    def __setitem__(self, index, val):
        if index == 0: self.SetRowspan(val)
        elif index == 1: self.SetColspan(val)
        else: raise IndexError
    def __nonzero__(self):               return self.Get() != (0,0)
    __safe_for_unpickling__ = True
    def __reduce__(self):                return (wx.GBSpan, self.Get())

    rowspan = property(GetRowspan, SetRowspan)
    colspan = property(GetColspan, SetColspan)

__core.GBSpan_swigregister(GBSpan)

class GBSizerItem(SizerItem):
    """
    The wx.GBSizerItem class is used to track the additional data about
    items in a `wx.GridBagSizer` such as the item's position in the grid
    and how many rows or columns it spans.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self) -> GBSizerItem

        Constructs an empty wx.GBSizerItem.  Either a window, sizer or spacer
        size will need to be set, as well as a position and span before this
        item can be used in a Sizer.

        You will probably never need to create a wx.GBSizerItem directly as they
        are created automatically when the sizer's Add method is called.
        """
        this = __core.new_GBSizerItem(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_GBSizerItem
    __del__ = lambda self : None;
    def GetPos(*args, **kwargs):
        """
        GetPos(self) -> GBPosition

        Get the grid position of the item
        """
        return __core.GBSizerItem_GetPos(*args, **kwargs)

    def GetPosTuple(self): return self.GetPos().Get() 
    def GetSpan(*args, **kwargs):
        """
        GetSpan(self) -> GBSpan

        Get the row and column spanning of the item
        """
        return __core.GBSizerItem_GetSpan(*args, **kwargs)

    def GetSpanTuple(self): return self.GetSpan().Get() 
    def SetPos(*args, **kwargs):
        """
        SetPos(self, GBPosition pos) -> bool

        If the item is already a member of a sizer then first ensure that
        there is no other item that would intersect with this one at the new
        position, then set the new position.  Returns True if the change is
        successful and after the next Layout() the item will be moved.
        """
        return __core.GBSizerItem_SetPos(*args, **kwargs)

    def SetSpan(*args, **kwargs):
        """
        SetSpan(self, GBSpan span) -> bool

        If the item is already a member of a sizer then first ensure that
        there is no other item that would intersect with this one with its new
        spanning size, then set the new spanning.  Returns True if the change
        is successful and after the next Layout() the item will be resized.

        """
        return __core.GBSizerItem_SetSpan(*args, **kwargs)

    def Intersects(*args, **kwargs):
        """
        Intersects(self, GBSizerItem other) -> bool

        Returns True if this item and the other item instersect.
        """
        return __core.GBSizerItem_Intersects(*args, **kwargs)

    def IntersectsPos(*args, **kwargs):
        """
        IntersectsPos(self, GBPosition pos, GBSpan span) -> bool

        Returns True if the given pos/span would intersect with this item.
        """
        return __core.GBSizerItem_IntersectsPos(*args, **kwargs)

    def GetEndPos(*args, **kwargs):
        """
        GetEndPos(self) -> GBPosition

        Get the row and column of the endpoint of this item.
        """
        return __core.GBSizerItem_GetEndPos(*args, **kwargs)

    def GetGBSizer(*args, **kwargs):
        """
        GetGBSizer(self) -> GridBagSizer

        Get the sizer this item is a member of.
        """
        return __core.GBSizerItem_GetGBSizer(*args, **kwargs)

    def SetGBSizer(*args, **kwargs):
        """
        SetGBSizer(self, GridBagSizer sizer)

        Set the sizer this item is a member of.
        """
        return __core.GBSizerItem_SetGBSizer(*args, **kwargs)

    EndPos = property(GetEndPos,doc="See `GetEndPos`") 
    GBSizer = property(GetGBSizer,SetGBSizer,doc="See `GetGBSizer` and `SetGBSizer`") 
    Pos = property(GetPos,SetPos,doc="See `GetPos` and `SetPos`") 
    Span = property(GetSpan,SetSpan,doc="See `GetSpan` and `SetSpan`") 
__core.GBSizerItem_swigregister(GBSizerItem)
DefaultSpan = cvar.DefaultSpan

def GBSizerItemWindow(*args, **kwargs):
    """
    GBSizerItemWindow(Window window, GBPosition pos, GBSpan span=DefaultSpan, 
        int flag=0, int border=0, PyObject userData=None) -> GBSizerItem

    Construct a `wx.GBSizerItem` for a window.
    """
    val = __core.new_GBSizerItemWindow(*args, **kwargs)
    return val

def GBSizerItemSizer(*args, **kwargs):
    """
    GBSizerItemSizer(Sizer sizer, GBPosition pos, GBSpan span=DefaultSpan, 
        int flag=0, int border=0, PyObject userData=None) -> GBSizerItem

    Construct a `wx.GBSizerItem` for a sizer
    """
    val = __core.new_GBSizerItemSizer(*args, **kwargs)
    return val

def GBSizerItemSpacer(*args, **kwargs):
    """
    GBSizerItemSpacer(int width, int height, GBPosition pos, GBSpan span=DefaultSpan, 
        int flag=0, int border=0, PyObject userData=None) -> GBSizerItem

    Construct a `wx.GBSizerItem` for a spacer.
    """
    val = __core.new_GBSizerItemSpacer(*args, **kwargs)
    return val

class GBSizerItemList_iterator(object):
    """This class serves as an iterator for a wxGBSizerItemList object."""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_GBSizerItemList_iterator
    __del__ = lambda self : None;
    def next(*args, **kwargs):
        """next(self) -> GBSizerItem"""
        return __core.GBSizerItemList_iterator_next(*args, **kwargs)

__core.GBSizerItemList_iterator_swigregister(GBSizerItemList_iterator)

class GBSizerItemList(object):
    """
    This class wraps a wxList-based class and gives it a Python
    sequence-like interface.  Sequence operations supported are length,
    index access and iteration.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_GBSizerItemList
    __del__ = lambda self : None;
    def __len__(*args, **kwargs):
        """__len__(self) -> size_t"""
        return __core.GBSizerItemList___len__(*args, **kwargs)

    def __getitem__(*args, **kwargs):
        """__getitem__(self, size_t index) -> GBSizerItem"""
        return __core.GBSizerItemList___getitem__(*args, **kwargs)

    def __contains__(*args, **kwargs):
        """__contains__(self, GBSizerItem obj) -> bool"""
        return __core.GBSizerItemList___contains__(*args, **kwargs)

    def __iter__(*args, **kwargs):
        """__iter__(self) -> GBSizerItemList_iterator"""
        return __core.GBSizerItemList___iter__(*args, **kwargs)

    def index(*args, **kwargs):
        """index(self, GBSizerItem obj) -> int"""
        return __core.GBSizerItemList_index(*args, **kwargs)

    def __repr__(self):
        return "wxGBSizerItemList: " + repr(list(self))

__core.GBSizerItemList_swigregister(GBSizerItemList)

class GridBagSizer(FlexGridSizer):
    """
    A `wx.Sizer` that can lay out items in a virtual grid like a
    `wx.FlexGridSizer` but in this case explicit positioning of the items
    is allowed using `wx.GBPosition`, and items can optionally span more
    than one row and/or column using `wx.GBSpan`.  The total size of the
    virtual grid is determined by the largest row and column that items are
    positioned at, adjusted for spanning.

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, int vgap=0, int hgap=0) -> GridBagSizer

        Constructor, with optional parameters to specify the gap between the
        rows and columns.
        """
        this = __core.new_GridBagSizer(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
        self._setOORInfo(self)

    def Add(*args, **kwargs):
        """
        Add(self, item, GBPosition pos, GBSpan span=DefaultSpan, int flag=0,
        int border=0, userData=None) -> wx.GBSizerItem

        Adds an item to the sizer at the grid cell *pos*, optionally spanning
        more than one row or column as specified with *span*.  The remaining
        args behave similarly to `wx.Sizer.Add`.

        Returns True if the item was successfully placed at the given cell
        position, False if something was already there.

        """
        return __core.GridBagSizer_Add(*args, **kwargs)

    def AddItem(*args, **kwargs):
        """
        Add(self, GBSizerItem item) -> wx.GBSizerItem

        Add an item to the sizer using a `wx.GBSizerItem`.  Returns True if
        the item was successfully placed at its given cell position, False if
        something was already there.
        """
        return __core.GridBagSizer_AddItem(*args, **kwargs)

    def GetCellSize(*args, **kwargs):
        """
        GetCellSize(self, int row, int col) -> Size

        Get the size of the specified cell, including hgap and
        vgap.  Only valid after a Layout.
        """
        return __core.GridBagSizer_GetCellSize(*args, **kwargs)

    def GetEmptyCellSize(*args, **kwargs):
        """
        GetEmptyCellSize(self) -> Size

        Get the size used for cells in the grid with no item.
        """
        return __core.GridBagSizer_GetEmptyCellSize(*args, **kwargs)

    def SetEmptyCellSize(*args, **kwargs):
        """
        SetEmptyCellSize(self, Size sz)

        Set the size used for cells in the grid with no item.
        """
        return __core.GridBagSizer_SetEmptyCellSize(*args, **kwargs)

    def GetItemPosition(*args):
        """
        GetItemPosition(self, item) -> GBPosition

        Get the grid position of the specified *item* where *item* is either a
        window or subsizer that is a member of this sizer, or a zero-based
        index of an item.
        """
        return __core.GridBagSizer_GetItemPosition(*args)

    def SetItemPosition(*args):
        """
        SetItemPosition(self, item, GBPosition pos) -> bool

        Set the grid position of the specified *item* where *item* is either a
        window or subsizer that is a member of this sizer, or a zero-based
        index of an item.  Returns True on success.  If the move is not
        allowed (because an item is already there) then False is returned.

        """
        return __core.GridBagSizer_SetItemPosition(*args)

    def GetItemSpan(*args):
        """
        GetItemSpan(self, item) -> GBSpan

        Get the row/col spanning of the specified *item* where *item* is
        either a window or subsizer that is a member of this sizer, or a
        zero-based index of an item.
        """
        return __core.GridBagSizer_GetItemSpan(*args)

    def SetItemSpan(*args):
        """
        SetItemSpan(self, item, GBSpan span) -> bool

        Set the row/col spanning of the specified *item* where *item* is
        either a window or subsizer that is a member of this sizer, or a
        zero-based index of an item.  Returns True on success.  If the move is
        not allowed (because an item is already there) then False is returned.
        """
        return __core.GridBagSizer_SetItemSpan(*args)

    def FindItem(*args):
        """
        FindItem(self, item) -> GBSizerItem

        Find the sizer item for the given window or subsizer, returns None if
        not found. (non-recursive)
        """
        return __core.GridBagSizer_FindItem(*args)

    def GetItem(self, item):
        gbsi = None
        si = wx.FlexGridSizer.GetItem(self, item)
        if not si:
            return None
        if type(item) is not int:
            gbsi = self.FindItem(item)
        if gbsi: return gbsi
        return si

    def FindItemAtPosition(*args, **kwargs):
        """
        FindItemAtPosition(self, GBPosition pos) -> GBSizerItem

        Return the sizer item for the given grid cell, or None if there is no
        item at that position. (non-recursive)
        """
        return __core.GridBagSizer_FindItemAtPosition(*args, **kwargs)

    def FindItemAtPoint(*args, **kwargs):
        """
        FindItemAtPoint(self, Point pt) -> GBSizerItem

        Return the sizer item located at the point given in *pt*, or None if
        there is no item at that point. The (x,y) coordinates in pt correspond
        to the client coordinates of the window using the sizer for
        layout. (non-recursive)
        """
        return __core.GridBagSizer_FindItemAtPoint(*args, **kwargs)

    def GetChildren(*args, **kwargs):
        """
        GetChildren(self) -> GBSizerItemList

        Returns all of the `wx.GBSizerItem` objects managed by the sizer in a
        list-like object.
        """
        return __core.GridBagSizer_GetChildren(*args, **kwargs)

    def CheckForIntersection(*args, **kwargs):
        """
        CheckForIntersection(self, GBSizerItem item, GBSizerItem excludeItem=None) -> bool

        Look at all items and see if any intersect (or would overlap) the
        given *item*.  Returns True if so, False if there would be no overlap.
        If an *excludeItem* is given then it will not be checked for
        intersection, for example it may be the item we are checking the
        position of.

        """
        return __core.GridBagSizer_CheckForIntersection(*args, **kwargs)

    def CheckForIntersectionPos(*args, **kwargs):
        """
        CheckForIntersectionPos(self, GBPosition pos, GBSpan span, GBSizerItem excludeItem=None) -> bool

        Look at all items and see if any intersect (or would overlap) the
        given position and span.  Returns True if so, False if there would be
        no overlap.  If an *excludeItem* is given then it will not be checked
        for intersection, for example it may be the item we are checking the
        position of.
        """
        return __core.GridBagSizer_CheckForIntersectionPos(*args, **kwargs)

__core.GridBagSizer_swigregister(GridBagSizer)

#---------------------------------------------------------------------------

Left = __core.Left
Top = __core.Top
Right = __core.Right
Bottom = __core.Bottom
Width = __core.Width
Height = __core.Height
Centre = __core.Centre
Center = __core.Center
CentreX = __core.CentreX
CentreY = __core.CentreY
Unconstrained = __core.Unconstrained
AsIs = __core.AsIs
PercentOf = __core.PercentOf
Above = __core.Above
Below = __core.Below
LeftOf = __core.LeftOf
RightOf = __core.RightOf
SameAs = __core.SameAs
Absolute = __core.Absolute
class IndividualLayoutConstraint(Object):
    """
    Objects of this class are stored in the `wx.LayoutConstraints` class as
    one of eight possible constraints that a window can be involved in.
    You will never need to create an instance of
    wx.IndividualLayoutConstraint, rather you should create a
    `wx.LayoutConstraints` instance and use the individual contstraints
    that it contains.
    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def Set(*args, **kwargs):
        """
        Set(self, int rel, Window otherW, int otherE, int val=0, int marg=wxLAYOUT_DEFAULT_MARGIN)

        Sets the properties of the constraint. Normally called by one of the
        convenience functions such as Above, RightOf, SameAs.
        """
        return __core.IndividualLayoutConstraint_Set(*args, **kwargs)

    def LeftOf(*args, **kwargs):
        """
        LeftOf(self, Window sibling, int marg=0)

        Constrains this edge to be to the left of the given window, with an
        optional margin. Implicitly, this is relative to the left edge of the
        other window.
        """
        return __core.IndividualLayoutConstraint_LeftOf(*args, **kwargs)

    def RightOf(*args, **kwargs):
        """
        RightOf(self, Window sibling, int marg=0)

        Constrains this edge to be to the right of the given window, with an
        optional margin. Implicitly, this is relative to the right edge of the
        other window.
        """
        return __core.IndividualLayoutConstraint_RightOf(*args, **kwargs)

    def Above(*args, **kwargs):
        """
        Above(self, Window sibling, int marg=0)

        Constrains this edge to be above the given window, with an optional
        margin. Implicitly, this is relative to the top edge of the other
        window.
        """
        return __core.IndividualLayoutConstraint_Above(*args, **kwargs)

    def Below(*args, **kwargs):
        """
        Below(self, Window sibling, int marg=0)

        Constrains this edge to be below the given window, with an optional
        margin. Implicitly, this is relative to the bottom edge of the other
        window.
        """
        return __core.IndividualLayoutConstraint_Below(*args, **kwargs)

    def SameAs(*args, **kwargs):
        """
        SameAs(self, Window otherW, int edge, int marg=0)

        Constrains this edge or dimension to be to the same as the edge of the
        given window, with an optional margin.
        """
        return __core.IndividualLayoutConstraint_SameAs(*args, **kwargs)

    def PercentOf(*args, **kwargs):
        """
        PercentOf(self, Window otherW, int wh, int per)

        Constrains this edge or dimension to be to a percentage of the given
        window, with an optional margin.
        """
        return __core.IndividualLayoutConstraint_PercentOf(*args, **kwargs)

    def Absolute(*args, **kwargs):
        """
        Absolute(self, int val)

        Constrains this edge or dimension to be the given absolute value.
        """
        return __core.IndividualLayoutConstraint_Absolute(*args, **kwargs)

    def Unconstrained(*args, **kwargs):
        """
        Unconstrained(self)

        Sets this edge or dimension to be unconstrained, that is, dependent on
        other edges and dimensions from which this value can be deduced.
        """
        return __core.IndividualLayoutConstraint_Unconstrained(*args, **kwargs)

    def AsIs(*args, **kwargs):
        """
        AsIs(self)

        Sets this edge or constraint to be whatever the window's value is at
        the moment. If either of the width and height constraints are *as is*,
        the window will not be resized, but moved instead. This is important
        when considering panel items which are intended to have a default
        size, such as a button, which may take its size from the size of the
        button label.
        """
        return __core.IndividualLayoutConstraint_AsIs(*args, **kwargs)

    def GetOtherWindow(*args, **kwargs):
        """GetOtherWindow(self) -> Window"""
        return __core.IndividualLayoutConstraint_GetOtherWindow(*args, **kwargs)

    def GetMyEdge(*args, **kwargs):
        """GetMyEdge(self) -> int"""
        return __core.IndividualLayoutConstraint_GetMyEdge(*args, **kwargs)

    def SetEdge(*args, **kwargs):
        """SetEdge(self, int which)"""
        return __core.IndividualLayoutConstraint_SetEdge(*args, **kwargs)

    def SetValue(*args, **kwargs):
        """SetValue(self, int v)"""
        return __core.IndividualLayoutConstraint_SetValue(*args, **kwargs)

    def GetMargin(*args, **kwargs):
        """GetMargin(self) -> int"""
        return __core.IndividualLayoutConstraint_GetMargin(*args, **kwargs)

    def SetMargin(*args, **kwargs):
        """SetMargin(self, int m)"""
        return __core.IndividualLayoutConstraint_SetMargin(*args, **kwargs)

    def GetValue(*args, **kwargs):
        """GetValue(self) -> int"""
        return __core.IndividualLayoutConstraint_GetValue(*args, **kwargs)

    def GetPercent(*args, **kwargs):
        """GetPercent(self) -> int"""
        return __core.IndividualLayoutConstraint_GetPercent(*args, **kwargs)

    def GetOtherEdge(*args, **kwargs):
        """GetOtherEdge(self) -> int"""
        return __core.IndividualLayoutConstraint_GetOtherEdge(*args, **kwargs)

    def GetDone(*args, **kwargs):
        """GetDone(self) -> bool"""
        return __core.IndividualLayoutConstraint_GetDone(*args, **kwargs)

    def SetDone(*args, **kwargs):
        """SetDone(self, bool d)"""
        return __core.IndividualLayoutConstraint_SetDone(*args, **kwargs)

    def GetRelationship(*args, **kwargs):
        """GetRelationship(self) -> int"""
        return __core.IndividualLayoutConstraint_GetRelationship(*args, **kwargs)

    def SetRelationship(*args, **kwargs):
        """SetRelationship(self, int r)"""
        return __core.IndividualLayoutConstraint_SetRelationship(*args, **kwargs)

    def ResetIfWin(*args, **kwargs):
        """
        ResetIfWin(self, Window otherW) -> bool

        Reset constraint if it mentions otherWin
        """
        return __core.IndividualLayoutConstraint_ResetIfWin(*args, **kwargs)

    def SatisfyConstraint(*args, **kwargs):
        """
        SatisfyConstraint(self, LayoutConstraints constraints, Window win) -> bool

        Try to satisfy constraint
        """
        return __core.IndividualLayoutConstraint_SatisfyConstraint(*args, **kwargs)

    def GetEdge(*args, **kwargs):
        """
        GetEdge(self, int which, Window thisWin, Window other) -> int

        Get the value of this edge or dimension, or if this
        is not determinable, -1.
        """
        return __core.IndividualLayoutConstraint_GetEdge(*args, **kwargs)

    Done = property(GetDone,SetDone,doc="See `GetDone` and `SetDone`") 
    Margin = property(GetMargin,SetMargin,doc="See `GetMargin` and `SetMargin`") 
    MyEdge = property(GetMyEdge,doc="See `GetMyEdge`") 
    OtherEdge = property(GetOtherEdge,doc="See `GetOtherEdge`") 
    OtherWindow = property(GetOtherWindow,doc="See `GetOtherWindow`") 
    Percent = property(GetPercent,doc="See `GetPercent`") 
    Relationship = property(GetRelationship,SetRelationship,doc="See `GetRelationship` and `SetRelationship`") 
    Value = property(GetValue,SetValue,doc="See `GetValue` and `SetValue`") 
__core.IndividualLayoutConstraint_swigregister(IndividualLayoutConstraint)

class LayoutConstraints(Object):
    """
    **Note:** constraints are now deprecated and you should use sizers
    instead.

    Objects of this class can be associated with a window to define its
    layout constraints, with respect to siblings or its parent.

    The class consists of the following eight constraints of class
    wx.IndividualLayoutConstraint, some or all of which should be accessed
    directly to set the appropriate constraints.

        * left: represents the left hand edge of the window
        * right: represents the right hand edge of the window
        * top: represents the top edge of the window
        * bottom: represents the bottom edge of the window
        * width: represents the width of the window
        * height: represents the height of the window
        * centreX: represents the horizontal centre point of the window
        * centreY: represents the vertical centre point of the window 

    Most constraints are initially set to have the relationship
    wxUnconstrained, which means that their values should be calculated by
    looking at known constraints. The exceptions are width and height,
    which are set to wxAsIs to ensure that if the user does not specify a
    constraint, the existing width and height will be used, to be
    compatible with panel items which often have take a default size. If
    the constraint is ``wx.AsIs``, the dimension will not be changed.

    :see: `wx.IndividualLayoutConstraint`, `wx.Window.SetConstraints`

    """
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    left = property(__core.LayoutConstraints_left_get)
    top = property(__core.LayoutConstraints_top_get)
    right = property(__core.LayoutConstraints_right_get)
    bottom = property(__core.LayoutConstraints_bottom_get)
    width = property(__core.LayoutConstraints_width_get)
    height = property(__core.LayoutConstraints_height_get)
    centreX = property(__core.LayoutConstraints_centreX_get)
    centreY = property(__core.LayoutConstraints_centreY_get)
    def __init__(self, *args, **kwargs): 
        """__init__(self) -> LayoutConstraints"""
        this = __core.new_LayoutConstraints(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = __core.delete_LayoutConstraints
    __del__ = lambda self : None;
    def SatisfyConstraints(*args, **kwargs):
        """SatisfyConstraints(Window win) -> (areSatisfied, noChanges)"""
        return __core.LayoutConstraints_SatisfyConstraints(*args, **kwargs)

    def AreSatisfied(*args, **kwargs):
        """AreSatisfied(self) -> bool"""
        return __core.LayoutConstraints_AreSatisfied(*args, **kwargs)

__core.LayoutConstraints_swigregister(LayoutConstraints)

#---------------------------------------------------------------------------

COL_WIDTH_DEFAULT = __core.COL_WIDTH_DEFAULT
COL_WIDTH_AUTOSIZE = __core.COL_WIDTH_AUTOSIZE
COL_RESIZABLE = __core.COL_RESIZABLE
COL_SORTABLE = __core.COL_SORTABLE
COL_REORDERABLE = __core.COL_REORDERABLE
COL_HIDDEN = __core.COL_HIDDEN
COL_DEFAULT_FLAGS = __core.COL_DEFAULT_FLAGS
class HeaderColumn(object):
    """Proxy of C++ HeaderColumn class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = __core.delete_HeaderColumn
    __del__ = lambda self : None;
    def GetTitle(*args, **kwargs):
        """GetTitle(self) -> String"""
        return __core.HeaderColumn_GetTitle(*args, **kwargs)

    def GetBitmap(*args, **kwargs):
        """GetBitmap(self) -> Bitmap"""
        return __core.HeaderColumn_GetBitmap(*args, **kwargs)

    def GetWidth(*args, **kwargs):
        """GetWidth(self) -> int"""
        return __core.HeaderColumn_GetWidth(*args, **kwargs)

    def GetMinWidth(*args, **kwargs):
        """GetMinWidth(self) -> int"""
        return __core.HeaderColumn_GetMinWidth(*args, **kwargs)

    def GetAlignment(*args, **kwargs):
        """GetAlignment(self) -> int"""
        return __core.HeaderColumn_GetAlignment(*args, **kwargs)

    def GetFlags(*args, **kwargs):
        """GetFlags(self) -> int"""
        return __core.HeaderColumn_GetFlags(*args, **kwargs)

    def HasFlag(*args, **kwargs):
        """HasFlag(self, int flag) -> bool"""
        return __core.HeaderColumn_HasFlag(*args, **kwargs)

    def IsResizeable(*args, **kwargs):
        """IsResizeable(self) -> bool"""
        return __core.HeaderColumn_IsResizeable(*args, **kwargs)

    def IsSortable(*args, **kwargs):
        """IsSortable(self) -> bool"""
        return __core.HeaderColumn_IsSortable(*args, **kwargs)

    def IsReorderable(*args, **kwargs):
        """IsReorderable(self) -> bool"""
        return __core.HeaderColumn_IsReorderable(*args, **kwargs)

    def IsHidden(*args, **kwargs):
        """IsHidden(self) -> bool"""
        return __core.HeaderColumn_IsHidden(*args, **kwargs)

    def IsShown(*args, **kwargs):
        """IsShown(self) -> bool"""
        return __core.HeaderColumn_IsShown(*args, **kwargs)

    def IsSortKey(*args, **kwargs):
        """IsSortKey(self) -> bool"""
        return __core.HeaderColumn_IsSortKey(*args, **kwargs)

    def IsSortOrderAscending(*args, **kwargs):
        """IsSortOrderAscending(self) -> bool"""
        return __core.HeaderColumn_IsSortOrderAscending(*args, **kwargs)

    Title = property(GetTitle) 
    Bitmap = property(GetBitmap) 
    Width = property(GetWidth) 
    MinWidth = property(GetMinWidth) 
    Alignment = property(GetAlignment) 
    Flags = property(GetFlags) 
    Resizeable = property(IsResizeable) 
    Sortable = property(IsSortable) 
    Reorderable = property(IsReorderable) 
    Hidden = property(IsHidden) 
    Shown = property(IsShown) 
    SortOrderAscending = property(IsSortOrderAscending) 
    SortKey = property(IsSortKey) 
__core.HeaderColumn_swigregister(HeaderColumn)

class SettableHeaderColumn(HeaderColumn):
    """Proxy of C++ SettableHeaderColumn class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    def SetTitle(*args, **kwargs):
        """SetTitle(self, String title)"""
        return __core.SettableHeaderColumn_SetTitle(*args, **kwargs)

    def SetBitmap(*args, **kwargs):
        """SetBitmap(self, Bitmap bitmap)"""
        return __core.SettableHeaderColumn_SetBitmap(*args, **kwargs)

    def SetWidth(*args, **kwargs):
        """SetWidth(self, int width)"""
        return __core.SettableHeaderColumn_SetWidth(*args, **kwargs)

    def SetMinWidth(*args, **kwargs):
        """SetMinWidth(self, int minWidth)"""
        return __core.SettableHeaderColumn_SetMinWidth(*args, **kwargs)

    def SetAlignment(*args, **kwargs):
        """SetAlignment(self, int align)"""
        return __core.SettableHeaderColumn_SetAlignment(*args, **kwargs)

    def SetFlags(*args, **kwargs):
        """SetFlags(self, int flags)"""
        return __core.SettableHeaderColumn_SetFlags(*args, **kwargs)

    def ChangeFlag(*args, **kwargs):
        """ChangeFlag(self, int flag, bool set)"""
        return __core.SettableHeaderColumn_ChangeFlag(*args, **kwargs)

    def SetFlag(*args, **kwargs):
        """SetFlag(self, int flag)"""
        return __core.SettableHeaderColumn_SetFlag(*args, **kwargs)

    def ClearFlag(*args, **kwargs):
        """ClearFlag(self, int flag)"""
        return __core.SettableHeaderColumn_ClearFlag(*args, **kwargs)

    def ToggleFlag(*args, **kwargs):
        """ToggleFlag(self, int flag)"""
        return __core.SettableHeaderColumn_ToggleFlag(*args, **kwargs)

    def SetResizeable(*args, **kwargs):
        """SetResizeable(self, bool resizeable)"""
        return __core.SettableHeaderColumn_SetResizeable(*args, **kwargs)

    def SetSortable(*args, **kwargs):
        """SetSortable(self, bool sortable)"""
        return __core.SettableHeaderColumn_SetSortable(*args, **kwargs)

    def SetReorderable(*args, **kwargs):
        """SetReorderable(self, bool reorderable)"""
        return __core.SettableHeaderColumn_SetReorderable(*args, **kwargs)

    def SetHidden(*args, **kwargs):
        """SetHidden(self, bool hidden)"""
        return __core.SettableHeaderColumn_SetHidden(*args, **kwargs)

    def UnsetAsSortKey(*args, **kwargs):
        """UnsetAsSortKey(self)"""
        return __core.SettableHeaderColumn_UnsetAsSortKey(*args, **kwargs)

    def SetSortOrder(*args, **kwargs):
        """SetSortOrder(self, bool ascending)"""
        return __core.SettableHeaderColumn_SetSortOrder(*args, **kwargs)

    def ToggleSortOrder(*args, **kwargs):
        """ToggleSortOrder(self)"""
        return __core.SettableHeaderColumn_ToggleSortOrder(*args, **kwargs)

    Title = property(HeaderColumn.GetTitle,SetTitle) 
    Bitmap = property(HeaderColumn.GetBitmap,SetBitmap) 
    Width = property(HeaderColumn.GetWidth,SetWidth) 
    MinWidth = property(HeaderColumn.GetMinWidth,SetMinWidth) 
    Alignment = property(HeaderColumn.GetAlignment,SetAlignment) 
    Flags = property(HeaderColumn.GetFlags,SetFlags) 
    Resizeable = property(HeaderColumn.IsResizeable,SetResizeable) 
    Sortable = property(HeaderColumn.IsSortable,SetSortable) 
    Reorderable = property(HeaderColumn.IsReorderable,SetReorderable) 
    Hidden = property(HeaderColumn.IsHidden,SetHidden) 
    SortKey = property(HeaderColumn.IsSortKey) 
__core.SettableHeaderColumn_swigregister(SettableHeaderColumn)

class HeaderColumnSimple(SettableHeaderColumn):
    """Proxy of C++ HeaderColumnSimple class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, PyObject title_or_bitmap, int width=COL_WIDTH_DEFAULT, 
            int align=ALIGN_NOT, int flags=COL_DEFAULT_FLAGS) -> HeaderColumnSimple
        """
        this = __core.new_HeaderColumnSimple(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
__core.HeaderColumnSimple_swigregister(HeaderColumnSimple)

#---------------------------------------------------------------------------

class VersionInfo(object):
    """Proxy of C++ VersionInfo class"""
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        __init__(self, String name, int major, int minor, int micro=0, String description=wxEmptyString, 
            String copyright=wxEmptyString) -> VersionInfo
        """
        this = __core.new_VersionInfo(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    def GetName(*args, **kwargs):
        """GetName(self) -> String"""
        return __core.VersionInfo_GetName(*args, **kwargs)

    def GetMajor(*args, **kwargs):
        """GetMajor(self) -> int"""
        return __core.VersionInfo_GetMajor(*args, **kwargs)

    def GetMinor(*args, **kwargs):
        """GetMinor(self) -> int"""
        return __core.VersionInfo_GetMinor(*args, **kwargs)

    def GetMicro(*args, **kwargs):
        """GetMicro(self) -> int"""
        return __core.VersionInfo_GetMicro(*args, **kwargs)

    def ToString(*args, **kwargs):
        """ToString(self) -> String"""
        return __core.VersionInfo_ToString(*args, **kwargs)

    def GetVersionString(*args, **kwargs):
        """GetVersionString(self) -> String"""
        return __core.VersionInfo_GetVersionString(*args, **kwargs)

    def HasDescription(*args, **kwargs):
        """HasDescription(self) -> bool"""
        return __core.VersionInfo_HasDescription(*args, **kwargs)

    def GetDescription(*args, **kwargs):
        """GetDescription(self) -> String"""
        return __core.VersionInfo_GetDescription(*args, **kwargs)

    def HasCopyright(*args, **kwargs):
        """HasCopyright(self) -> bool"""
        return __core.VersionInfo_HasCopyright(*args, **kwargs)

    def GetCopyright(*args, **kwargs):
        """GetCopyright(self) -> String"""
        return __core.VersionInfo_GetCopyright(*args, **kwargs)

__core.VersionInfo_swigregister(VersionInfo)

#----------------------------------------------------------------------------

# Use Python's bool constants if available, make some if not
try:
    True
except NameError:
    __builtins__.True = 1==1
    __builtins__.False = 1==0
    def bool(value): return not not value
    __builtins__.bool = bool



# workarounds for bad wxRTTI names
__wxPyPtrTypeMap['wxGauge95']    = 'wxGauge'
__wxPyPtrTypeMap['wxSlider95']   = 'wxSlider'
__wxPyPtrTypeMap['wxStatusBar95']   = 'wxStatusBar'


#----------------------------------------------------------------------------
# Load version numbers from __version__...  Ensure that major and minor
# versions are the same for both wxPython and wxWidgets.

from __version__ import *
__version__ = VERSION_STRING

assert MAJOR_VERSION == _core_.MAJOR_VERSION, "wxPython/wxWidgets version mismatch"
assert MINOR_VERSION == _core_.MINOR_VERSION, "wxPython/wxWidgets version mismatch"
if RELEASE_VERSION != _core_.RELEASE_VERSION:
    import warnings
    warnings.warn("wxPython/wxWidgets release number mismatch")


def version():
    """Returns a string containing version and port info"""
    if wx.Platform == '__WXMSW__':
        port = 'msw'
    elif wx.Platform == '__WXMAC__':
        if 'wxOSX-carbon' in wx.PlatformInfo:
            port = 'osx-carbon'
        else:
            port = 'osx-cocoa'
    elif wx.Platform == '__WXGTK__':
        port = 'gtk'
        if 'gtk2' in wx.PlatformInfo:
            port = 'gtk2'
        elif 'gtk3' in wx.PlatformInfo:
            port = 'gtk3'
    else:
        port = '?'

    return "%s %s (classic)" % (wx.VERSION_STRING, port)
                      
    
#----------------------------------------------------------------------------

# Set wxPython's default string<-->unicode conversion encoding from
# the locale, but only if Python's default hasn't been changed.  (We
# assume that if the user has customized it already then that is the
# encoding we need to use as well.)
#
# The encoding selected here is used when string or unicode objects
# need to be converted in order to pass them to wxWidgets.  Please be
# aware that the default encoding within the same locale may be
# slightly different on different platforms.  For example, please see
# http://www.alanwood.net/demos/charsetdiffs.html for differences
# between the common latin/roman encodings.

default = _sys.getdefaultencoding()
if default == 'ascii':
    import locale
    import codecs
    try:
        if hasattr(locale, 'getpreferredencoding'):
            default = locale.getpreferredencoding()
        else:
            default = locale.getdefaultlocale()[1]
        codecs.lookup(default)
    except (ValueError, LookupError, TypeError):
        default = _sys.getdefaultencoding()
    del locale
    del codecs
if default:
    wx.SetDefaultPyEncoding(default)
del default

#----------------------------------------------------------------------------

class PyDeadObjectError(AttributeError):
    pass

class _wxPyDeadObject(object):
    """
    Instances of wx objects that are OOR capable will have their __class__
    changed to this class when the C++ object is deleted.  This should help
    prevent crashes due to referencing a bogus C++ pointer.
    """
    reprStr = "wxPython wrapper for DELETED %s object! (The C++ object no longer exists.)"
    attrStr = "The C++ part of the %s object has been deleted, attribute access no longer allowed."

    def __repr__(self):
        if not hasattr(self, "_name"):
            self._name = "[unknown]"
        return self.reprStr % self._name

    def __getattr__(self, *args):
        if not hasattr(self, "_name"):
            self._name = "[unknown]"
        raise PyDeadObjectError(self.attrStr % self._name)

    def __nonzero__(self):
        return 0



class PyUnbornObjectError(AttributeError):
    pass

class _wxPyUnbornObject(object):
    """
    Some stock objects are created when the wx._core module is
    imported, but their C++ instance is not created until the wx.App
    object is created and initialized.  These object instances will
    temporarily have their __class__ changed to this class so an
    exception will be raised if they are used before the C++ instance
    is ready.
    """

    reprStr = "wxPython wrapper for UNBORN object! (The C++ object is not initialized yet.)"
    attrStr = "The C++ part of this object has not been initialized, attribute access not allowed."

    def __repr__(self):
        #if not hasattr(self, "_name"):
        #    self._name = "[unknown]"
        return self.reprStr #% self._name

    def __getattr__(self, *args):
        #if not hasattr(self, "_name"):
        #    self._name = "[unknown]"
        raise PyUnbornObjectError(self.attrStr) # % self._name )

    def __nonzero__(self):
        return 0


#----------------------------------------------------------------------------

def CallAfter(callableObj, *args, **kw):
    """
    Call the specified function after the current and pending event
    handlers have been completed.  This is also good for making GUI
    method calls from non-GUI threads.  Any extra positional or
    keyword args are passed on to the callable when it is called.

    :see: `wx.CallLater`
    """
    assert callable(callableObj), "callableObj is not callable"
    app = wx.GetApp()
    assert app is not None, 'No wx.App created yet'

    if not hasattr(app, "_CallAfterId"):
        app._CallAfterId = wx.NewEventType()
        app.Connect(-1, -1, app._CallAfterId,
                    lambda event: event.callable(*event.args, **event.kw) )
    evt = wx.PyEvent()
    evt.SetEventType(app._CallAfterId)
    evt.callable = callableObj
    evt.args = args
    evt.kw = kw
    wx.PostEvent(app, evt)

#----------------------------------------------------------------------------


class CallLater:
    """
    A convenience class for `wx.Timer`, that calls the given callable
    object once after the given amount of milliseconds, passing any
    positional or keyword args.  The return value of the callable is
    availbale after it has been run with the `GetResult` method.

    If you don't need to get the return value or restart the timer
    then there is no need to hold a reference to this object.

    :see: `wx.CallAfter`
    """

    __RUNNING = set()
    
    def __init__(self, millis, callableObj, *args, **kwargs):
        assert callable(callableObj), "callableObj is not callable"
        self.millis = millis
        self.callable = callableObj
        self.SetArgs(*args, **kwargs)
        self.runCount = 0
        self.running = False
        self.hasRun = False
        self.result = None
        self.timer = None
        self.Start()


    def Start(self, millis=None, *args, **kwargs):
        """
        (Re)start the timer
        """
        self.hasRun = False
        if millis is not None:
            self.millis = millis
        if args or kwargs:
            self.SetArgs(*args, **kwargs)
        self.Stop()
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(self.millis, wx.TIMER_ONE_SHOT)
        self.running = True
        self.__RUNNING.add(self)
    Restart = Start


    def Stop(self):
        """
        Stop and destroy the timer.
        """
        if self.timer is not None:
            self.timer.Stop()
            self.timer = None
        self.__RUNNING.discard(self)


    def GetInterval(self):
        if self.timer is not None:
            return self.timer.GetInterval()
        else:
            return 0


    def IsRunning(self):
        return self.timer is not None and self.timer.IsRunning()


    def SetArgs(self, *args, **kwargs):
        """
        (Re)set the args passed to the callable object.  This is
        useful in conjunction with Restart if you want to schedule a
        new call to the same callable object but with different
        parameters.
        """
        self.args = args
        self.kwargs = kwargs


    def HasRun(self):
        return self.hasRun

    
    def GetResult(self):
        return self.result

    
    def Notify(self):
        """
        The timer has expired so call the callable.
        """
        if self.callable and getattr(self.callable, 'im_self', True):
            self.runCount += 1
            self.running = False
            self.result = self.callable(*self.args, **self.kwargs)
        self.hasRun = True
        if not self.running:
            # if it wasn't restarted, then cleanup
            wx.CallAfter(self.Stop)

    Interval = property(GetInterval)
    Result = property(GetResult)


class FutureCall(CallLater):
    """A compatibility alias for `CallLater`."""

#----------------------------------------------------------------------------
# Control which items in this module should be documented by epydoc.
# We allow only classes and functions, which will help reduce the size
# of the docs by filtering out the zillions of constants, EVT objects,
# and etc that don't make much sense by themselves, but are instead
# documented (or will be) as part of the classes/functions/methods
# where they should be used.

class __DocFilter:
    """
    A filter for epydoc that only allows non-Ptr classes and
    functions, in order to reduce the clutter in the API docs.
    """
    def __init__(self, globals):
        self._globals = globals
        
    def __call__(self, name):
        import types
        obj = self._globals.get(name, None)

        # only document classes and function
        if type(obj) not in [type, types.ClassType, types.FunctionType, types.BuiltinFunctionType]:
            return False

        # skip other things that are private or will be documented as part of somethign else
        if name.startswith('_') or name.startswith('EVT') or name.endswith('_swigregister')  or name.endswith('Ptr') :
            return False

        # skip functions that are duplicates of static functions in a class
        if name.find('_') != -1:
            cls = self._globals.get(name.split('_')[0], None)
            methname = name.split('_')[1]
            if hasattr(cls, methname) and type(getattr(cls, methname)) is types.FunctionType:
                return False
            
        return True

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------

# Import other modules in this package that should show up in the
# "core" wx namespace
from _gdi import *
from _windows import *
from _controls import *
from _misc import *

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------



