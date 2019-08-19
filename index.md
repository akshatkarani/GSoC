---
layout: report
student: Akshat Karani
student_link: https://akshatkarani.github.io
organisation: coala
organisation_link : https://coala.io
project: Next Generation Action System
project_link: https://summerofcode.withgoogle.com/projects/#5450946933424128
tarball: https://github.com/akshatkarani
mentors: >
 [Abhinav Kaushlya](https://github.com/abhishalya), [Vamshi Krishna](https://github.com/Vamshi99) & [Kriti Rohilla](https://github.com/kriti21)
phase:
 - Bonding : https://gitlab.com/coala/GSoC/gsoc-2019/-/milestones/19?title=BONDING_Next_Gen_Action_System
 - Phase 1 : https://gitlab.com/coala/GSoC/gsoc-2019/-/milestones/20?title=PHASE_1_Next_Gen_Action_System
 - Phase 2 : https://gitlab.com/coala/GSoC/gsoc-2019/-/milestones/21?title=PHASE_2_Next_Gen_Action_System
 - Phase 3 : https://gitlab.com/coala/GSoC/gsoc-2019/-/milestones/22?title=PHASE_3_Next_Gen_Action_System
bio: >
 I'm a third year student of Computer Science & Engineering at
 Indian Institute of Technology, Dharwad. I am enthusiatic about
 contributing to open source and working on my own projects.
 I participated in GSoC and worked with [coala](https://coala.io) to provide
 support for bears to define their own custom actions. I also provided support
 for bears to suggest multiple patches for a problem.
social:
 - GitHub:
   - username: akshatkarani
   - link: https://github.com/akshatkarani
 - GitLab:
   - username: akshatkarani
   - link: https://gitlab.com/akshatkarani
 - Gitter:
   - username: akshatkarani
   - link: https://gitter.im/akshatkarani
email: akshatkarani@gmail.com
blog: http://akshatkarani.github.io/blog
activity:
 - 0:
   - repo: cEP
   - link: https://github.com/coala/cEPs/pull/182/
   - details: > 
      cEP for Project
 - 1:
   - repo: coala
   - link: https://github.com/coala/coala/pull/6039
   - details: > 
       Fixing color_letter function in ConsoleInteraction module
 - 2:
   - repo: coala
   - link: https://github.com/coala/coala/pull/6029
   - details: > 
      Adding actions attribute to Result class
 - 3:
   - repo: coala-bears
   - link: https://github.com/coala/coala-bears/pull/2927
   - details: >
      EditCommitMessageAction and AddNewlineAction for GitCommitBear
 - 4:
   - repo: coala
   - link: https://github.com/coala/coala/pull/6046
   - details: >
      Tutorial for writing bear specific actions
 - 5:
   - repo: coala
   - link: https://github.com/coala/coala/pull/6057
   - details: >
      Implementing AlternatePatchAction and support for bears to provide multiple patches
 - 6:
   - repo: coala-bears
   - link: https://github.com/coala/coala-bears/pull/2947
   - details: >
      DeleteFileAction for DuplicateFileBear
 - 7:
   - repo: coala-bears
   - link: https://github.com/coala/coala-bears/pull/2948
   - details: >
      Providing multiple patches for FilenameBear
 - 8:
   - repo: coala
   - link: https://github.com/coala/coala/pull/6060
   - details: >
      Update the docs to explain how bears can suggest multiple patches
 
---

### Next generation action system


##### Work Done

- Made some changes to `action_dict`, now the key of the dictionary
is `id` of the object rather that name of the class.

- Updated the `color_letter` function in ConsoleInteraction module to display
the action on console properly.

- I added two new attribute to `Result` class:

-- `actions` attribute which is a list of action instances and
allows bears to define their own actions.

-- `alternate_diffs` attribute which is a list of dictionaries
where each element is an alternate patch.

- Implemented some bears specific actions:

-- `EditCommitMessageAction` for `GitCommitBear` which opens an editor
in which user can edit the commit message.

-- `ApplyPatchAction` for `GitCommitBear` which adds a newline between
shortlog and body of commit message when applied.

-- `DeleteFileAction` for `DuplicateFileBear` which deletes one of the duplicate file.

- Wrote a tutorial which describes how to write bear specific actions.

- Updated FilenameBear to provide multiple patches wherever it cannot guess the naming convention to use.

- Updated the docs to briefly explain how bears can suggest multiple patches.

##### Challenges

It was a great learning experience overall, and I did face a few problems throughout but I was able to tackle/workaround them with help of my mentors. The first problem I faced was allowing bears to define their own actions without affecting the default actions. There were many possible options to implement this and selecting one which would be feasible and works was a difficult task. Also allowing multiple patches without making huge changes in existing framework was challenging. Writing tests for some of the actions implemented which involved deleting a file or amending commit messages was tricky.


##### Work to be done

Main advantage after this project is that now many useful custom actions can be implemented for bears. Identifying where custom actions can be useful and implementing them will be a community driven process.
Another thing which can be done is extending some of the existing bears to provide multiple patches.
Also allowing actions to be initialized with custom descriptions would be really helpful because currently actions particularly AlternatePatchActions are displayed as `Show AlternatePatch` and a feature like above will display that actions specific descriptions which would be helpful to the user.
