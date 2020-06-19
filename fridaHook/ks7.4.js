Java.perform(function () {
    var string = "java.lang.String";

    // var task = Java.use("com.kuaishou.livestream.message.nano.LiveStreamMessages$PkPlayerInfo");
    // task.parseFrom.overload('[B').implementation = function (p1) {
    //     var info = this.parseFrom(p1);
    //     console.log(info);
    //     return info;
    // };
    //
    // var sss = Java.use("com.kuaishou.livestream.message.nano.LiveStreamMessages$BroadcastGiftFeed");
    // sss.parseFrom.overload('[B').implementation = function (p1) {
    //     var info = this.parseFrom(p1);
    //     console.log(info);
    //     return info;
    // };
        // SCFeedPush SCLiveWatchingList
    // var watch = Java.use("com.kuaishou.livestream.message.nano.LiveStreamMessages$SCLiveWatchingList");
    // watch.parseFrom.overload('[B').implementation = function (p1) {
    //     var info = this.parseFrom(p1);
    //     console.log(info);
    //     return info;
    // };

//     var ss = Java.use("com.cmbchina.ccd.library.cache.a.a");
//     ss.a.overload(string).implementation = function (p1) {
//         console.log("aaaaaaaaaaaaaaaaa: " + p1);
//         var sss = this.a(p1);
//         console.log("aaaaaaaaaaaaaaaaa: " + sss);
//         return sss;
//     };
//


      var ss = Java.use("com.cmbchina.ccd.library.cache.defaultimpl.encrypt");
      ss.a.overload(string).implementation = function (p1) {
          console.log("aaaaaaaaaaaaaaaaa: " + p1);
          var sss = this.a(p1);
          console.log("aaaaaaaaaaaaaaaaa: " + sss);
          return sss;
      };


//    var dd = Java.use("com.cmbchina.ccd.security.keys.Key");
//    dd.decipherStr.overload(string).implementation = function (p1) {
//        console.log("decipherStrdecipherStr: " + p1);
//        var sss = this.decipherStr(p1);
//        console.log("decipherStrdecipherStr: " + sss);
//        return sss;
//    };



//    var dd = Java.use(" com.cmbchina.ccd.pluto.cmbActivity.aggregatetraffic.activity.onEventMainThread");
//    dd.decipherStr.overload(string).implementation = function (p1) {
//        console.log("decipherStrdecipherStr: " + p1);
//        var sss = this.decipherStr(p1);
//        console.log("decipherStrdecipherStr: " + sss);
//        return sss;
//    };

    // console.log(ss.b("Hl/8JBmtmePKYD7TLpQKjdxgalaEFPifrsrbJfo/zWZYD69XeaR2/s90VNQDfB0c8JsAozSEJoYr4d/8sG7sT/1pj5pihqbNI1XOsisDl/C0WHRtFS0ijS6HiqJSwvtEzALQfYk5Vlw="));

    console.log("=====================start=================")
});

function sleep(numberMillis) {
    var now = new Date();
    var exitTime = now.getTime() + numberMillis;
    while (true) {
        now = new Date();
        if (now.getTime() > exitTime)
            return;
    }
}

function trace() {
    Java.perform(function () {
        var thr = Java.use("java.lang.Thread");
        var list = thr.currentThread().getStackTrace();
        for (var k in list) {
            console.log(list[k].getClassName() + "." + list[k].getMethodName() + "()\t" + list[k].getLineNumber())
        }
    });
}

