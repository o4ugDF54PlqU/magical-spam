init python:

    import math
    import pygame

    class Charge(renpy.Displayable):

        def __init__(self, child, label, charge_multiplier, **kwargs):
            global decreasing_charge
            decreasing_charge = 0

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Charge, self).__init__(**kwargs)

            # The child.
            self.child = renpy.displayable(child)

            self.label = label
                
            self.charge_multiplier = charge_multiplier

            # The alpha channel of the child.
            self.alpha = 0.0

            # The width and height of us, and our child.
            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):

            global last_event_time
            current_time = pygame.time.get_ticks()
            time_since_last_event = current_time - last_event_time
            last_event_time = current_time

            decrease_charge(0.0001 * time_since_last_event)
            
            # Check if the alpha has changed.
            if self.alpha != decreasing_charge:
                self.alpha = decreasing_charge

            # Create a transform, that can adjust the alpha channel of the
            # child.
            t = Transform(child=self.child, alpha=self.alpha)

            # Create a render from the child.
            child_render = renpy.render(t, width, height, st, at)

            # Get the size of the child.
            self.width, self.height = child_render.get_size()

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (0, 0))

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the render.
            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                increase_charge(0.03 * self.charge_multiplier)
                check_win(self.label)
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                increase_charge(0.04 * self.charge_multiplier)
                check_win(self.label)

            # If the alpha has changed, trigger a redraw event.
            # if self.alpha != decreasing_charge:
            #     self.alpha = decreasing_charge
            #     renpy.redraw(self, 0)

            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]