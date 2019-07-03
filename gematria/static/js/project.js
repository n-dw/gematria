/* Project specific Javascript goes here. */

import VueTouchKeyboard from "vue-touch-keyboard";

new Vue({
  el: '#app',
  components: { VueTouchKeyboard },

  data: {
   visible: false,
      layout: "normal",
      input: null,
      options: {
        useKbEvents: false,
        preventClickEvent: false
      }
  },

  methods: {
    accept(text) {
          alert("Input text: " + text);
          this.hide();
        },

        show(e) {
          this.input = e.target;
          this.layout = e.target.dataset.layout;

          if (!this.visible)
            this.visible = true
        },

        hide() {
          this.visible = false;
        }
  }
});

const Layouts = {
    "default": {

        _meta: {
            "tab": { key: "\t", text: "Tab", width: 60, classes: "control"},
            "shiftl": { keySet: "shifted", text: "Shift", width: 100, classes: "control"},
            "shiftr": { keySet: "shifted", text: "Shift", width: 100, classes: "control"},
            "caps": { keySet: "capsed", text: "Caps lock", width: 80, classes: "control"},
            "space": { key: " ", text: "Space", width: 180},
            "enter": { key: "\r\n", text: "Enter", width: 80, classes: "control"},
            "backspace": { func: "backspace", classes: "control backspace", width: 65},
            "accept": { func: "accept", text: "Close", classes: "control featured"},
            "next": { func: "next", text: "Next", classes: "control featured"}
        },



        default:  [
		'; 1 2 3 4 5 6 7 8 9 0 - = {backspace}',
		"{tab} / ' \u05e7 \u05e8 \u05d0 \u05d8 \u05d5 \u05df \u05dd \u05e4 [ ] \\",
		"\u05e9 \u05d3 \u05d2 \u05db \u05e2 \u05d9 \u05d7 \u05dc \u05da \u05e3 , {enter}",
		"{shift} \u05d6 \u05e1 \u05d1 \u05d4 \u05e0 \u05de \u05e6 \u05ea \u05e5 . {shift}",
		"{accept} {alt} {space} {alt} {cancel}"
	],
        shifted: [
            "~ ! @ # $ % ^ & * ( ) _ + {backspace}",
            "{tab} ח ח ל ך ם U I O P { } |",
            "{caps} A S D F G H J K L : \" {enter}",
            "{shiftl} Z X C V B N M < > ? {shiftr}",
            "{next} {space} {accept}"
        ],

        capsed: [
            "` 1 2 3 4 5 6 7 8 9 0 - = {backspace}",
            "{tab} Q W E R T Y U I O P [ ] \\",
            "{caps} A S D F G H J K L ; ' {enter}",
            "{shiftl} Z X C V B N M , . / {shiftr}",
            "{next} {space} {accept}"
        ]
    },
    "email": {

        _meta: {
            "tab": { key: "\t", text: "Tab", width: 60},
            "shiftl": { keySet: "shifted", text: "Shift", width: 100},
            "shiftr": { keySet: "shifted", text: "Shift", width: 100},
            "caps": { keySet: "capsed", text: "Caps lock", width: 80},
            "space": { key: " ", text: "Space", width: 180},
            "enter": { key: "\r\n", text: "Enter", width: 80},
            "backspace": { func: "backspace", classes: "backspace", width: 65},
            "next": { func: "next", text: "Next", classes: "featured"},
            "accept": { func: "accept", text: "Close", classes: "close featured"},
            "@": { key: "@", text: "@", classes: "email featured", width: 15},
            "gmail": { key: "@gmail.com", text: "@gmail.com", classes: "email featured"},
            "hotmail": { key: "@hotmail.com", text: "@hotmail.com", classes: "email featured"},
            "live": { key: "@live.com", text: "@live.com", classes: "email featured"},
            "yahoo_us": { key: "@yahoo.com", text: "@yahoo.com", classes: "email featured"},
            "yahoo_br": { key: "@yahoo.com", text: "@yahoo.com.br", classes: "email featured"},
            "mac": { key: "@mac.com", text: "@mac.com", classes: "email featured"},
            "me": { key: "@me.com", text: "@me.com", classes: "email featured"},
        },

        default: [
            "{@} {gmail} {hotmail} {live} {yahoo_us} {yahoo_br} {mac_us} {me_us}",
            "` 1 2 3 4 5 6 7 8 9 0 - = {backspace}",
            "{tab} q w e r t y u i o p [ ] \\",
            "{caps} a s d f g h j k l ; ' {enter}",
            "{shiftl} z x c v b n m , . / {shiftr}",
            "{next} {space} {accept}"
        ],
        shifted: [
            "{@} {gmail} {hotmail} {live} {yahoo_us} {yahoo_br} {mac_us} {me_us}",
            "~ ! @ # $ % ^ & * ( ) _ + {backspace}",
            "{tab} Q W E R T Y U I O P { } |",
            "{caps} A S D F G H J K L : \" {enter}",
            "{shiftl} Z X C V B N M < > ? {shiftr}",
            "{next} {space} {accept}"
        ],

        capsed: [
            "{@} {gmail} {hotmail} {live} {yahoo_us} {yahoo_br} {mac_us} {me_us}",
            "` 1 2 3 4 5 6 7 8 9 0 - = {backspace}",
            "{tab} Q W E R T Y U I O P [ ] \\",
            "{caps} A S D F G H J K L ; ' {enter}",
            "{shiftl} Z X C V B N M , . / {shiftr}",
            "{next} {space} {accept}"
        ]
    },
}


'default' : [
		'; 1 2 3 4 5 6 7 8 9 0 - = {bksp}',
		"{tab} / ' \u05e7 \u05e8 \u05d0 \u05d8 \u05d5 \u05df \u05dd \u05e4 [ ] \\",
		"\u05e9 \u05d3 \u05d2 \u05db \u05e2 \u05d9 \u05d7 \u05dc \u05da \u05e3 , {enter}",
		"{shift} \u05d6 \u05e1 \u05d1 \u05d4 \u05e0 \u05de \u05e6 \u05ea \u05e5 . {shift}",
		"{accept} {alt} {space} {alt} {cancel}"
	],
	'alt-shift' : [
		"~ ! @ # $ % ^ & * ( ) _ + {bksp}",
		"{tab} Q W E R T Y U I O P { } |",
		'A S D F G H J K L : " {enter}',
		"{shift} Z X C V B N M < > ? {shift}",
		"{accept} {alt} {space} {alt} {cancel}"
	],
	'alt' : [
		'` 1 2 3 4 5 6 7 8 9 0 - = {bksp}',
		"{tab} q w e r t y u i o p [ ] \\",
		"a s d f g h j k l ; ' {enter}",
		"{shift} z x c v b n m , . / {shift}",
		"{accept} {alt} {space} {alt} {cancel}"
	]
};
