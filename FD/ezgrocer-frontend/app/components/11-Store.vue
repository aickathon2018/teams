<template>
	<Page class="actio">
		<ActionBar title="Nearest Stores" class="action-bar" />
		<WebView src='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3983.881541759781!2d101.72621131470464!3d3.1260099977237448!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31cc3613698a6b23%3A0xa96ac8e1bbdddea6!2sAEON+Taman+Maluri+Shopping+Centre!5e0!3m2!1sen!2smy!4v1542480488559" width="400" height="300" frameborder="0" style="border:0" allowfullscreen></iframe>' />
		
		<stackLayout height="100%">

		<StackLayout height="15%" >
			<StackLayout orientation="horizontal" width="100%" height="100%">
				<Image src="https://storage.googleapis.com/fd-photo-dump/icon_asset/Aeon%20.jpg" width="30%" margin="10" height="100%" />
				<StackLayout width="70%" margin="10" height="100%">
					<label class="text-left h1 font-weight-bold" text="AEON" margin="10" />
					<label class="text-left h3" text="Crowd: Low" margin="10" />
				</StackLayout>
			</StackLayout>
		</StackLayout>

		<StackLayout height="15%" >
			<StackLayout orientation="horizontal" width="100%" height="100%">
				<Image src="https://storage.googleapis.com/fd-photo-dump/icon_asset/KK%20mart.png" width="30%" margin="10" height="100%" />
				<StackLayout width="70%" margin="10" height="100%">
					<label class="text-left h1 font-weight-bold" text="KK Mart" margin="10" />
					<label class="text-left h3" text="Crowd: Mid" margin="10" />
				</StackLayout>
			</StackLayout>
		</StackLayout>

		<StackLayout height="15%" >
			<StackLayout orientation="horizontal" width="100%" height="100%">
				<Image src="https://storage.googleapis.com/fd-photo-dump/icon_asset/jayagrocer.png" width="30%" margin="10" height="100%" />
				<StackLayout width="70%" margin="10" height="100%">
					<label class="text-left h1 font-weight-bold" text="Jaya Grocer" margin="10" />
					<label class="text-left h3" text="Crowd: Low" margin="10" />
				</StackLayout>
			</StackLayout>
		</StackLayout>
			<Button class="btn btn-primary btn-rounded-lg" height="10%" width="50%" text="Back" dock="bottom" @tap="$navigateTo(detailPage)" margin="40% 0 0 0"/>
		</StackLayout>

		
	</Page>
</template>

<script>
import Back from './8-NonFirstTime'

export default {
    data() {
      return {
        detailPage: Back
      }
    },
    methods: {

    }
}
</script>
