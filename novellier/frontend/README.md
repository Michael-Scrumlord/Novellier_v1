# Novellier Frontend

This directory contains the frontend application for Novellier.

## Setup
This frontend project is intended to be set up using `create-react-app` or a similar modern JavaScript toolchain (e.g., Vite).

To initialize the project fully:
1. Ensure you have Node.js and npm (or yarn) installed.
2. If you haven't already, you might want to run `npx create-react-app .` within this directory (or your chosen tool's equivalent command) to scaffold the project. This will replace the basic `package.json` and set up the necessary scripts and dependencies.
   **Note:** Running `create-react-app .` in an existing directory requires the directory to be largely empty or for you to confirm overwriting certain files. Given this `README.md` and `package.json` exist, you might need to temporarily move them, run the command, and then integrate them back. Alternatively, create a new project and copy over the `src` and `public` contents.

## Available Scripts

Once properly initialized (e.g., with `create-react-app`), you will likely have scripts such as:

### `npm start` or `yarn start`
Runs the app in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### `npm test` or `yarn test`
Launches the test runner in interactive watch mode.

### `npm run build` or `yarn build`
Builds the app for production to the `build` folder.

## Further Development
The `src/App.js` provides a basic entry point. Components are organized under `src/components`. Services (like API interaction) will be in `src/services`. Static assets are in `public`.
