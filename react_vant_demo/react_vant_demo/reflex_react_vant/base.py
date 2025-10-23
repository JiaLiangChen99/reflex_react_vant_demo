"""Base classes for ReactVant components."""

import reflex as rx


class ReactVantBase(rx.Component):
    """Base class for all ReactVant components.
    
    This base class provides common functionality for all ReactVant components,
    including setting the library name and importing global styles.
    """

    # The React library to wrap.
    library = "react-vant"

    def add_imports(self):
        """Add imports for the react-vant library.
        
        Returns:
            Dict[str, Any]: A dictionary of imports to add.
        """
        # Import the global styles for react-vant
        return {
            "": "react-vant/lib/index.css"
        }


class ReactVantNoSSRBase(rx.NoSSRComponent):
    """Base class for ReactVant components that don't support SSR.
    
    This base class is used for components that require client-side rendering
    and are not compatible with Server-Side Rendering (SSR).
    """

    # The React library to wrap.
    library = "react-vant"

    def add_imports(self):
        """Add imports for the react-vant library.
        
        Returns:
            Dict[str, Any]: A dictionary of imports to add.
        """
        # Import the global styles for react-vant
        return {
            "": "react-vant/lib/index.css"
        }