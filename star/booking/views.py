from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Booking
from .forms import EditBooking, NewBooking

active_fields = [
    'user', 'sauna', 'entry_date', 'entry_time', 'quantity', 'hours'
]


class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'


class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'


class BookingCreateView(CreateView):
    form_class = NewBooking
    template_name = 'booking_new.html'

    def get_success_url(self):
        return reverse_lazy('booking_detail', kwargs={'pk': self.get_context_data()['booking'].pk})

    def form_valid(self, form):
        new_booking = form.save()
        booking = Booking.objects.get(id=new_booking.pk)
        booking.user = self.request.user
        booking.save()
        return HttpResponseRedirect(reverse_lazy('booking_detail', kwargs={'pk': new_booking.pk}))


class BookingUpdateView(UpdateView):
    model = Booking
    form_class = EditBooking
    template_name = 'booking_edit.html'
    success_url = reverse_lazy('booking_list')


class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('booking_list')