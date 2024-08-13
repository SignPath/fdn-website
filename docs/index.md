---
layout: home
---

<section class='home right bg-black font-white top-section'>
    <div>
        <!--<div class='img'>
            <div>
                <img src='assets/img/cropped-OSI-horizontal-large.webp' title='{{ site.title }}' />
            </div>
        </div>-->
        <div class='center'>
            <h1>Free Code Signing for Open Source software</h1>
            <p>
                No more installation warnings. SignPath Foundation provides you with a code signing certificate that provides a clear link between your repository and the published binary.
            </p>
            <p class='buttons'>
                <a class='btn btn-primary' href='/apply'>Apply</a>
                <!--<a class='How it works' href='#how-it-works'>How it works&nbsp;&nbsp;{%- include svg/arrow-right-solid.svg -%}</a>-->
            </p> 
        </div>
    </div>
</section>

<section class='bg-blue font-white small-v-padding'>
    <div>
        <h4 class='center'>The open source community trusts SignPath Foundation<br></h4>
        <div class='carousel'>
            <ul>
                <li title='Stellarium'>{%- include svg/projects/stellarium.svg -%}</li>
                <li title='Vim'>{%- include svg/projects/vim.svg -%}</li>
                <li title='LiteDB'>{%- include svg/projects/litedb.svg -%}</li>
                <li title='Flameshot'>{%- include svg/projects/flameshot.svg -%}</li>
                <li title='Git Extensions'>{%- include svg/projects/git-extensions.svg -%}</li>
                <li title='Nuke'>{%- include svg/projects/nuke.svg -%}</li>
            </ul>
            <a class='left' href='#'>
                {%- include svg/angle-left-solid.svg %}
            </a>
            <a class='right' href='#'>
                {%- include svg/angle-right-solid.svg %}
            </a>
        </div>
        <h4 class='center'><a class='btn btn-secondary' href='/projects'>View all projects&nbsp;&nbsp;{%- include svg/arrow-right-solid.svg -%}</a></h4>
    </div>
</section>

<section class='home'>
    <div class='columns-2'>
        <div markdown="1">

## The Challenge

Getting a code signing certificate for your OSS project is difficult:
* You have to go through a cumbersome process with a certificate authority to verify your identity or find an organization that vouches for you.
* The certificate is issued to you personally and not to your project. 
* Your users have no means of verifying that the software they install was built from the OSS repository.
* The private key you receive is on a USB token, impossible to plug into your cloud-based build processes.
* You have to pay fees for every certificate issuance or re-issuance.

</div>
<div markdown="1">

## The Solution

* SignPath Foundation provides you with a code signing certificate.
* No need for personal identification, we verify that the binary was built from your open source repository and vouch for that with our name.
* By using <a href='https://about.signpath.io'>SignPath.io</a> for code signing, the private key of your certificate is securely generated and stored on our Hardware Security Module (HSM).
* Integration in your automated build process is simple.
* For OSS projects, our services are free of charge.

</div>
    </div>
</section>