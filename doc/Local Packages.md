Assets
If a wrapped component depends on assets such as images, scripts, or stylesheets, these can be kept adjacent to the component code and included in the final build using the rx.asset function.

rx.asset returns a relative path that references the asset in the compiled output. The target files are copied into a subdirectory of assets/external based on the module where they are initially used. This allows third-party components to have external assets with the same name without conflicting with each other.

For example, if there is an SVG file named wave.svg in the same directory as this component, it can be rendered using rx.image and rx.asset.

class Hello(rx.Component):
    @classmethod
    def create(cls, *children, **props) -> rx.Component:
        props.setdefault("align", "center")
        return rx.hstack(
            rx.image(
                src=rx.asset("wave.svg", shared=True),
                width="50px",
                height="50px",
            ),
            rx.heading("Hello ", *children),
            **props
        )

Local Components
You can also wrap components that you have written yourself. For local components (when the code source is directly in the project), we recommend putting it beside the files that is wrapping it.

If there is a file hello.jsx in the same directory as the component with this content:

// /path/to/components/hello.jsx
import React from 'react';

export function Hello({name, onGreet}) {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <button onClick={() => onGreet(name)}>Greet</button>
    </div>
  )
}

The python app can use the rx.asset helper to copy the component source into the generated frontend, after which the library path in the rx.Component may be specified by prefixing $/public to that path returned by rx.asset.

import reflex as rx

hello_path = rx.asset("./hello.jsx", shared=True)
hello_css_path = rx.asset("./hello.css", shared=True)


class Hello(rx.Component):
    # Use an absolute path starting with $/public
    library = f"$/public{hello_path}"

    # Define everything else as normal.
    tag = "Hello"

    name: rx.Var[str] = rx.Var("World")
    on_greet: rx.EventHandler[
        rx.event.passthrough_event_spec(str)
    ]

    # Include any related CSS files with rx.asset to ensure they are copied.
    def add_imports(self):
        return {"": f"$/public/{hello_css_path}"}

Considerations
When wrapping local components, keep the following in mind:

File Extensions: Ensure that the file extensions are correct (e.g., .jsx for React components and .tsx for TypeScript components).
Asset Management: Use rx.asset with shared=True to manage any assets (e.g., images, styles) that the component depends on.
Event Handling: Define any event handlers (e.g., on_greet) as part of the component's API and pass those to the component from the Reflex app. Do not attempt to hook into Reflex's event system directly from Javascript.
Use Case
Local components are useful when shimming small pieces of functionality that are simpler or more performant when implemented directly in Javascript, such as:

Spammy events: keys, touch, mouse, scroll -- these are often better processed on the client side.
Using canvas, graphics or WebGPU
Working with other Web APIs like storage, screen capture, audio/midi
Integrating with complex third-party libraries
For application-specific use, it may be easier to wrap a local component that provides the needed subset of the library's functionality in a simpler API for use in Reflex.
Local Packages
If the component is part of a local package, available on Github, or downloadable via a web URL, it can also be wrapped in Reflex. Specify the path or URL after an @ following the package name.

Any local paths are relative to the .web folder, so you can use ../ prefix to reference the Reflex project root.

Some examples of valid specifiers for a package called @masenf/hello-react are:

GitHub: @masenf/hello-react@github:masenf/hello-react
URL: @masenf/hello-react@https://github.com/masenf/hello-react/archive/refs/heads/main.tar.gz
Local Archive: @masenf/hello-react@../hello-react.tgz
Local Directory: @masenf/hello-react@../hello-react
It is important that the package name matches the name in package.json so Reflex can generate the correct import statement in the generated javascript code.

These package specifiers can be used for library or lib_dependencies.
```
class GithubComponent(rx.Component):
    library = (
        "@masenf/hello-react@github:masenf/hello-react"
    )
    tag = "Counter"

    def add_imports(self):
        return {"": ["@masenf/hello-react/dist/style.css"]}


def github_component_example():
    return GithubComponent.create()
```
Although more complicated, this approach is useful when the local components have additional dependencies or build steps required to prepare the component for use.

Some important notes regarding this approach:

The repo or archive must contain a package.json file.
prepare or build scripts will NOT be executed. The distribution archive, directory, or repo must already contain the built javascript files (this is common).