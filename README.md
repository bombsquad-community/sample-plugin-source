# sample-plugin-source

Template repository to allow people easily create their own plugin sources to use with plugin manager.

## How does this work?

- If you have [bombsquad-community/plugin-manager](https://github.com/bombsquad-community/plugin-manager)
  installed in your game, simply go to the category selection pop-up window and add
  `bombsquad-community/sample-plugin-source` as a plugin source. Press refresh and plugins from this
  repository will now be visible!
- Plugin manager will default to picking up plugins from the `main` branch of the custom source repository.
  You can specify a different branch by suffixing the source URI with `@branchname`, such as
  `bombsquad-community/sample-plugin-source@experimental`.
- The plugin-manager expects a [category.json](category.json) file for all 3rd party plugin
  sources. This file acts as a metadata source for all the plugins present in the repository.
  Please refer to it if you're interested in creating your own 3rd party plugin source.
- This README file is a reference for modders wanting to setup their own 3rd plugin source and is not
  mandatory.

## License

All code in this repository is unlicensed. You can change this license when creating your own plugin
source as per your requirement.
