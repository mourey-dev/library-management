<template>
  <div
    v-if="visible"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm"
  >
    <div class="bg-white w-full max-w-lg rounded-2xl shadow-2xl p-8 relative">
      <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">
        Return Book
      </h2>

      <form @submit.prevent="handleSubmit" class="space-y-5">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">
            Borrowed Transaction
          </label>
          <select
            v-model="selectedTransactionId"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-500 focus:outline-none"
            required
          >
            <option disabled value="">Select a transaction</option>
            <option
              v-for="tx in borrowedTransactions"
              :key="tx.id"
              :value="tx.id"
            >
              {{ tx.user.first_name }} {{ tx.user.last_name }} – “{{
                tx.book.title
              }}”
            </option>
          </select>
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">
            Return Date
          </label>
          <input
            type="date"
            v-model="returnDate"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-green-500 focus:outline-none"
            required
          />
        </div>

        <div class="flex justify-end gap-3 pt-4">
          <button
            type="button"
            @click="close"
            class="px-4 py-2 rounded-lg border border-gray-300 text-gray-700 hover:bg-gray-100 transition"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="px-5 py-2 rounded-lg bg-green-600 text-white hover:bg-green-700 transition"
          >
            Return
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";

const props = defineProps({
  visible: Boolean,
  transactions: Array,
});

const emit = defineEmits(["close", "saved"]);

const selectedTransactionId = ref("");
const returnDate = ref(new Date().toISOString().split("T")[0]);

const borrowedTransactions = computed(() =>
  props.transactions.filter((tx) => tx.status === "borrowed")
);

function resetForm() {
  selectedTransactionId.value = "";
  returnDate.value = new Date().toISOString().split("T")[0];
}

async function handleSubmit() {
  try {
    const transaction = props.transactions.find(
      (t) => t.id === selectedTransactionId.value
    );

    if (!transaction) throw new Error("Invalid transaction selected.");

    await axios.post(`http://localhost:8000/api/return/${transaction.id}/`, {
      date: returnDate.value,
    });

    emit("saved");
    close();
    toast.success("Book returned successfully!", {
      autoClose: 1500,
      pauseOnFocusLoss: false,
    });
  } catch (error) {
    console.error("Return failed:", error);
    toast.error("Failed to return book.", {
      autoClose: 1500,
      pauseOnFocusLoss: false,
    });
  }
}

function close() {
  resetForm();
  emit("close");
}
</script>
