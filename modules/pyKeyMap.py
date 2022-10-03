import pygame
from enum import Enum, unique

@unique
class NyleEnum(Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    I = 'I'
    J = 'J'
    K = 'K'
    L = 'L'
    M = 'M'
    N = 'N'
    O = 'O'
    P = 'P'
    Q = 'Q'
    R = 'R'
    S = 'S'
    T = 'T'
    U = 'U'
    V = 'V'
    W = 'W'
    X = 'X'
    Y = 'Y'
    Z = 'Z'
    ONE = 'ONE'
    TWO = 'TWO'
    THREE = 'THREE'
    FOUR = 'FOUR'
    FIVE = 'FIVE'
    SIX = 'SIX'
    SEVEN = 'SEVEN'
    EIGHT = 'EIGHT'
    NINE = 'NINE'
    ZERO = 'ZERO'
    PERIOD = 'PERIOD'
    COMMA = 'COMMA'
    SLASH = 'SLASH'
    BACKSPACE = 'BACKSPACE'
    SEMICOLON = 'SEMICOLON'
    BACKSLASH = 'BACKSLASH'
    BACKTICK = 'BACKTICK' # `
    SINGLE_QUOTE = 'SINGLE_QUOTE'
    DOUBLE_QUOTE = 'DOUBLE_QUOTE'
    LEFT_BRACKET = 'LEFT_BRACKET' # [
    RIGHT_BRACKET = 'RIGHT_BRACKET'
    MINUS = 'MINUS'
    EQUALS = 'EQUALS'
    ESCAPE = 'ESCAPE'
    TAB = 'TAB'
    CAPS_LOCK = 'CAPS_LOCK'
    LEFT_SHIFT = 'LEFT_SHIFT'
    RIGHT_SHIFT = 'RIGHT_SHIFT'
    LEFT_CONTROL = 'LEFT_CONTROL'
    RIGHT_CONTROL = 'RIGHT_CONTROL'
    LEFT_ALT = 'LEFT_ALT'
    RIGHT_ALT = 'RIGHT_ALT'
    ENTER = 'ENTER'
    FUNCTION = 'FUNCTION'
    PAGE_UP = 'PAGE_UP'
    PAGE_DOWN = 'PAGE_DOWN'
    KEYPAD_ONE = 'KEYPAD_ONE'
    KEYPAD_TWO = 'KEYPAD_TWO'
    KEYPAD_THREE = 'KEYPAD_THREE'
    KEYPAD_FOUR = 'KEYPAD_FOUR'
    KEYPAD_FIVE = 'KEYPAD_FIVE'
    KEYPAD_SIX = 'KEYPAD_SIX'
    KEYPAD_SEVEN = 'KEYPAD_SEVEN'
    KEYPAD_EIGHT = 'KEYPAD_EIGHT'
    KEYPAD_NINE = 'KEYPAD_NINE'
    KEYPAD_ZERO = 'KEYPAD_ZERO'
    KEYPAD_PERIOD = 'KEYPAD_PERIOD'
    KEYPAD_ENTER = 'KEYPAD_ENTER'
    KEYPAD_PLUS = 'KEYPAD_PLUS'
    KEYPAD_MINUS = 'KEYPAD_MINUS'
    KEYPAD_ASTERISK = 'KEYPAD_ASTERISK'
    KEYPAD_SLASH = 'KEYPAD_SLASH'
    NUMLOCK = 'NUMLOCK'
    F1 = 'F1'
    F2 = 'F2'
    F3 = 'F3'
    F4 = 'F4'
    F5 = 'F5'
    F6 = 'F6'
    F7 = 'F7'
    F8 = 'F8'
    F9 = 'F9'
    F10 = 'F10'
    F11 = 'F11'
    F12 = 'F12'
    INSERT = 'INSERT'
    DELETE = 'DELETE'
    SPACE = 'SPACE'

    #The following require the shift key to be pressed

    TILDE = 'TILDE' # ~
    BANG = 'BANG' # !
    AT = 'AT' # @
    HASH = 'HASH'
    DOLLAR = 'DOLLAR'
    PERCENT = 'PERCENT'
    CARET = 'CARET'
    AMPERSAND = 'AMPERSAND'
    ASTERISK = 'ASTERISK'
    LEFT_PARENTHESIS = 'LEFT_PARENTHESIS' # (
    RIGHT_PARENTHESIS = 'RIGHT_PARENTHESIS' # )
    UNDERSCORE = 'UNDERSCORE'
    PLUS = 'PLUS'
    LEFT_BRACE = 'LEFT_BRACE'
    RIGHT_BRACE = 'RIGHT_BRACE'
    PIPE = 'PIPE' # |
    COLON = 'COLON'
    GREATER_THAN = 'GREATER_THAN'
    LESS_THAN = 'LESS_THAN'
    QUESTION_MARK = 'QUESTION_MARK'


requiresShift = [
    NyleEnum.TILDE,
    NyleEnum.AT,
    NyleEnum.HASH,
    NyleEnum.DOLLAR,
    NyleEnum.PERCENT,
    NyleEnum.CARAT,
    NyleEnum.AMPERSAND,
    NyleEnum.ASTERISK,
    NyleEnum.LEFT_PARENTHESIS,
    NyleEnum.RIGHT_PARENTHESIS,
    NyleEnum.MINUS,
    NyleEnum.PLUS,
    NyleEnum.LEFT_PARENTHESIS,
    NyleEnum.RIGHT_PARENTHESIS,
    NyleEnum.UNDERSCORE,
    NyleEnum.PLUS,
    NyleEnum.LEFT_BRACE,
    NyleEnum.RIGHT_BRACE,
    NyleEnum.PIPE,
    NyleEnum.COLON,
    NyleEnum.GREATER_THAN,
    NyleEnum.LESS_THAN,
    NyleEnum.QUESTION_MARK
]

keyConvert = {
    [pygame.K_BACKSPACE]: NyleEnum.BACKSPACE,
    [pygame.K_TAB]: NyleEnum.TAB,
    [pygame.K_RETURN]: NyleEnum.ENTER,
    [pygame.K_ESCAPE]: NyleEnum.ESCAPE,
    [pygame.K_SPACE]: NyleEnum.SPACE,
    [pygame.K_EXCLAIM]: NyleEnum.BANG,
    [pygame.K_QUOTEDBL]: NyleEnum.DOUBLE_QUOTE,
    [pygame.K_HASH]: NyleEnum.HASH,
    [pygame.K_DOLLAR]: NyleEnum.DOLLAR,
    [pygame.K_AMPERSAND]: NyleEnum.AMPERSAND,
    [pygame.K_QUOTE]: NyleEnum.SINGLE_QUOTE,
    [pygame.K_LEFTPAREN]: NyleEnum.LEFT_PARENTHESIS,
    [pygame.K_RIGHTPAREN]: NyleEnum.RIGHT_PARENTHESIS,
    [pygame.K_ASTERISK]: NyleEnum.ASTERISK,
    [pygame.K_PLUS]: NyleEnum.PLUS,
    [pygame.K_COMMA]: NyleEnum.COMMA,
    [pygame.K_MINUS]: NyleEnum.MINUS,
    [pygame.K_PERIOD]: NyleEnum.PERIOD,
    [pygame.K_SLASH]: NyleEnum.SLASH,
    [pygame.K_0]: NyleEnum.ZERO,
    [pygame.K_1]: NyleEnum.ONE,
    [pygame.K_2]: NyleEnum.TWO,
    [pygame.K_3]: NyleEnum.THREE,
    [pygame.K_4]: NyleEnum.FOUR,
    [pygame.K_5]: NyleEnum.FIVE,
    [pygame.K_6]: NyleEnum.SIX,
    [pygame.K_7]: NyleEnum.SEVEN,
    [pygame.K_8]: NyleEnum.EIGHT,
    [pygame.K_9]: NyleEnum.NINE,
    [pygame.K_COLON]: NyleEnum.COLON,
    [pygame.K_SEMICOLON]: NyleEnum.SEMICOLON,
    [pygame.K_LESS]: NyleEnum.LESS_THAN,
    [pygame.K_EQUALS]: NyleEnum.EQUALS,
    [pygame.K_GREATER]: NyleEnum.GREATER_THAN,
    [pygame.K_QUESTION]: NyleEnum.QUESTION_MARK,
    [pygame.K_AT]: NyleEnum.AT,
    [pygame.K_LEFTBRACKET]: NyleEnum.LEFT_BRACKET,
    [pygame.K_BACKSLASH]: NyleEnum.BACKSLASH,
    [pygame.K_RIGHTBRACKET]: NyleEnum.RIGHT_BRACKET,
    [pygame.K_CARET]: NyleEnum.CARET,
    [pygame.K_UNDERSCORE]: NyleEnum.UNDERSCORE,
    [pygame.K_BACKQUOTE]: NyleEnum.TILDE,
    [pygame.K_a]: NyleEnum.A,
    [pygame.K_b]: NyleEnum.B,
    [pygame.K_c]: NyleEnum.C,
    [pygame.K_d]: NyleEnum.D,
    [pygame.K_e]: NyleEnum.E,
    [pygame.K_f]: NyleEnum.F,
    [pygame.K_g]: NyleEnum.G,
    [pygame.K_h]: NyleEnum.H,
    [pygame.K_i]: NyleEnum.I,
    [pygame.K_j]: NyleEnum.J,
    [pygame.K_k]: NyleEnum.K,
    [pygame.K_l]: NyleEnum.L,
    [pygame.K_m]: NyleEnum.M,
    [pygame.K_n]: NyleEnum.N,
    [pygame.K_o]: NyleEnum.O,
    [pygame.K_p]: NyleEnum.P,
    [pygame.K_q]: NyleEnum.Q,
    [pygame.K_r]: NyleEnum.R,
    [pygame.K_s]: NyleEnum.S,
    [pygame.K_t]: NyleEnum.T,
    [pygame.K_u]: NyleEnum.U,
    [pygame.K_v]: NyleEnum.V,
    [pygame.K_w]: NyleEnum.W,
    [pygame.K_x]: NyleEnum.X,
    [pygame.K_y]: NyleEnum.Y,
    [pygame.K_z]: NyleEnum.Z,
    [pygame.K_DELETE]: NyleEnum.DELETE,
    [pygame.K_KP0]: NyleEnum.KEYPAD_ZERO,
    [pygame.K_KP1]: '',
    [pygame.K_KP2]: '',
    [pygame.K_KP3]: '',
    [pygame.K_KP4]: '',
    [pygame.K_KP5]: '',
    [pygame.K_KP6]: '',
    [pygame.K_KP7]: '',
    [pygame.K_KP8]: '',
    [pygame.K_KP9]: '',
    [pygame.K_KP_PERIOD]: '',
    [pygame.K_KP_DIVIDE]: '',
    [pygame.K_KP_MULTIPLY]: '',
    [pygame.K_KP_MINUS]: '',
    [pygame.K_KP_PLUS]: '',
    [pygame.K_KP_ENTER]: '',
    [pygame.K_KP_EQUALS]: '',
    [pygame.K_UP]: '',
    [pygame.K_DOWN]: '',
    [pygame.K_RIGHT]: '',
    [pygame.K_LEFT]: '',
    [pygame.K_INSERT]: '',
    [pygame.K_HOME]: '',
    [pygame.K_END]: '',
    [pygame.K_PAGEUP]: '',
    [pygame.K_PAGEDOWN]: '',
    [pygame.K_F1]: '',
    [pygame.K_F2]: '',
    [pygame.K_F3]: '',
    [pygame.K_F4]: '',
    [pygame.K_F5]: '',
    [pygame.K_F6]: '',
    [pygame.K_F7]: '',
    [pygame.K_F8]: '',
    [pygame.K_F9]: '',
    [pygame.K_F10]: '',
    [pygame.K_F11]: '',
    [pygame.K_F12]: '',
    [pygame.K_F13]: '',
    [pygame.K_F14]: '',
    [pygame.K_F15]: '',
    [pygame.K_NUMLOCK]: '',
    [pygame.K_CAPSLOCK]: '',
    [pygame.K_SCROLLOCK]: '',
    [pygame.K_RSHIFT]: '',
    [pygame.K_LSHIFT]: '',
    [pygame.K_RCTRL]: '',
    [pygame.K_LCTRL]: '',
    [pygame.K_RALT]: '',
    [pygame.K_LALT]: '',
    [pygame.K_RMETA]: '',
    [pygame.K_LMETA]: '',
    [pygame.K_LSUPER]: '',
    [pygame.K_RSUPER]: '',
    [pygame.K_MODE]: '',
    [pygame.K_HELP]: '',
    [pygame.K_PRINT]: '',
    [pygame.K_SYSREQ]: '',
    [pygame.K_BREAK]: '',
    [pygame.K_MENU]: '',
    [pygame.K_POWER]: '',
    [pygame.K_EURO]: '',
    [pygame.K_AC_BACK]: ''
}