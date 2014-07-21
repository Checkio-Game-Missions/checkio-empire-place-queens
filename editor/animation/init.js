//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210'],
    function (ext, $, TableComponent) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide["in"] = data[0];
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            //YOUR FUNCTION NAME
            var fname = 'place_queens';

            if (data.ext && data.ext.show) {
                var checkioInputStr = fname + "(" + data.ext.show + ")";
            }
            else {
                checkioInputStr = fname + '({"b1", "c4", "d6", "e8"})';
            }

            var failError = function (dError) {
                $content.find('.call').html('Fail: ' + checkioInputStr);
                $content.find('.output').html(dError.replace(/\n/g, ","));

                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.answer').remove();
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
            };

            if (data.error) {
                failError(data.error);
                return false;
            }

            if (data.ext && data.ext.inspector_fail) {
                failError(data.ext.inspector_result_addon);
                return false;
            }

            var checkioInput = data.in;
            var rightResult = data.ext["answer"];
            var userResult = data.out[0];
            var userResultShow = data.out[1];
            var result = data.ext["result"];
            var resultAddon = data.ext["result_addon"];
            var resultCode = resultAddon[0];
            var resultText = resultAddon[1];
            var threats = resultAddon[2];

            //if you need additional info from tests (if exists)
            var explanation = data.ext["explanation"];

            $content.find('.output').html('&nbsp;Your result:&nbsp;' + userResultShow);

            if (!result) {
                $content.find('.call').html('Fail: ' + checkioInputStr);
                $content.find('.answer').html(resultText);
                $content.find('.answer').addClass('error');
                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
            }
            else {
                $content.find('.call').html('Pass: ' + checkioInputStr);
                $content.find('.answer').remove();
            }

            var canvas = new ChessCanvas($content.find(".explanation")[0]);
            canvas.prepare(checkioInput);


            this_e.setAnimationHeight($content.height() + 60);

        });

        //This is for Tryit (but not necessary)
//        var $tryit;
//        ext.set_console_process_ret(function (this_e, ret) {
//            $tryit.find(".checkio-result").html("Result<br>" + ret);
//        });
//
//        ext.set_generate_animation_panel(function (this_e) {
//            $tryit = $(this_e.setHtmlTryIt(ext.get_template('tryit'))).find('.tryit-content');
//            $tryit.find('.bn-check').click(function (e) {
//                e.preventDefault();
//                this_e.sendToConsoleCheckiO("something");
//            });
//        });

        function ChessCanvas(dom) {

            var colorOrange4 = "#F0801A";
            var colorOrange3 = "#FA8F00";
            var colorOrange2 = "#FAA600";
            var colorOrange1 = "#FABA00";

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue2 = "#65A1CF";
            var colorBlue1 = "#8FC7ED";

            var colorGrey4 = "#737370";
            var colorGrey3 = "#9D9E9E";
            var colorGrey2 = "#C5C6C6";
            var colorGrey1 = "#EBEDED";

            var colorWhite = "#FFFFFF";

            var padding = 10;
            var cell = 40;

            var figures;

            var size = padding * 2 + cell * 9;
            var paper = Raphael(dom, size, size);

            var attrBoard = {"stroke": colorBlue4, "stroke-width": 3};
            var attrBlack = {"fill": colorBlue2, "stroke-width": 0};
            var attrWhite = {"fill": colorGrey1, "stroke-width": 0};
            var attrQueen = {"stroke": colorBlue4, "font-family": "Roboto", "font-size": cell * 0.8};
            var attrText = {"stroke": colorBlue4, "font-family": "Roboto", "font-size": cell * 0.8, "font-weight": "bold"};

            var rows = "12345678";
            var cols = "abcdefgh";


            this.place_queen = function(coor, full) {
                var r = rows.indexOf(coor[1]);
                var c = cols.indexOf(coor[0]);
                paper.text(padding + cell * 1.5 + c * cell, size - padding - cell * 1.5 - cell * r,
                    full ? "♛" : "♕").attr(attrQueen);
            };


            this.prepare = function(placed) {
                for (var i = 0; i < 8; i++) {
                    paper.text(padding + cell / 2, size - padding - cell * i - cell * 1.5, rows[i]).attr(attrText);
                    paper.text(padding + cell * 1.5 + cell * i, size - padding - cell / 2, cols[i]).attr(attrText);
                    for (var j = 0; j < 8; j++) {
                        paper.rect(padding + cell + cell * i, padding + cell * j, cell, cell).attr(
                            (i + j) % 2 === 1 ? attrBlack : attrWhite);
                    }
                }
                paper.rect(padding + cell, padding, cell * 8, cell * 8).attr(attrBoard);
                for (i = 0; i < placed.length; i++) {
                    this.place_queen(placed[i], true);
                }
            }

        }

    }
);
