<template>
    <Page>
        <ActionBar class="action-bar" :title="pageTitle" flat="true" backgroundColor="rgba(232, 31, 31, 0.86)" style="font-family: Futura;line-height: normal;font-size: 24px;text-align: center;color: #000000;"/>
        <Image src="blob:https://web.whatsapp.com/5e4b4a81-6f7e-47cd-b9e5-72054f430c63" horizontalAlignment="center"/>
        <TabView :selectedIndex="selectedIndex" tabBackgroundColor="rgba(232, 31, 31, 0.86)" tabTextColor="#FFFFFF" selectedTabTextColor="#000000" style="font-family: Futura;line-height: normal;font-size: 24px;text-align: center;color: #000000;">
            <TabViewItem title="Sign In" style="font-family: Futura;line-height: normal;font-size: 24px;text-align: center;color: #000000;">
                <StackLayout>
                    <Label text="Sign in to Ez Grocer" style="font-family: Futura;line-height: normal;font-size: 30px;text-align: center;color: #000000;" padding="20 20 20 20" margin="30 20 20 20"/>
                    <TextField :text="usernameValue" hint="Username" padding="20 20 20 20" margin="10 50 10 50" textAlignment="left" style="font-family: Helvetica Neue;line-height: normal;font-size: 18px;"/>
                    <TextField :text="passwordValue" hint="Password" secure="true" padding="20 20 20 20" margin="10 50 10 50" textAlignment="left" style="font-family: Helvetica Neue;line-height: normal;font-size: 18px;"/>
                    <Button class="btn btn-primary btn-rounded-sm" height="8%" width="40%" text="GO" backgroundColor="rgba(232, 31, 31, 0.86)" style="font-family: Futura;line-height: normal;font-size: 14px;text-align: center;color: #FFFFFF;" margin="50 0 50 0" @tap="$navigateTo(nonFirstTimePage)"/>
                    <StackLayout orientation="horizontal">
                        <StackLayout class="hr-dark m-10" width="25%"></StackLayout>
                        <StackLayout width="40%"><Label text="or" textAlignment="center" width="100%"/></StackLayout>
                        <StackLayout class="hr-dark m-10" width="25%"></StackLayout>
                    </StackLayout>
                    <Label text="Sign in with" textAlignment="center"/>
                    <StackLayout orientation="horizontal">
                        <StackLayout width="20%"></StackLayout>
                        <StackLayout width="30%">
                            <Image src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBlDEjsFBcll42EDDllRBvOxEQq_873HD0ycB4txGkLToLVmLhKg" stretch="aspectFit" height="30%" margin="20 0 20 0" horizontalAlignment="right"/>
                        </StackLayout>
                        <StackLayout width="30%">
                            <Image src="https://png2.kisspng.com/20180419/xaw/kisspng-google-logo-google-search-google-account-redes-5ad81f9da5df28.3745082315241133096794.png" stretch="aspectFit" height="30%" margin="20 0 0 20" horizontalAlignment="left"/>
                        </StackLayout>
                        <StackLayout width="20%"></StackLayout>
                    </StackLayout>
                    <Button class="btn btn-outline" text="Forgot your password?" margin="30 10 0 10"></Button>
                </StackLayout>
            </TabViewItem>
            <TabViewItem title="Sign Up" style="font-family: Futura;line-height: normal;font-size: 24px;text-align: center;color: #000000;">
                <StackLayout>
                    <Label text="Sign up with Ez Grocer" style="font-family: Futura;line-height: normal;font-size: 30px;text-align: center;color: #000000;" padding="20 20 20 20" margin="30 20 20 20"/>
                    <TextField :text="usernameSignUpValue" hint="Username" padding="10 20 10 20" margin="10 50 10 50" textAlignment="left" style="font-family: Helvetica Neue;line-height: normal;font-size: 18px;"/>
                    <TextField :text="emailSignUpValue" hint="Email" padding="10 20 10 20" margin="10 50 10 50" textAlignment="left" style="font-family: Helvetica Neue;line-height: normal;font-size: 18px;"/>
                    <TextField :text="passwordSignUpValue" hint="Password" secure="true" padding="10 20 10 20" margin="10 50 10 50" textAlignment="left" style="font-family: Helvetica Neue;line-height: normal;font-size: 18px;"/>
                    <Button class="btn btn-primary btn-rounded-sm" height="8%" width="40%" text="GO" backgroundColor="rgba(232, 31, 31, 0.86)" style="font-family: Futura;line-height: normal;font-size: 14px;text-align: center;color: #FFFFFF;" margin="50 0 50 0" @tap="$navigateTo(firstTimePage)"/>
                    <StackLayout orientation="horizontal">
                        <StackLayout class="hr-dark m-10" width="25%"></StackLayout>
                        <StackLayout width="40%"><Label text="or" textAlignment="center" width="100%"/></StackLayout>
                        <StackLayout class="hr-dark m-10" width="25%"></StackLayout>
                    </StackLayout>
                    <Label text="Sign up with" textAlignment="center"/>
                    <StackLayout orientation="horizontal">
                        <StackLayout width="20%"></StackLayout>
                        <StackLayout width="30%">
                            <Image src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBlDEjsFBcll42EDDllRBvOxEQq_873HD0ycB4txGkLToLVmLhKg" stretch="aspectFit" height="30%" margin="20 20 0 0" horizontalAlignment="right"/>
                        </StackLayout>
                        <StackLayout width="30%">
                            <Image src="https://png2.kisspng.com/20180419/xaw/kisspng-google-logo-google-search-google-account-redes-5ad81f9da5df28.3745082315241133096794.png" stretch="aspectFit" height="30%" margin="20 0 0 20" horizontalAlignment="left"/>
                        </StackLayout>
                        <StackLayout width="20%"></StackLayout>
                    </StackLayout>
                </StackLayout>
            </TabViewItem>
        </TabView>
    </Page>
</template>

<script>
import NonFirstTime from './8-NonFirstTime'
import FirstTime from './2-LastPurchase'

export default {
    data() {
      return {
        pageTitle: "Ez Grocer",
        nonFirstTimePage: NonFirstTime,
        firstTimePage: FirstTime,
        usernameValue:"ali98",
        passwordValue:"11111111",
        usernameSignUpValue:"ali98",
        emailSignUpValue:"ali98@gmail.com",
        passwordSignUpValue:"11111111",
      }
    },
    methods: {

    }
}
</script>