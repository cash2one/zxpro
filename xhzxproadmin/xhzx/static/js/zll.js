startorstop = function (c) {

    cur = c.parent().parent().parent().parent().parent()
//        console.log(c.attr('title'))
    if (c.attr('title') == '启用') {
        cur.attr('zll_status', "1")
        c.parent().prev().children('span').text('启用')
        c.parent().prev().children('span').removeClass('label-danger')
        c.parent().prev().children('span').addClass('label-primary')
    }
    if (c.attr('title') == '停用') {
        cur.attr('zll_status', "0")
        c.parent().prev().children('span').text('停用')
        c.parent().prev().children('span').removeClass('label-primary')
        c.parent().prev().children('span').addClass('label-danger')
    }
//        console.log(cur.attr('zll_status'))
    swal("设置为" + c.attr('title'), "重启后才能生效.", "success");
}

var debug = true
var svb = true
address = function (mos, alname, adr, netmask) {

    if (mos == '从')
        style = "label-info"
    else if (mos == '主')
        style = "label-primary"
    else {
        mos = '新'
        style = "label-warning"
    }
    if (alname) {
        return ' <tr zll_name="' + alname + '" class=" zll_json" > <td><span class="label ' + style + ' pull-right">' + mos + '</span>IP地址</td> <td><input type="text" class="form-control adr"   zll-type="ipv4" maxlength="15"    placeholder="IP地址" value="' + adr + '"></td>   <td>子网掩码</td> <td><input type="text" class="form-control netmask"     zll-type="ipv4" maxlength="15"    placeholder="255.255.255.255" value="' + netmask + '"></td>   <td> <div class="btn-group">  <button class="btn btn-warning   address-clean" title="清空地址" type="button"><i    class="fa fa-ban"></i>清空地址</button>    <button class="btn btn-danger    something-delete "  zll-name="从地址" type="button"><i    class="fa fa-times"></i>删除地址</button>  </div>  </td>    </tr>'
    }
    else {

        return ' <tr zll_name="' + alname + '" class="new zll_json"> <td><span class="label ' + style + ' pull-right">' + mos + '</span>IP地址</td> <td><input type="text" class="form-control adr"   zll-type="ipv4" maxlength="15"    placeholder="IP地址" ></td>   <td>子网掩码</td> <td><input type="text" class="form-control netmask"     zll-type="ipv4" maxlength="15"    placeholder="255.255.255.255"></td>   <td> <div class="btn-group">  <button class="btn btn-warning address-clean" title="清空地址" type="button"><i    class="fa fa-ban"></i>清空地址</button>    <button class="btn btn-danger   something-delete "  zll-name="从地址" type="button"><i    class="fa fa-times"></i>删除地址</button>  </div>  </td>    </tr>'


    }
}


router = function (network, netmask, gateway) {
    if (network) {

        return '<tr class="zll_json"><td>目标网络IP </td><td><input type="text" class="form-control network"  zll-type="ipv4" maxlength="15" placeholder="IP地址" value="' + network + '"> </td><td>子网掩码</td><td><input type="text" class="form-control netmask"  zll-type="ipv4" maxlength="15" placeholder="255.0.0.0" value="' + netmask + '"></td> <td>网关地址</td> <td><input type="text" class="form-control gateway"  zll-type="ipv4" maxlength="15" placeholder="IP地址" value="' + gateway + '" ></td> <td> <div class="btn-group">   <button class="btn btn-danger something-delete" zll-name="路由" type="button"><i class="fa fa-times"></i> 删除路由  </button>   </div>   </td> </tr>'


    }
    else {
        mos = "新"
        style = "label-warning"
        return '<tr class="new zll_json"><td><span class="label ' + style + ' pull-right">' + mos + '</span>目标网络IP </td><td><input type="text" class="form-control network"  zll-type="ipv4" maxlength="15" placeholder="IP地址" > </td><td>子网掩码</td><td><input type="text" class="form-control netmask"  zll-type="ipv4" maxlength="15" placeholder="255.0.0.0"></td> <td>网关地址</td> <td><input type="text" class="form-control gateway"  zll-type="ipv4" maxlength="15" placeholder="IP地址" ></td> <td> <div class="btn-group">   <button class="btn btn-danger something-delete" zll-name="路由" type="button"><i class="fa fa-times"></i> 删除路由  </button>   </div>   </td> </tr>'

    }

}


nints = function (netname, v) {

//        console.log(config)

    return '<div zll_int="em' + v + '" class="panel panel-default em' + v + '"><div class="panel-heading">' + netname + ' <button class="btn btn-primary   address-add" type="button"><i  class="fa fa-plus"></i> 增加地址       </button></div><div class="panel-body"><table class="table table-striped  table-condensed tb_adr"> <tbody></tbody></table> </div> </div>'

}


gapline = function (name, myadr, myport, hisadr, hisport) {
    if (name) {

        mos = ""

        return '<tr class="zll_json"><td><span class="label ' + style + ' pull-right">' + mos + '</span> </td><td><input type="text" placeholder="名称"  maxlength="8" class="form-control rule_name" value="' + name + '"  ></td><td><input type="text" class="form-control rule_myadr"   zll-type="ipv4" maxlength="15"    placeholder="IP地址" value="' + myadr + '"></td><td><input type="text"  placeholder="端口号" zll-type="port" value="' + myport + '" maxlength="5"  class="form-control rule_myport"></td><td><input type="text" class="form-control rule_hisadr"     zll-type="ipv4" maxlength="15"  value="' + hisadr + '"  placeholder="IP地址" ></td>  <td><input type="text"   placeholder="端口号" value="' + hisport + '" zll-type="port" maxlength="5"  class="form-control rule_hisport"></td> <td> <div class="btn-group"><button class="btn btn-danger    something-delete " zll-name="策略"  type="button"><i class="fa fa-times"></i>删除策略</button></div></td></tr>'

    }
    else {
        mos = '新'
        style = "label-warning"
        return '<tr class="new zll_json"><td><span class="label ' + style + ' pull-right">' + mos + '</span> </td><td><input type="text" placeholder="名称"  maxlength="8" class="form-control rule_name"></td><td><input type="text" class="form-control rule_myadr"   zll-type="ipv4" maxlength="15"    placeholder="IP地址" ></td><td><input type="text" placeholder="端口号"  zll-type="port" maxlength="5"  class="form-control rule_myport"></td><td><input type="text" class="form-control rule_hisadr"     zll-type="ipv4" maxlength="15"    placeholder="IP地址" ></td>  <td><input type="text" placeholder="端口号" zll-type="port" maxlength="5"  class="form-control rule_hisport"></td> <td> <div class="btn-group"><button class="btn btn-warning   something-delete " zll-name="策略"  type="button"><i class="fa fa-times"></i>删除策略</button></div></td></tr>'


    }

}
function checkINPUT(valid, value) {

    if (valid == 'port') {
        if (value >= 1 && value <= 65535)
            return true
        else
            return false
    }

    if (valid == 'ipv4') {
        var exp = /^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
        var reg = value.match(exp);
        if (reg == null)
            return false;
        else
            return true;
    }
}

function getstatus() {
    var reqpath = "/get_status/"
    $.getJSON(reqpath, {}, function (data) {
//            console.log(data.ia)
        if (data) {
            var mach = ["ia", "oa"];
            $.each(mach, function (i, val) {
                $("#" + val + "_uptime").text(eval('data.' + val + '.uptime'))
                $("#" + val + " .use_cpu").text(eval('data.' + val + '.cpu') + '%')
                $("#" + val + " .use_cpu_bar").css("width", eval('data.' + val + '.cpu') + '%')
                $("#" + val + " .use_mem").text(eval('data.' + val + '.memory') + '%')
                $("#" + val + " .use_mem_bar").css("width", eval('data.' + val + '.memory') + '%')
                $("#" + val + " .use_disk").text(eval('data.' + val + '.disk') + '%')
                $("#" + val + " .use_disk_bar").css("width", eval('data.' + val + '.disk') + '%')
            });
        }
    });
}

getlog = function () {
    var reqpath = "/get_log/"
    $.getJSON(reqpath, {}, function (data) {

        htmls = ''
        if (data.ia) {
            $.each(data.ia, function (i, val) {
                htmls += '<tr><td class="issue-info"><code>' + val + '</code></td></tr>'
            })

            $("#ialog").html(htmls)
            $("#iacount").html(data.iacount)
        }

        if (data.oa) {
            $.each(data.oa, function (i, val) {
                htmls += '<tr><td class="issue-info"><code>' + val + '</code></td></tr>'
            })

            $("#oalog").html(htmls)
            $("#oacount").text(data.oacount)
        }


    })


}


getconfig = function () {

    var reqpath = "/get_config/"
    $.getJSON(reqpath, {}, function (data) {

//            console.log(data)
        config = data
        if (data) {
            $(".ia .defaultgateway").val(data.ia.defaultgateway)
            $(".oa .defaultgateway").val(data.oa.defaultgateway)

            var mach = ["ia", "oa"];
            $.each(mach, function (s, m) {
                var ints = eval('data.' + m + '.interface');

//                    console.log(ints)
                $.each(ints, function (i, val) {
                    if (val.name) {
                        var em = val.name.split('_');
                        var mos = "主";
                        if (em.length > 1)
                            mos = "从";
                        var tbody = $("." + m + " ." + em[0] + " .tb_adr tbody")[0]


                        var htm = address(mos, val.name, val.adr, val.netmask);
//                            console.log($(htm))
                        $(htm).appendTo(tbody)

                    }

                })
                var routers = eval('data.' + m + '.router');
                $.each(routers, function (i, val) {
                    if (val.network) {
                        var htm = router(val.network, val.netmask, val.gateway);
//                            console.log($(htm).html())
                        $(htm).appendTo($("." + m + " .router")[0])

                    }

                })
            });

            var rs = ["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA", "IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"];


            $.each(rs, function (i, rule) {

//                    console.log(rs)
//                    console.log(rule)
                var rules = eval('data.' + rule);
//                    console.log(data.OUT_TCP)
                var rulestatus = $($("." + rule + " .status")[0])
                if (eval('data.' + rule).on == "1") {

                    rulestatus.text('启用')
                    rulestatus.addClass('label-primary')
                }

                else {
                    rulestatus.text('停用')
                    rulestatus.addClass('label-danger')
                }


                $.each(rules['rules'], function (i, val) {
//                        console.log($("." + rule + " .tcpinside tbody")[0])
                    if (val.name) {
                        var htm = gapline(val.name, val.myadr, val.myport, val.hisadr, val.hisport);
//                            console.log($(htm).html())

                        $(htm).appendTo($("." + rule + " .tcpinside tbody")[0])

                    }


                })
            })

        }
    });

}

CallBack = function () {


}
gap_reload = function () {

    swal({
        title: "重启!?",
        text: "配置确定保存了吗?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "确认重启",
        cancelButtonText: "取消",
        closeOnConfirm: false
    }, function () {

        $.ajax({
            url: "/gap_reload/",
            data: {
                cmd: "reload",
                password: "zll"
            },
            type: "POST",
            dataType: 'json',
            success: CallBack,
            error: function (er) {
                setInterval(location.reload(), 60000)
            }
        });

    });


}
gap_stop = function () {
    swal({
        title: "关机!?",
        text: "配置确定保存了吗?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        confirmButtonText: "确认关机",
        cancelButtonText: "取消",
        closeOnConfirm: false
    }, function () {

        $.ajax({
            url: "/gap_stop/",
            data: {
                cmd: "stop",
                password: "zll"
            },
            type: "POST",
            dataType: 'json',
            success: CallBack,
            error: function (er) {
                alert("网闸正在关机...")
                location.href = 'http://page:blank'
            }
        });
    });
}


getconfig_now = function () {


}

var config = {};
var newconfig = {};

createconfig_new = function () {

    $.each(['ia', 'oa'], function (i, mash) {
        jSing.create(newconfig, mash, {
            "interface": [],
            "router": [],
            "defaultgateway": ""
        });

        var defaultgateway = $("." + mash + " .defaultgateway").val().trim()
        if (defaultgateway)
            jSing.set(newconfig, mash, "defaultgateway", defaultgateway)


//            console.log($(".ia .tb_adr tbody .zll_json").html())


        var ints = $("." + mash + " .tb_adr tbody .zll_json")
        var ints_json = []
        $.each(ints, function (i, val) {

            var int_tr = $(val)
            var name = $.trim(int_tr.attr('zll_name'))
            var adr = $.trim(int_tr.find('.adr').val())
            var netmask = $.trim(int_tr.find('.netmask').val())

            //alert(name)
            if (name && adr && netmask) {

                var int_adr_info = {
                    "name": name,
                    "adr": adr,
                    "netmask": netmask
                };
//                    console.log(int_adr_info)
                ints_json.push(int_adr_info)
            }
        })

        //console.log(ints_json)

        var routers = $("." + mash + " .router .zll_json")

        var routers_json = []
        $.each(routers, function (i, val) {
            var int_tr = $(val)
            var network = $.trim(int_tr.find('.network').val())
            var netmask = $.trim(int_tr.find('.netmask').val())
            var gateway = $.trim(int_tr.find('.gateway').val())


            if (network && netmask && gateway) {

                var router_info = {
                    "network": network,
                    "netmask": netmask,
                    "gateway": gateway
                };
//                    console.log(router_info)
                routers_json.push(router_info)
            }
        })


//            console.log(routers_json)
        jSing.set(newconfig, mash, "interface", ints_json)
        jSing.set(newconfig, mash, "router", routers_json)

    });

    $.each(["OUT_TCP", "OUT_UDP", "OUT_FTP", "OUT_ORA", "IN_TCP", "IN_UDP", "IN_FTP", "IN_ORA"], function (i, rule) {


        if ($($("." + rule + " .status")[0]).text() == "启用")
            var on = '1'
        else
            var on = '0'

        var rules_tr = $("." + rule + " .zll_json")

        var rule_json = []


        $.each(rules_tr, function (i, val) {
            var rule_tr = $(val)

            var name = $.trim(rule_tr.find('.rule_name').val())
            var myadr = $.trim(rule_tr.find('.rule_myadr').val())
            var myport = $.trim(rule_tr.find('.rule_myport').val())
            var hisadr = $.trim(rule_tr.find('.rule_hisadr').val())
            var hisport = $.trim(rule_tr.find('.rule_hisport').val())

//                console.log(name)

            if (name && myadr && myport && hisadr && hisport) {

                var rule_info = {
                    "name": name,
                    "myadr": myadr,
                    "myport": myport,
                    "hisadr": hisadr,
                    "hisport": hisport
                };
//                    console.log(rule_info)
                rule_json.push(rule_info)
            }
        })

        jSing.create(newconfig, rule, {
            "on": on,
            "rules": rule_json
        });

    })

    var oldpass = $("#oldpass").val()
    var newpass1 = $("#newpass1").val()
    var newpass2 = $("#newpass2").val()


    if (oldpass && newpass1 && newpass2)
        if (newpass1 == newpass2)
            jSing.create(newconfig, "changepass", {
                "oldpass": oldpass,
                "newpass1": newpass1,
                "newpass2": newpass2
            });
    //console.log(JSON.stringify(newconfig))
    //console.log(JSON.stringify(config))
    //console.log(JSON.stringify(newconfig) == JSON.stringify(config))

}


styleset = function () {

    $("body").addClass('fixed-sidebar');
    $('.sidebar-collapse').slimScroll({
        height: '100%',
        railOpacity: 0.9
    });
    if (localStorageSupport) {
        localStorage.setItem("fixedsidebar", 'on');
    }
    $('#boxedlayout').prop('checked', false);
    $("body").removeClass('boxed-layout');
    $(".footer").addClass('fixed');

    if (localStorageSupport) {
        localStorage.setItem("boxedlayout", 'off');
    }

    if (localStorageSupport) {
        localStorage.setItem("fixedfooter", 'on');
    }

}

need_restart_set = function () {

    $.getJSON('/need_restart/', {}, function (data) {
        if (data.succ) {

            $("#nr_tip").text('1')
            $("#nr_info").text('配置已经改变,重启之后才能生效!')


            swal({
                title: "现在就重启?",
                text: "配置已经改变,重启之后才能生效!",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确认重启",
                cancelButtonText: "取消",
                closeOnConfirm: false
            }, function () {
                $.ajax({
                    url: "/gap_reload/",
                    data: {
                        cmd: "reload",
                        password: "zll"
                    },
                    type: "POST",
                    dataType: 'json',
                    success: CallBack,
                    error: function (er) {
                        setInterval(location.reload(), 60000)
                    }
                });

            });


            //swal("注意!", "配置已经改变,重启之后才能生效!", "info");
            //console.log(arguments.callee)
        }
    });


}

$(document).ready(function () {

    styleset()
    need_restart_set()
    getstatus()
    getconfig()
    getlog()

    $(".startorstop").on('click', function () {
        startorstop($(this))
    })
    //var Status = setInterval(getstatus, 60000);

    $(".zll_fresh li").on('click', function () {
//            console.log($(this).attr('zll_act'))
        if ($(this).attr('zll_act') == '0') {
            //clearInterval(Status);
            $("#refresh_info").html('不刷新')
        }
        else if ($(this).attr('zll_act') == '60') {
            //clearInterval(Status);
            //Status = setInterval(getstatus, 60000);
            $("#refresh_info").html('每1分钟刷新')
        }
        else if ($(this).attr('zll_act') == '600') {
            //clearInterval(Status);
            //Status = setInterval(getstatus, 600000);
            $("#refresh_info").html('每10分钟刷新')
        }
        else
            ;
    })


//        $(document).on("click", ".address-delete",function () {
//            var $tmp = $(this)
//
//                swal({
//                    title: "确定吗?",
//                    text: "确定要删除这个地址吗?",
//                    type: "warning",
//                    showCancelButton: true,
//                    confirmButtonColor: "#DD6B55",
//                    confirmButtonText: "删除!",
//                    closeOnConfirm: false
//                }, function (isConfirm) {
//                    if (isConfirm) {
////                        $tmp.parent().parent().remove()
//                        swal("成功!", "从地址已经删除!.", "成功");
//                    } else {
//                        swal("取消删除!", "取消删除从地址已经删除!.", "取消删除成功");
//                    }
//
//                });
//        });
    var ints = ["接口1", "接口2", "接口3", "接口4"];


    for (var i = 0; i < ints.length; i++) {
        $(".address").append(nints(ints[i], i))
    }


    $(document).on("click", ".save", function () {
        createconfig_new()

        console.log(newconfig)
        var $tmp = $(this)
        swal({
            title: "确定吗?",
            text: "确定要保存吗?点击确认保存后,请耐心等待...",
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "确认保存",
            cancelButtonText: "取消",
            closeOnConfirm: false
        }, function () {
            if (svb) {
                svb = false
                $.post("/save/",
                    {
                        cmd: "save",
                        config: JSON.stringify(newconfig)
                    },
                    function (data, status) {
                        svb = true
                        if (data.succ) {
                            swal("成功!", "配置已经保存,重启后生效.", "success");
                        }
                        else
                            swal("不成功!", "配置保存出错", "warning");
                    });
            }
            else{
                alert("配置正在保存中,请勿连续点击..")
            }
        });
    });


    $(document).on("click", ".something-delete", function () {
        var $tmp = $(this)
        if ($tmp.parent().parent().parent().hasClass('new'))
            $tmp.parent().parent().parent().remove();
        else {
//                console.log($tmp.parent().parent().parent())
            swal({
                title: "确定吗?",
                text: "确定要删除这条" + $tmp.attr('zll-name') + "吗?",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确认删除",
                cancelButtonText: "取消",
                closeOnConfirm: false
            }, function () {
                if (debug)
//                        console.log($tmp.parent().parent())
                    $tmp.parent().parent().parent().remove()
                swal("成功!", $tmp.attr("zll-name") + "已经删除.重启后生效", "success");
            });
        }
    });


    $(document).on("click", ".address-add", function () {
        lasttr = $(this).parent().parent().find('tbody > tr:last-child')

        intname = $(this).parent().parent().attr('zll_int')

        if (lasttr.hasClass(' zll_json')) {
            name = lasttr.attr('zll_name')

            if (name == intname) {
                $(this).parent().parent().find('tbody').append(address("从", name + "_alias0", "", ""))
            } else {
                var em = name.split('alias');
                newname = intname + "_alias" + String(parseInt(em[em.length - 1]) + 1)
                $(this).parent().parent().find('tbody').append(address("从", newname, "", ""))
            }
        }
        else
            $(this).parent().parent().find('tbody').append(address("主", intname, "", ""))
    });


    $(document).on("blur", "[zll-type]", function () {
        $(this).removeClass('animated tada')
//            console.log($(this).val())
        if ($(this).val()) {
            flag = checkINPUT($(this).attr('zll-type'), $(this).val())
//                console.log(flag)
            if (flag) {
            } else {
                $(this).focus()
                swal({
                    title: $(this).attr('placeholder') + "格式错误",
                    text: "请修改" + $(this).attr('placeholder') + "格式"
                });
                $(this).addClass('animated tada')
            }
        }
//            console.log(checkINPUT($(this).val()))
    });
    $(document).on("blur", "#newpass2,#oldpass,#newpass1", function () {
        oldpass = $("#oldpass").val()
        if (oldpass) {
            newpass1 = $("#newpass1").val()
            newpass2 = $("#newpass2").val()
            if (newpass1 && newpass2) {

                if (newpass1 == newpass2) {
                } else {
                    swal({
                        title: "新密码两次输入必须相同",
                        text: "请修改两次新密码"
                    });
                    $("#newpass1").val('')
                    $("#newpass2").val('')
                }

            }
        }
    });


    $(document).on("click", ".router-add", function () {
        $(this).parent().parent().find('tbody').append(router())
    });

    $(document).on("click", ".gapline-add", function () {
        $(this).parent().parent().find('tbody').append(gapline())
    });

    $(document).on("click", ".address-clean", function () {

        $(this).parent().parent().parent().find('input').val('')
        var $tmp = $(this)

        if ($tmp.parent().parent().parent().hasClass('new')) {


            ;

        }
        else
            swal({
                title: "成功",
                text: "清空地址成功,重启后生效",
                type: "success"
            });

    });
});
