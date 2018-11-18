<template>
	<Page class="page">
		<ActionBar title="Camera" class="action-bar" />
        <StackLayout>
            <Image :src="pictureFromCamera"/>
            <Button :text="textPicture" class="btn btn-primary" marginTop="20" @tap="takePicture"></Button>
            <Button text="Next" class="btn btn-primary" marginTop="20" @tap="$navigateTo(displayPage)"></Button>
        </StackLayout>
	</Page>
</template>

<script>
import * as camera from "../nativescriptcamera";
import * as http from "http";
import * as fs from "tns-core-modules/file-system";
import * as imageSourceModule from "tns-core-modules/image-source";
import * as firebase from "nativescript-plugin-firebase";
import Done from "./7-SetUpDone"

export default {
    data() {
        return {
            pictureFromCamera: null,
            textPicture: "Take a Picture",
            displayPage: Done,
            filepath: null,
            filename: null
        };
    },
    methods: {

        takePicture() {
            // See the options at https://github.com/NativeScript/nativescript-camera#using-the-options-to-take-memory-efficient-picture
            // for more information on how to customize the pictures you take.
            camera
                .takePicture({ width: 400, height: 500, keepAspectRatio: false , saveToGallery: true})
                .then(imageAsset => {
                    this.pictureFromCamera = imageAsset;
                    var savepath = fs.knownFolders.documents().path;
                    var filename = 'img_' + new Date().getTime() + '.jpg';
                    console.log("filename: " + this.filename);
                    this.filename = filename;
                    var filepath = fs.path.join(savepath, filename);
                    this.filepath = filepath;
                    console.log("filepath: " + this.filepath);
                    imageSourceModule.fromAsset(imageAsset).then(res => {
                        imageSource = res;        
                        var picsaved = imageSource.saveToFile(filepath, "jpg");
                        console.log("filepath: " + filepath);
                        //uploadStorage(filepath);
                    });
                })
                .catch(err => {
                    console.log("Error -> " + err.message);
                });
        }

        /*
        uploadStorage() {
            firebase.uploadFile({
            remoteFullPath: 'uploads/images/' + remoteFileName,
            localFile: fs.File.fromPath(this.filepath),
            localFullPath: filepath,
            onProgress: function (status) {
            console.log("Uploaded fraction: " + status.fractionCompleted)
            console.log("Percentage complete: " + status.percentageCompleted)
            }
        }).then(
            uploadedFile => {
            console.log("File uploaded: " + JSON.stringify(uploadedFile))
            },
            error => {
            console.log("File upload error: " + error)
            }
        )
            if (filename) {
                console.log("Saved!");
                var session = bghttp.session("image-upload");
                var request = {
                    url: "https://www.googleapis.com/upload/storage/v1/b/[BUCKET_NAME]/o?uploadType=media&name=" + this.filename,
                    method: "POST",
                    headers: {
                        "Authorization": "Bearer ya29.GltXBlqgJ6bsm76jlwiIEumRH6cza_fgU7dmKbUdIy81h2SkefcXMGG3JcO1a0SRcySOM7c6Aeqllf-2X8oxmkhch4oD11YUHNyiSJ2PLF6DnQnGSe2cLcG1eDOW",
                        "Content-Type": "image/jpeg"
                    }
                };

                // pass filepath here instead of fileUri and no need for file:// in this case
                var task = session.uploadFile(this.filepath, request);

                task.on("progress", logEvent);
                task.on("error", logEvent);
                task.on("complete", logEvent);
            } else {
                console.log("Failed To Save");
            }
            
            // Your Google Cloud Platform project ID
            const projectId = 'aickerthon-fd';

            // Imports the Google Cloud client library
            const { Storage } = require('@google-cloud/storage');

            // Creates a client
            const storage = new Storage();


            const bucketName = 'fd-photo-dump';
            // const filename = 'receipt.jpeg';
            // Uploads a local file to the bucket
            storage.bucket(bucketName).upload(this.filepath, {
                // Support for HTTP requests made with `Accept-Encoding: gzip`
                metadata: {
                // Enable long-lived HTTP caching headers
                // Use only if the contents of the file will never change
                // (If the contents will change, use cacheControl: 'no-cache')
                cacheControl: 'public, max-age=31536000',
                },
            });
    }*/
    }
};
</script>
