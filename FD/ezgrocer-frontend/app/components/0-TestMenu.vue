<template>
    <page>
        <ActionBar title="My App">
            <NavigationButton text="Go back"  android.systemIcon="ic_menu_back" @tap="goBack" />
        </ActionBar>
        <WrapLayout>
            <stackLayout orientation="horizontal">
                <button width="50" height="50" text="01" @tap="$navigateTo(p01)"></button>
                <button width="50" height="50" text="02" @tap="$navigateTo(p02)"></button>
                <button width="50" height="50" text="03" @tap="$navigateTo(p03)"></button>
                <button width="50" height="50" text="04" @tap="$navigateTo(p04)"></button>
                <button width="50" height="50" text="05" @tap="$navigateTo(p05)"></button>
            </stackLayout>
            <stackLayout orientation="horizontal">
                <button width="50" height="50" text="06" @tap="$navigateTo(p06)" isEnabled="false"></button>
                <button width="50" height="50" text="07" @tap="$navigateTo(p07)"></button>
                <button width="50" height="50" text="08" @tap="$navigateTo(p08)"></button>
                <button width="50" height="50" text="09" @tap="$navigateTo(p09)"></button>
                <button width="50" height="50" text="10" @tap="$navigateTo(p10)"></button>
            </stackLayout>
            <stackLayout orientation="horizontal">
                <button width="50" height="50" text="11" @tap="$navigateTo(p11)"></button>
                <button width="50" height="50" text="12" @tap="$navigateTo(p12)"></button>
                <button width="50" height="50" text="13" @tap="$navigateTo(p13)"></button>
                <button width="50" height="50" text="14" @tap="$navigateTo(p14)"  isEnabled="false"></button>
                <button width="50" height="50" text="15" @tap="$navigateTo(p15)"  isEnabled="false"></button>
            </stackLayout>
        </WrapLayout>
    </page>
</template>

<script>
import pp00 from './0-TestMenu'
import pp01 from './1-Login'
import pp02 from './2-LastPurchase'
import pp03 from './3-InsertReceipt'
import pp04 from './4-SnapReceipt'
import pp05 from './5-ManuallyInput'

import pp07 from './7-SetUpDone'
import pp08 from './8-NonFirstTime'
import pp09 from './9-BuyAgain'
import pp10 from './10-TrackYourStock'
import pp13 from './11-Store'

export default {
    data(){
        return{
            p01:pp01,
            p02:pp02,
            p03:pp03,
            p04:pp04,
            p05:pp05,
            p07:pp07,
            p08:pp08,
            p09:pp09,
            p10:pp10,
            p13:pp13     
        }
    },
    methods: {

    }
}
</script>

