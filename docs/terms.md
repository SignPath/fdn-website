---
layout: default
header: Code of conduct
---

> **Draft**
>
> The code of conduct is still in a draft version.
{:.panel.warning}

# SignPath Foundation conditions for Open Source projects

This page details what conditions must be met by OSS projects in order to be eligible for signing by SignPath Foundation.

## Conditions for free OSS SignPath.io subscriptions

* **No malware:** The project must not contain malware or potentially unwanted programs.
* **OSS License:** The project must use an [OSI-approved Open Source license](https://opensource.org/licenses) without commercial dual-licensing for all components.
* **No proprietary code:** The project may not contain any proprietary, non open-source component (especially code published by a maintainer or an affiliated person/organization). However, you may include System Libraries in signed packages. For a useful definition of System Libraries, see section 1 of the [GPL v3 license](https://www.gnu.org/licenses/gpl-3.0.html).
* **Maintained:** The project must be actively maintained.
* **Released:** The project must already be released in the form that should be signed.
* **Documented:** The project's functionality must be described on its download page or in the app store entry of the respective platform.

If you bring your own certificate, that's it. If your certificate is issued by *SignPath Foundation*, see the next section for additional constraints.

## Conditions for free code signing certificates from *SignPath Foundation*

The code signing certificate is issued to *SignPath Foundation*. This means that *SignPath Foundation* is the publisher of the OSS project. *SignPath Foundation* will therefore define and execute technical constraints and require project members to follow certain rules. If any of the rules in the Code of Conduct are violated by the project, *SignPath Foundation* reserves the right to

* pause or terminate the subscription without prior notice
* revoke the certificate effective immediately or retroactively

### Conditions for what can be signed

* **Sign your own projects only**

  The team responsible for code signing must also be the team responsible for development and maintenance, including ownership of the source code repository.

* **Sign your own binaries only**

  The team must only sign software artifacts built from their own source code.

  * Your team must be the maintainers of all source code files and build scripts.
  * If you need signed libraries from another OSS project ("upstream"), ask them to get a signature via *SignPath Foundation* or any other means.
  * If you need to build your own modified version of upstream software, you may sign it with your project’s certificate if
    * the upstream project publishes signed builds.
    * your project visibly uses a fork of the upstream project, e.g. using GitHub’s fork feature.
    * the release branches you use for signing are based on upstream branches that are usually signed.
    * you fulfill all other obligations as required for your own project by this policy, e.g. code reviews for all changes of the upstream code base.
  * You may include unsigned binaries of upstream OSS projects, e.g. DLL files, in your signed packages, e.g. MSI installers.
    * We kindly ask you to try and get as much signing coverage as you can. If you use upstream libraries, please ask their maintainers to sign their code. You are welcome to point your upstream projects to *SignPath Foundation* to get their libraries signed.
    * While we do realize that this is currently not feasible, we reserve the right to require that signed packages only include signed program and library files in the future.

  _We reserve the right to enforce the implementation of additional best practices in the future, such as the generation of SBOM files, as the industry adoption progresses._

* **No hacking tools**
  
  Software must not include features designed to identify or exploit security vulnerabilities or circumvent security measures of their execution environment. This includes security diagnosis tools that actively scan for and highlight exploitable vulnerabilities, e.g. by identifying unprotected network ports, missing password protection etc.
  
  This clause _does not_ probibit:

  * features that detect _actual_ security breaches, e.g. traces of being hacked, presence of malware or potentially unwanted programs 
  * scanning software artifacts during development or testing (since this occurs outside the software's execution environment)

  We are aware of the utility of white hat security tools, but cannot sign them using SignPath Foundation certificates at this time.

### Conditions for end user interactions

* **Respect user privacy and security**

  Software must not include features that compromise the privacy or security of users and their systems.
  
  Software that collects user data and transfers it to systems not specified by the user must a) describe this behavior in a privacy policy, b) display this policy during installation and c) include installation options to disable these functions.

* **Announce system changes**

  Software must not modify the user’s system configuration without proper warnings.

* **Provide uninstallation**

  Software that includes instructions or automated facilities for installation must also include instructions or automated facilities for uninstallation.

### Conditions for OSS contributors

* **Follow security best practices**
  
  All team members must use multi-factor authentication for both SignPath and source code repository access (e.g. GitHub).

* **Assign code signing roles**

  The OSS project team must self-organize to create a team structure with clear responsibilities:

  * **Authors**: people who are trusted to modify the source code in the project’s version control system without additional reviews.
  * **Reviewers**: each change proposed by people who are not committers (e.g. pull requests) must be reviewed by a team member.
  * **Approvers**: each signing request must be approved by a team member trusted by the entire team to decide if a certain release can be code signed.

### Conditions for the website / repository

* **Specify a code signing policy**

  A code signing policy must be specified on the project’s home page.

  * Use the term "**Code signing policy**" on your project’s home page and download/release pages (section header or link to a dedicated page).
  * Include the following information:
    * "Free code signing provided by [SignPath.io](https://about.signpath.io), certificate by [SignPath Foundation]"
    * Team roles and their members (see above, may include references to the project’s permission groups). Example (markdown syntax):
      * Committers and reviewers: `[Members team](https://github.com/orgs/…/teams/members)`
      * Approvers: `[Owners](https://github.com/orgs/…/people?query=role%3Aowner)`
    * Privacy policy:
      * Link to your privacy policy or specify "This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it".
      * Remember to specify the privacy policies of other Open Source or third party components or services your application uses if your users are affected.

  In the future, SignPath may provide code signing policy pages for all projects that just need to be linked.

### SignPath configuration requirements

* **Artifact configuration**
  * All signed binaries must have **metadata attributes set and enforced** using [file metadata restrictions]
    * Set all *product name* attributes to your project's name.
    * Set all *product version* attributes to the same value in each build.
    * (remember that upstream OSS projects' binaries must not be signed using your subscription, but may be included in signed packages and installers)

### Other conditions

* **Don't fight the system**

  You must accept all technical constraints in place for SignPath.io OSS subscriptions and not try to work around them. Noteworthy constraints include:

  * Binary artifacts must be built from source code in a verifiable way.
  * Every release needs manual approval for signing.

  Note that some constraints are not automatically enforced yet.

* **Investigate accusations of violation**

  When SignPath Foundation receives complaints about violation of the Code of Conduct, the project team must assist in verification, investigation and root cause analysis.

## *SignPath Foundation* certificate promises

If software has a valid signature using a "SignPath Foundation" certificate, the following verifications are implied:

* *SignPath Foundation* performs initial verification of **project reputation and control**. Note that we don't repeat these verifications periodically.

* For each release, *SignPath.io* verifies the origin of signed files. A signature confirms that **the binary is a valid, automated build resulting from the source code** at the noted source code repository. This verification is automatic and technically enforced. Note that *source code* includes build scripts and CI configurations in the repository. Any code review must therefore put special attention to these files.

If you feel that a certain file signed with a *SignPath Foundation* certificate violates our policy, especially with regard to signing of malware or potentially unwanted programs, please report it to [support@signpath.io](mailto:support@signpath.io) with a concise report and proof of the violation. We will verify the claim, contact the project team and take appropriate action, including, if warranted, revocation of the certificate provided to this project.

***SignPath Foundation* cannot acccept any liability for damages resulting from software signed with certificates that were issued to *SignPath Foundation* and provided to Open Source projects.**

## Common misunderstandings

* **SignPath issues certificates:** Since we are not a Certificate Authority (CA), we cannot issue certificates to you, your project, or anybody else. But even a CA will not issue certificates to an OSS project - a code signing certificate must always be issued to a legal entity. What we actually do is get certificates issued to "SignPath Foundation" and let OSS projects use them.
* **Any project can get a SignPath certificate**: Since our name is on the certificate, our name and reputation is at stake. We cannot risk signing malware or other unwanted software. Closing the gap between source code and signed binaries is key here, but not always sufficient. In other words: we cannot sign binaries based on source code that nobody knows. For executable programs that may be downloaded and executed based on our signature, we require a certain verifiable reputation. (Not for developer libraries/components/packages though.)
* **Projects have a right to get a certificate**: The current CA regime does not recognize OSS projects, it is based on legal ownership and responsibility only. SignPath replaces these formal conditions with technical conditions, but in the end we too must accept the law of the land: the only way to offer our service is to provide certificates in our own name. We can only do this for projects that clearly meet our stated requirements. Some of these rules are soft and fuzzy, and we're not claiming that we always get it right. We try to be as fair as we can based on the knowledge we have, but ultimately it can only be our decision to accept or reject a project. We're under no obligation to accept your project, and there is no independent arbitration mechanism. This does not mean that we somehow reject your mission or doubt your skills or integrity. It only means that we're not comfortable taking the responsibility. We will listen to arguments about your specific situation, but we generally don't discuss policy. Please don't argue with us, we can only provide this service if we can keep the manual work for each applicant to a minimum.

[file metadata restrictions]:https://about.signpath.io/documentation/artifact-configuration/reference#metadata-restrictions

[SignPath Foundation]:{{ site.url }}
[SignPath.io]:https://signpath.io
