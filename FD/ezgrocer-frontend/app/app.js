import Vue from "nativescript-vue";
//components
import pp00 from './components/0-TestMenu'
import pp01 from './components/1-Login' //done
import pp02 from './components/2-LastPurchase' // done
import pp03 from './components/3-InsertReceipt' //done
import pp04 from './components/4-SnapReceipt' //done
import pp05 from './components/5-ManuallyInput'

import pp07 from './components/7-SetUpDone' //done
import pp08 from './components/8-NonFirstTime'
import pp09 from './components/9-BuyAgain' //done
import pp10 from './components/10-TrackYourStock'

new Vue({

    template: `
        <Frame>
            <pp01/>
        </Frame>`,

    components: {
        pp01
    }
}).$start();