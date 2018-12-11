<template>
    <Page class="page">
        <ActionBar class="action-bar" height="200" padding="0 25" BackgroundColor="#e81f1f">
            <label class="text-center h1 font-weight-bold" :text="pageTitle" dock="bottom" verticalalignment="bottom" width="100%" height="30%"/>
        </ActionBar>
        <StackLayout padding="0 25">
            <StackLayout height="21%" margin="2% 0 4% 0">
                <label class="text-mute text-left h2" :text="content[0]" height="50%" width="100%" margin="8% 0 1% 0" textWrap="true"
                    style="color: #b8b8b8;"/> 
                <label class="text-mute text-center h2" :text="content[1]" height="50%" width="100%" margin="8% 0 18% 5%" textWrap="true"
                    style="color: #000000;"/> 
                    
        <!--StackLayout class="m-10" >
            <StackLayout height="13%" margin="4% 0 2% 0">
                <Label class="text-center h2" :text="content" Width="100%" textWrap="true" /-->
            </StackLayout>

            <StackLayout orientation="horizontal" height="6%" width="100%">
                                    
                <GridLayout class="input-field input-sides" width="45%" rows="auto, auto" columns="*,*">
                    <Label text="Product Name" class="label font-weight-bold" row="0" col="0" textWrap="true"/>
                </GridLayout>

                <GridLayout class="input-field input-sides" width="30%" rows="auto, auto" columns="*,*">
                    <Label text="Size" class="label font-weight-bold" row="0" col="0"  />
                </GridLayout>

                <GridLayout class="input-field input-sides" width="25%" rows="auto, auto" columns="*,*">
                    <Label text="(%)" class="label font-weight-bold" row="0" col="0" textWrap="true"/>
                </GridLayout>

            </StackLayout>

            <ListView for="item in listOfItems" padding="10 0" @itemTap="onItemTap" height="35%">
                <v-template>
                    <!-- Shows the list item label in the default color and style. -->
                    <StackLayout orientation="horizontal" width="100%" >
                        
                        <StackLayout class="input-field" width="45%" >
                            <TextField :text="item.name" class="input" style="color: #606060;" />
                        </StackLayout>

                        <StackLayout class="input-field" width="30%" >
                            <TextField :text="item.size" class="input" style="color: #606060;" />
                        </StackLayout>

                        <StackLayout class="input-field" width="25%" >
                            <TextField :text="percent(item.quantity)" class="input" :style="{color: resultcolor(item.quantity)}" />
                        </StackLayout>

                    </StackLayout>

                </v-template>
            </ListView>   

            <StackLayout orientation="vertical" height="60%">
                <Button class="btn btn-primary btn-rounded-lg" height="25%" width="40%" :text="buttonText[0]" @tap="$navigateTo(detailPage)" />
                <!--<Button class="btn btn-primary btn-rounded-lg" height="55%" width="40%" :text="buttonText[1]" @tap="$navigateTo(detailPage)" />-->
                <WebView src='<html><head><script type="text/javascript" src="https://addevent.com/libs/atc/1.6.1/atc.min.js" async defer></script></head><body><div title="Add to Calendar" class="addeventatc">Add to Calendar<span class="start">11/20/2018 12:00 PM</span><span class="end">11/20/2018 02:05 PM</span><span class="timezone">Asia/Kuala_Lumpur</span><span class="title">Grocery day</span><span class="description">TO BUY: DETERGENT DOWNY (920ML REFILL), GAREDENIA LOAF (400g), 12 EGGS NUTRIPLUS OMEGA A+</span><span class="location">AEON Mall Taman Maluri, Jusco, Jalan Jejaka, Maluri, Kuala Lumpur, Federal Territory of Kuala Lumpur</span><span class="alarm_reminder">1440</span></div></body></html>' dock="top" margin="0 0 0 21%"/>
                
            </StackLayout>

        </StackLayout>
    </Page>
</template>

<script>
import Store from './11-Store'

export default {
    data() {
      return {
        pageTitle: "GROCER TRACKER",
        buttonText: ["Store", "Confirm"], 
        content: ["We believe you should shop on:" , "20/11/2018" ],
        detailPage: Store,
        listOfItems: [
            {id: 0, name: "Sugar", size: "500g", quantity: 17} , 
            {id: 1, name: "Toothpaste", size: "100g", quantity: 26} , 
            {id: 2, name: "Tissue", size: "5", quantity: 54} ,
         ]
      }
    },
    methods: {
        resultcolor(value){
            if(value < 25)
            {
                return 'red';
            }
            else 
            {
                return 'green';
            }
        },
        percent(value){
            return value + '%';
        }
    }
}
</script>