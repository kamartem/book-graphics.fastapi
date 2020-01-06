// Imports
import plugin0 from '/opt/app/node_modules/react-static-plugin-reach-router/browser.api.js'

// Plugins
const plugins = [{
        location: "/opt/app/node_modules/react-static-plugin-source-filesystem",
        plugins: [],
        hooks: {}
      },
{
        location: "/opt/app/node_modules/react-static-plugin-reach-router",
        plugins: [],
        hooks: plugin0({})
      },
{
        location: "/opt/app/node_modules/react-static-plugin-sitemap/dist",
        plugins: [],
        hooks: {}
      },
{
        location: "/opt/app",
        plugins: [],
        hooks: {}
      }]

// Export em!
export default plugins