from typing import TypedDict
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
    HOME = 'HOME'
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
    KEYPAD_EQUALS = 'KEYPAD_EQUALS'
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
    F13 = 'F13'
    F14 = 'F14'
    F15 = 'F15'
    INSERT = 'INSERT'
    DELETE = 'DELETE'
    SPACE = 'SPACE'
    END = 'END'
    SCROLL_LOCK = 'SCROLL_LOCK'
    LEFT_META = 'LEFT_META'
    RIGHT_META = 'RIGHT_META'
    LEFT_SUPER = 'LEFT_SUPER'
    RIGHT_SUPER = 'RIGHT_SUPER'
    MODE = 'MODE'
    HELP = 'HELP'
    PRINT = 'PRINT'
    SYSREQ = 'SYSREQ'
    BREAK = 'BREAK'
    MENU = 'MENU'
    POWER = 'POWER'
    EURO = 'EURO'
    ANDROID_BACK = 'ANDROID_BACK'

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

    #MACOS

    CLEAR = 'CLEAR'


requiresShift = [
    NyleEnum.TILDE,
    NyleEnum.AT,
    NyleEnum.HASH,
    NyleEnum.DOLLAR,
    NyleEnum.PERCENT,
    NyleEnum.CARET,
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
    pygame.K_BACKSPACE: NyleEnum.BACKSPACE,
    pygame.K_TAB: NyleEnum.TAB,
    pygame.K_CLEAR: NyleEnum.CLEAR,
    pygame.K_RETURN: NyleEnum.ENTER,
    pygame.K_ESCAPE: NyleEnum.ESCAPE,
    pygame.K_SPACE: NyleEnum.SPACE,
    pygame.K_EXCLAIM: NyleEnum.BANG,
    pygame.K_QUOTEDBL: NyleEnum.DOUBLE_QUOTE,
    pygame.K_HASH: NyleEnum.HASH,
    pygame.K_DOLLAR: NyleEnum.DOLLAR,
    pygame.K_AMPERSAND: NyleEnum.AMPERSAND,
    pygame.K_QUOTE: NyleEnum.SINGLE_QUOTE,
    pygame.K_LEFTPAREN: NyleEnum.LEFT_PARENTHESIS,
    pygame.K_RIGHTPAREN: NyleEnum.RIGHT_PARENTHESIS,
    pygame.K_ASTERISK: NyleEnum.ASTERISK,
    pygame.K_PLUS: NyleEnum.PLUS,
    pygame.K_COMMA: NyleEnum.COMMA,
    pygame.K_MINUS: NyleEnum.MINUS,
    pygame.K_PERIOD: NyleEnum.PERIOD,
    pygame.K_SLASH: NyleEnum.SLASH,
    pygame.K_0: NyleEnum.ZERO,
    pygame.K_1: NyleEnum.ONE,
    pygame.K_2: NyleEnum.TWO,
    pygame.K_3: NyleEnum.THREE,
    pygame.K_4: NyleEnum.FOUR,
    pygame.K_5: NyleEnum.FIVE,
    pygame.K_6: NyleEnum.SIX,
    pygame.K_7: NyleEnum.SEVEN,
    pygame.K_8: NyleEnum.EIGHT,
    pygame.K_9: NyleEnum.NINE,
    pygame.K_COLON: NyleEnum.COLON,
    pygame.K_SEMICOLON: NyleEnum.SEMICOLON,
    pygame.K_LESS: NyleEnum.LESS_THAN,
    pygame.K_EQUALS: NyleEnum.EQUALS,
    pygame.K_GREATER: NyleEnum.GREATER_THAN,
    pygame.K_QUESTION: NyleEnum.QUESTION_MARK,
    pygame.K_AT: NyleEnum.AT,
    pygame.K_LEFTBRACKET: NyleEnum.LEFT_BRACKET,
    pygame.K_BACKSLASH: NyleEnum.BACKSLASH,
    pygame.K_RIGHTBRACKET: NyleEnum.RIGHT_BRACKET,
    pygame.K_CARET: NyleEnum.CARET,
    pygame.K_UNDERSCORE: NyleEnum.UNDERSCORE,
    pygame.K_BACKQUOTE: NyleEnum.TILDE,
    pygame.K_a: NyleEnum.A,
    pygame.K_b: NyleEnum.B,
    pygame.K_c: NyleEnum.C,
    pygame.K_d: NyleEnum.D,
    pygame.K_e: NyleEnum.E,
    pygame.K_f: NyleEnum.F,
    pygame.K_g: NyleEnum.G,
    pygame.K_h: NyleEnum.H,
    pygame.K_i: NyleEnum.I,
    pygame.K_j: NyleEnum.J,
    pygame.K_k: NyleEnum.K,
    pygame.K_l: NyleEnum.L,
    pygame.K_m: NyleEnum.M,
    pygame.K_n: NyleEnum.N,
    pygame.K_o: NyleEnum.O,
    pygame.K_p: NyleEnum.P,
    pygame.K_q: NyleEnum.Q,
    pygame.K_r: NyleEnum.R,
    pygame.K_s: NyleEnum.S,
    pygame.K_t: NyleEnum.T,
    pygame.K_u: NyleEnum.U,
    pygame.K_v: NyleEnum.V,
    pygame.K_w: NyleEnum.W,
    pygame.K_x: NyleEnum.X,
    pygame.K_y: NyleEnum.Y,
    pygame.K_z: NyleEnum.Z,
    pygame.K_DELETE: NyleEnum.DELETE,
    pygame.K_KP0: NyleEnum.KEYPAD_ZERO,
    pygame.K_KP1: NyleEnum.KEYPAD_ONE,
    pygame.K_KP2: NyleEnum.KEYPAD_ZERO,
    pygame.K_KP3: NyleEnum.KEYPAD_THREE,
    pygame.K_KP4: NyleEnum.KEYPAD_FOUR,
    pygame.K_KP5: NyleEnum.KEYPAD_FIVE,
    pygame.K_KP6: NyleEnum.KEYPAD_SIX,
    pygame.K_KP7: NyleEnum.KEYPAD_SEVEN,
    pygame.K_KP8: NyleEnum.KEYPAD_EIGHT,
    pygame.K_KP9: NyleEnum.KEYPAD_NINE,
    pygame.K_KP_PERIOD: NyleEnum.KEYPAD_PERIOD,
    pygame.K_KP_DIVIDE: NyleEnum.KEYPAD_SLASH,
    pygame.K_KP_MULTIPLY: NyleEnum.KEYPAD_ASTERISK,
    pygame.K_KP_MINUS: NyleEnum.KEYPAD_MINUS,
    pygame.K_KP_PLUS: NyleEnum.KEYPAD_PLUS,
    pygame.K_KP_ENTER: NyleEnum.KEYPAD_ENTER,
    pygame.K_KP_EQUALS: NyleEnum.KEYPAD_EQUALS,
    pygame.K_UP: NyleEnum.UP,
    pygame.K_DOWN: NyleEnum.DOWN,
    pygame.K_RIGHT: NyleEnum.RIGHT,
    pygame.K_LEFT: NyleEnum.LEFT,
    pygame.K_INSERT: NyleEnum.INSERT,
    pygame.K_HOME: NyleEnum.HOME,
    pygame.K_END: NyleEnum.END,
    pygame.K_PAGEUP: NyleEnum.PAGE_UP,
    pygame.K_PAGEDOWN: NyleEnum.PAGE_DOWN,
    pygame.K_F1: NyleEnum.F1,
    pygame.K_F2: NyleEnum.F2,
    pygame.K_F3: NyleEnum.F3,
    pygame.K_F4: NyleEnum.F4,
    pygame.K_F5: NyleEnum.F5,
    pygame.K_F6: NyleEnum.F6,
    pygame.K_F7: NyleEnum.F7,
    pygame.K_F8: NyleEnum.F8,
    pygame.K_F9: NyleEnum.F9,
    pygame.K_F10: NyleEnum.F10,
    pygame.K_F11: NyleEnum.F11,
    pygame.K_F12: NyleEnum.F12,
    pygame.K_F13: NyleEnum.F13,
    pygame.K_F14: NyleEnum.F14,
    pygame.K_F15: NyleEnum.F15,
    pygame.K_NUMLOCK: NyleEnum.NUMLOCK,
    pygame.K_CAPSLOCK: NyleEnum.CAPS_LOCK,
    pygame.K_SCROLLOCK: NyleEnum.SCROLL_LOCK,
    pygame.K_RSHIFT: NyleEnum.RIGHT_SHIFT,
    pygame.K_LSHIFT: NyleEnum.LEFT_SHIFT,
    pygame.K_RCTRL: NyleEnum.RIGHT_CONTROL,
    pygame.K_LCTRL: NyleEnum.LEFT_CONTROL,
    pygame.K_RALT: NyleEnum.LEFT_ALT,
    pygame.K_LALT: NyleEnum.RIGHT_ALT,
    pygame.K_RMETA: NyleEnum.RIGHT_META,
    pygame.K_LMETA: NyleEnum.LEFT_META,
    pygame.K_LSUPER: NyleEnum.LEFT_SUPER,
    pygame.K_RSUPER: NyleEnum.RIGHT_SUPER,
    pygame.K_MODE: NyleEnum.MODE,
    pygame.K_HELP: NyleEnum.HELP,
    pygame.K_PRINT: NyleEnum.PRINT,
    pygame.K_SYSREQ: NyleEnum.SYSREQ,
    pygame.K_BREAK: NyleEnum.BREAK,
    pygame.K_MENU: NyleEnum.MENU,
    pygame.K_POWER: NyleEnum.POWER,
    pygame.K_EURO: NyleEnum.EURO,
    pygame.K_AC_BACK: NyleEnum.ANDROID_BACK
}

class NyleModifiers(Enum):
    NONE = 'None'
    LEFT_SHIFT = 'LEFT_SHIFT'
    RIGHT_SHIFT = 'RIGHT_SHIFT'
    SHIFT = 'SHIFT'
    LEFT_CONTROL = 'LEFT_CONTROL'
    RIGHT_CONTROL = 'RIGHT_CONTROL'
    CONTROL = 'CONTROL'
    LEFT_ALT = 'LEFT_ALT'
    RIGHT_ALT = 'RIGHT_ALT'
    ALT = 'ALT'
    LEFT_META = 'LEFT_META'
    RIGHT_META = 'RIGHT_META'
    META = 'META'
    CAPS_LOCK = 'CAPS_LOCK'
    NUM_LOCK = 'NUM_LOCK'
    MODE = 'MODE'

modifierConvert = {
    pygame.KMOD_NONE: NyleModifiers.NONE,
    pygame.KMOD_LSHIFT: NyleModifiers.LEFT_SHIFT,
    pygame.KMOD_RSHIFT: NyleModifiers.RIGHT_SHIFT,
    pygame.KMOD_SHIFT: NyleModifiers.SHIFT,
    pygame.KMOD_LCTRL: NyleModifiers.LEFT_CONTROL,
    pygame.KMOD_RCTRL: NyleModifiers.RIGHT_CONTROL,
    pygame.KMOD_CTRL: NyleModifiers.CONTROL,
    pygame.KMOD_LALT: NyleModifiers.LEFT_ALT,
    pygame.KMOD_RALT: NyleModifiers.RIGHT_ALT,
    pygame.KMOD_ALT: NyleModifiers.ALT,
    pygame.KMOD_LMETA: NyleModifiers.LEFT_META,
    pygame.KMOD_RMETA: NyleModifiers.RIGHT_META,
    pygame.KMOD_META: NyleModifiers.META,
    pygame.KMOD_CAPS: NyleModifiers.CAPS_LOCK,
    pygame.KMOD_NUM: NyleModifiers.NUM_LOCK,
    pygame.KMOD_MODE: NyleModifiers.MODE,
}

class rawKeyBuffer(TypedDict):
    keys: list[int]
    modifiers: list[int]

class keyBuffer(TypedDict):
    keys: list[NyleEnum]
    modifiers: list[NyleModifiers]

def purifyRawKeyBuffer(keyBuffer: rawKeyBuffer) -> keyBuffer:
    pureKeys: list[NyleEnum] = []
    pureMods: list[NyleModifiers] = []

    for key in keyBuffer["keys"]:

        v = keyConvert.get(key)

        if v: pureKeys.append(v)
        else: raise Exception(f'key {key} has no proper mapping to NyleEnum')
    for mod in keyBuffer["modifiers"]:

        v = modifierConvert.get(mod)

        if v: pureMods.append(v)
        else: raise Exception(f'modifier {mod} has no proper mapping to NyleModifiers')

    return {
        "modifiers": pureMods,
        "keys": pureKeys
    }