function bol(){

//        if (top.location != self.location) {
//            return false;
//        }


        var real_jump_address = 'https://s.click.taobao.com/t?e=m%3D2%26s%3DQCxeO3rjJC9w4vFB6t2Z2ueEDrYVVa64yK8Cckff7TVRAdhuF14FMVKbWjSHff6A1aH1Hk3GeOjCLbnHYgDO7RXvAaHY+k4sE1p8UKWvOoOYHHoEKDSsVB8X7G7Q37BaEHESUfc7ygHrmWdQF0imwYwe6/tGg2/RSyiL934V8t7Ny6VfD8aHxJ6P/jo9mSm0fWsUjZoD5RCiPjN8FPKfVoLiglfzF7Nrm/AqrVg3iolmYKmPQjlXgib4FRL6yn47QLQtqj2NQCM7Qq3IsVviSLpPcC+jxcBwIYULNg46oBA%3D&amp;amp;union_lens=lensId:0b0fc0d4_0c42_16e38989d39_2d47&amp;amp;xId=HfEnx5soKtEOSU6xpxHyXf5L2yvJ5eyqro75Yu86HVvwAc6nBXSnV71dtNhBUvNRcTRx2Z74G3KFfywtwOixkM&amp;amp;union_lens=lensId:0b1b5435_0cca_16e38989d3b_d834&amp;amp;utm_campaign=client_share&amp;amp;app=aweme&amp;amp;utm_medium=ios&amp;amp;tt_from=copy&amp;amp;utm_source=copy&amp;amp;ref=&amp;amp;et=trFa2PhmCJKS%2FG53hCfeuDhoOyNq6XyZ&amp;ref=&amp;et=IBep79g4BBq9hGxZdVU3FJXkMi5N%2BqCa'
//        return real_jump_address
        if (!window.attachEvent) {
            document.write('<input style="display:none" type="button" id="exe" value="" onclick="window.location=\'' + real_jump_address + '\'">');
            document.getElementById('exe').click();
        } else {
            document.write('<a style="display:none" href="' + real_jump_address + '" id="exe"></a>');
            document.getElementById('exe').click();
        }
//        return real_jump_address
    }//end of bol()
    bol();